import minimalmodbus
import serial
from retrying import retry


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

    def get_battery_capacity(self):
        """Battery capacity in amp hours"""
        return self.retriable_read_register(0x9001, 0, 3)

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
        return self.retriable_read_register(0x311A, 2, 4)

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
        return self.retriable_read_register(0x3200, 2, 4)

    def get_charging_equipment_status(self):
        """Charging equipment status"""
        return self.retriable_read_register(0x3201, 2, 4)

    def get_discharging_equipment_status(self):
        """Charging equipment status"""
        return self.retriable_read_register(0x3202, 2, 4)

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
