import minimalmodbus
import serial
from retrying import retry

class EpeverChargeController( minimalmodbus.Instrument ):
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
    def retriable_read_register(self, registeraddress, number_of_decimals, functioncode):
        return self.read_register(registeraddress, number_of_decimals, functioncode, False)

    def get_solar_voltage(self):
        """PV array input in volts"""
        return self.retriable_read_register(0x3100, 2, 4)

    def get_solar_current(self):
        """PV array input in amps"""
        return self.retriable_read_register(0x3101, 2, 4)

    def get_solar_power(self):
        """PV array input in watts"""
        return self.get_solar_voltage() * self.get_solar_current()

    def get_load_voltage(self):
        """Load output in volts"""
        return self.retriable_read_register(0x310C, 2, 4)

    def get_load_current(self):
        """Load output in amps"""
        return self.retriable_read_register(0x310D, 2, 4)

    def get_load_power(self):
        """Load output in watts"""
        return self.get_load_voltage() * self.get_load_current()

    def get_battery_capacity(self):
        """Battery capacity in amp hours"""
        return self.retriable_read_register(0x9001, 0, 3)

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


if __name__ == "__main__":
    controller = EpeverChargeController("/dev/ttyUSB1", 1)
    print('Solar voltage: ', controller.get_solar_voltage())
    print('Solar current: ', controller.get_solar_current())
    print('Solar power: ', controller.get_solar_current())
    print('Load voltage: ', controller.get_load_voltage())
    print('Load current: ', controller.get_load_current())
    print('Load power: ', controller.get_load_power())
    print('Battery capacity: ', controller.get_battery_capacity())
    print('Battery voltage: ', controller.get_battery_voltage())
    print('Battery state of charge: ', controller.get_battery_state_of_charge())
    print('Battery temperature: ', controller.get_battery_temperature())
    print('Remote battery temperature: ', controller.get_remote_battery_temperature())
    print('Controller temperature: ', controller.get_controller_temperature())
    print('Battery status: ', controller.get_battery_status())
    print('Charging equipment status: ', controller.get_charging_equipment_status())
    print('Discharging equipment status: ', controller.get_discharging_equipment_status())

