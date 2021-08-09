import minimalmodbus
import serial
from retrying import retry
from epevermodbus.extract_bits import extract_bits


class EpeverChargeController(minimalmodbus.Instrument):
    """Instrument class for Epever Charge Controllers.

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    """

    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
        self.serial.baudrate = 115200
        self.serial.bytesize = 8
        self.serial.parity = serial.PARITY_NONE
        self.serial.stopbits = 1
        self.serial.timeout = 1
        self.mode = minimalmodbus.MODE_RTU
        self.clear_buffers_before_each_transaction = True

    @retry(wait_fixed=200, stop_max_attempt_number=5)
    def retriable_read_register(
        self, registeraddress, number_of_decimals, functioncode
    ):
        return self.read_register(
            registeraddress, number_of_decimals, functioncode, False
        )

    @retry(wait_fixed=200, stop_max_attempt_number=5)
    def retriable_read_bit(self, registeraddress, functioncode):
        return self.read_bit(registeraddress, functioncode)

    def get_solar_voltage(self):
        """PV array input in volts"""
        return self.retriable_read_register(0x3100, 2, 4)

    def get_solar_current(self):
        """PV array input in amps"""
        return self.retriable_read_register(0x3101, 2, 4)

    def get_solar_power(self):
        """PV array input in watts"""
        return self.get_solar_voltage() * self.get_solar_current()

    def get_solar_power_l(self):
        """PV array input power L"""
        return self.retriable_read_register(0x3102, 2, 4)

    def get_solar_power_h(self):
        """PV array input power H"""
        return self.retriable_read_register(0x3103, 2, 4)

    def get_load_voltage(self):
        """Load output in volts"""
        return self.retriable_read_register(0x310C, 2, 4)

    def get_load_current(self):
        """Load output in amps"""
        return self.retriable_read_register(0x310D, 2, 4)

    def get_load_power(self):
        """Load output in watts"""
        return self.get_load_voltage() * self.get_load_current()

    def get_load_power_l(self):
        """Load power L"""
        return self.retriable_read_register(0x310E, 2, 4)

    def get_load_power_h(self):
        """Load power H"""
        return self.retriable_read_register(0x310F, 2, 4)

    def get_battery_current_l(self):
        """Battery current L"""
        return self.retriable_read_register(0x331B, 2, 4)

    def get_battery_current_h(self):
        """Battery current H"""
        return self.retriable_read_register(0x331C, 2, 4)

    def get_battery_voltage(self):
        """Battery voltage"""
        return self.retriable_read_register(0x331A, 2, 4)

    def get_battery_state_of_charge(self):
        """Battery state of charge"""
        return self.retriable_read_register(0x311A, 0, 4)

    def get_battery_temperature(self):
        """battery temperature"""
        return self.retriable_read_register(0x3110, 2, 4)

    def get_remote_battery_temperature(self):
        """The battery temperature measured by remote temperature sensor"""
        return self.retriable_read_register(0x311B, 2, 4)

    def get_controller_temperature(self):
        """Temperature inside equipment"""
        return self.retriable_read_register(0x3111, 2, 4)

    def get_battery_status(self):
        """Battery status"""
        register_value = self.retriable_read_register(0x3200, 0, 4)

        # D7-4
        temperature_warning_status = {
            0: "NORMAL",
            1: "OVER_TEMP",  # Higher than warning settings
            2: "LOW_TEMP",  # Lower than warning settings
        }[extract_bits(register_value, 4, 0b111)]

        # D3-0
        battery_status = {
            0: "NORMAL",
            1: "OVER_VOLTAGE",
            2: "UNDER_VOLTAGE",
            3: "OVER_DISCHARGE",
            4: "FAULT",
        }[extract_bits(register_value, 0, 0b111)]

        return {
            "wrong_identifaction_for_rated_voltage": bool(
                extract_bits(register_value, 15, 0b1)
            ),
            "battery_inner_resistence_abnormal": bool(
                extract_bits(register_value, 8, 0b1)
            ),
            "temperature_warning_status": temperature_warning_status,
            "battery_status": battery_status,
        }

    def get_charging_equipment_status(self):
        """Charging equipment status"""
        register_value = self.retriable_read_register(0x3201, 0, 4)

        # D15-14
        input_voltage_status = {
            0: "NORMAL",
            1: "NO_INPUT_POWER",
            2: "HIGHER_INPUT",
            3: "INPUT_VOLTAGE_ERROR",
        }[extract_bits(register_value, 14, 0b11)]

        # D3-2
        charging_status = {
            0: "NO_CHARGING",
            1: "FLOAT",
            2: "BOOST",
            3: "EQUALIZATION",
        }[extract_bits(register_value, 2, 0b11)]

        return {
            "input_voltage_status": input_voltage_status,
            "charging_mosfet_is_short_circuit": bool(
                extract_bits(register_value, 13, 0b1)
            ),
            "charging_or_anti_reverse_mosfet_is_open_circuit": bool(
                extract_bits(register_value, 12, 0b1)
            ),
            "anti_reverse_mosfet_is_short_circuit": bool(
                extract_bits(register_value, 11, 0b1)
            ),
            "input_over_current": bool(extract_bits(register_value, 10, 0b1)),
            "load_over_current": bool(extract_bits(register_value, 9, 0b1)),
            "load_short_circuit": bool(extract_bits(register_value, 8, 0b1)),
            "load_mosfet_short_circuit": bool(extract_bits(register_value, 7, 0b1)),
            "disequilibrium_in_three_circuits": bool(
                extract_bits(register_value, 6, 0b1)
            ),
            "pv_input_short_circuit": bool(extract_bits(register_value, 4, 0b1)),
            "charging_status": charging_status,
            "fault": bool(
                extract_bits(register_value, 1, 0b1)
            ),  # this does not seem to be functioning correctly. Fault status is returned when no fault.
            "running": bool(extract_bits(register_value, 0, 0b1)),
        }

    def get_discharging_equipment_status(self):
        """Charging equipment status"""
        register_value = self.retriable_read_register(0x3202, 0, 4)

        # D15-14
        input_voltage_status = {
            0: "NORMAL",
            1: "LOW",
            2: "HIGH",
            3: "NO_ACCESS",
        }[extract_bits(register_value, 14, 0b11)]

        # D13-12
        output_power_load = {
            0: "LIGHT",
            1: "MODERATE",
            2: "RATED",
            3: "OVERLOAD",
        }[extract_bits(register_value, 12, 0b11)]

        return {
            "input_voltage_status": input_voltage_status,
            "output_power_load": output_power_load,
            "short_circuit": bool(extract_bits(register_value, 11, 0b1)),
            "unable_to_discharge": bool(extract_bits(register_value, 10, 0b1)),
            "unable_to_stop_discharging": bool(extract_bits(register_value, 9, 0b1)),
            "output_voltage_abnormal": bool(extract_bits(register_value, 8, 0b1)),
            "input_over_voltage": bool(extract_bits(register_value, 7, 0b1)),
            "short_circuit_in_high_voltage_side": bool(
                extract_bits(register_value, 6, 0b1)
            ),
            "boost_over_voltage": bool(extract_bits(register_value, 5, 0b1)),
            "output_over_voltage": bool(extract_bits(register_value, 4, 0b1)),
            "output_over_voltage": bool(extract_bits(register_value, 4, 0b1)),
            "fault": bool(extract_bits(register_value, 1, 0b1)),
            "running": bool(extract_bits(register_value, 0, 0b1)),
        }

    def is_day(self):
        """Is day time"""
        return not self.is_night()

    def is_night(self):
        """Is night time"""
        return True if self.retriable_read_bit(0x200C, 2) == 1 else False

    def is_device_over_temperature(self):
        """Over temperature inside the device"""
        return True if self.retriable_read_bit(0x2000, 2) == 1 else False

    def get_maximum_battery_voltage_today(self):
        """Maximum battery voltage today"""
        return self.retriable_read_register(0x3302, 2, 4)

    def get_minimum_battery_voltage_today(self):
        """Minimum battery voltage today"""
        return self.retriable_read_register(0x3303, 2, 4)

    def get_rated_charging_current(self):
        """Rated charging current"""
        return self.retriable_read_register(0x3005, 2, 4)

    def get_rated_load_current(self):
        """Rated load current"""
        return self.retriable_read_register(0x300E, 2, 4)

    def get_battery_real_rated_voltage(self):
        """Battery real rated voltage"""
        return self.retriable_read_register(0x311D, 2, 4)

    def get_battery_type(self):
        """Battery type"""
        return {0: "USER_DEFINED", 1: "SEALED", 2: "GEL", 3: "FLOODED"}[
            self.retriable_read_register(0x9000, 2, 3)
        ]

    def get_battery_capacity(self):
        """Battery capacity in amp hours"""
        return self.retriable_read_register(0x9001, 0, 3)

    def get_temperature_compensation_coefficient(self):
        """Temperature compensation coefficient"""
        return self.retriable_read_register(0x9002, 0, 3)

    def get_over_voltage_disconnect_voltage(self):
        """Over voltage disconnect voltage"""
        return self.retriable_read_register(0x9003, 2, 3)

    def get_charging_limit_voltage(self):
        """Charging limit voltage"""
        return self.retriable_read_register(0x9004, 2, 3)

    def get_over_voltage_reconnect_voltage(self):
        """Over voltage reconnect voltage"""
        return self.retriable_read_register(0x9005, 2, 3)

    def get_equalize_charging_voltage(self):
        """Equalize charging voltage"""
        return self.retriable_read_register(0x9006, 2, 3)

    def get_boost_charging_voltage(self):
        """Boost charging voltage"""
        return self.retriable_read_register(0x9007, 2, 3)

    def get_float_charging_voltage(self):
        """Float charging voltage"""
        return self.retriable_read_register(0x9008, 2, 3)

    def get_boost_reconnect_charging_voltage(self):
        """Boost reconnect charging voltage"""
        return self.retriable_read_register(0x9009, 2, 3)

    def get_low_voltage_reconnect_voltage(self):
        """Low voltage reconnect voltage"""
        return self.retriable_read_register(0x900A, 2, 3)

    def get_under_voltage_recover_voltage(self):
        """Under voltage warning recover voltage"""
        return self.retriable_read_register(0x900B, 2, 3)

    def get_under_voltage_warning_voltage(self):
        """Under voltage warning voltage"""
        return self.retriable_read_register(0x900C, 2, 3)

    def get_low_voltage_disconnect_voltage(self):
        """Low voltage disconnect voltage"""
        return self.retriable_read_register(0x900D, 2, 3)

    def get_discharging_limit_voltage(self):
        """Discharging limit voltage"""
        return self.retriable_read_register(0x900E, 2, 3)

    def get_battery_rated_voltage(self):
        """Battery rated voltage"""
        return {
            0: "AUTO",
            1: "12V",
            2: "24V",
            3: "36V",
            4: "48V",
            5: "60V",
            6: "110V",
            7: "120V",
            8: "220V",
            9: "240V",
        }[self.retriable_read_register(0x9067, 0, 3)]

    def get_default_load_on_off_in_manual_mode(self):
        """Default load On/Off in manual mode"""
        return {0: "OFF", 1: "ON"}[self.retriable_read_register(0x906A, 0, 3)]

    def get_equalize_duration(self):
        """Equalize duration"""
        return self.retriable_read_register(0x906B, 0, 3)

    def get_boost_duration(self):
        """Equalize duration"""
        return self.retriable_read_register(0x906C, 0, 3)

    def get_battery_discharge(self):
        """Battery discharge"""
        return self.retriable_read_register(0x906D, 0, 3)

    def get_battery_charge(self):
        """Battery charge"""
        return self.retriable_read_register(0x906E, 0, 3)

    def get_charging_mode(self):
        """Charging mode"""
        return {0: "VOLTAGE_COMPENSATION", 1: "SOC"}[
            self.retriable_read_register(0x9070, 0, 3)
        ]
