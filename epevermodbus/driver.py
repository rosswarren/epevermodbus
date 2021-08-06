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
        return self.retriable_read_register(0x3100, 2, 4)

    def get_solar_current(self):
        return self.retriable_read_register(0x3101, 2, 4)

if __name__ == "__main__":
    controller = EpeverChargeController("/dev/ttyUSB0", 1)
    print('Solar voltage: ', controller.get_solar_voltage())
    print('Solar current: ', controller.get_solar_current())