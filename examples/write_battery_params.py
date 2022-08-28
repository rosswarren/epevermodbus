from minimalmodbus import SlaveReportedException

from epevermodbus.driver import EpeverChargeController


def main():
    portname = "/dev/ttyUSB0"
    slaveaddress = 1
    controller = EpeverChargeController(portname, slaveaddress)

    # Meta Example 1: Show all register names
    print("Battery Voltage Control Register Names")
    print(controller.battery_voltage_control_register_names)

    # Get Example 1: Show all registers and their values:
    print("All registers and their values:")
    battery_voltage_control_registers = controller.get_battery_voltage_control_registers()

    for param_name, param_value in battery_voltage_control_registers.items():
        print(f"{param_name}: {param_value}")

    # Set Example 1: Set all registers at once
    print("Set all registers at once...")

    # These values are an example and must be tuned to a particular battery type
    battery_voltage_control_registers = {
        'over_voltage_disconnect_voltage': 14.7,
        'charging_limit_voltage': 14.6,
        'over_voltage_reconnect_voltage': 14.6,
        'equalize_charging_voltage': 14.4,
        'boost_charging_voltage': 14.6,
        'float_charging_voltage': 13.6,
        'boost_reconnect_charging_voltage': 13.3,
        'low_voltage_reconnect_voltage': 11.5,
        'under_voltage_recover_voltage': 11.6,
        'under_voltage_warning_voltage': 11.5,
        'low_voltage_disconnect_voltage': 11.0,
        'discharging_limit_voltage': 10.5
    }
    controller.set_battery_voltage_control_registers_dict(
        battery_voltage_control_registers)

    # Set Example 2: Set a single register
    print("Set a single register...")
    controller.set_battery_voltage_control_registers(
        over_voltage_disconnect_voltage=14.7)

    # Set Example 3: Set a single register which throws an error
    print("Trying to set an illegal value...")
    try:
        controller.set_battery_voltage_control_registers(
            over_voltage_disconnect_voltage=543.21)

    except SlaveReportedException as err:
        print("The device reported an error:", err)


if __name__ == "__main__":
    main()
