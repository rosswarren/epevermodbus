from epevermodbus.driver import EpeverChargeController
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--portname", help="Port name for example /dev/ttyUSB0", default="/dev/ttyUSB0"
    )
    parser.add_argument(
        "--slaveaddress", help="Slave address 1-247", default=1, type=int
    )
    args = parser.parse_args()

    controller = EpeverChargeController(args.portname, args.slaveaddress)

    print("Real Time Data")
    print("Solar voltage:", controller.get_solar_voltage())
    print("Solar current:", controller.get_solar_current())
    print("Solar power:", controller.get_solar_current())
    print("Solar power L:", controller.get_solar_power_l())
    print("Solar power H:", controller.get_solar_power_h())
    print("Load voltage:", controller.get_load_voltage())
    print("Load current:", controller.get_load_current())
    print("Load power:", controller.get_load_power())
    print("Load power L:", controller.get_load_power_l())
    print("Load power H:", controller.get_load_power_h())
    print("Battery capacity:", controller.get_battery_capacity())
    print("Battery current L:", controller.get_battery_current_l())
    print("Battery current H:", controller.get_battery_current_h())
    print("Battery voltage:", controller.get_battery_voltage())
    print("Battery state of charge:", controller.get_battery_state_of_charge())
    print("Battery temperature:", controller.get_battery_temperature())
    print("Remote battery temperature:", controller.get_remote_battery_temperature())
    print("Controller temperature:", controller.get_controller_temperature())
    print("Battery status:", controller.get_battery_status())
    print("Charging equipment status:", controller.get_charging_equipment_status())
    print(
        "Discharging equipment status:", controller.get_discharging_equipment_status()
    )
    print("Day time:", controller.is_day())
    print("Night time:", controller.is_night())
    print(
        "Maximum battery voltage today:", controller.get_maximum_battery_voltage_today()
    )
    print(
        "Minimum battery voltage today:", controller.get_minimum_battery_voltage_today()
    )
    print("Device over temperature:", controller.is_device_over_temperature())
    print("\n")
    print("Battery Parameters:")
    print("Rated charging current:", controller.get_rated_charging_current())
    print("Rated load current:", controller.get_rated_load_current())
    print("Battery real rated voltage:", controller.get_battery_real_rated_voltage())


if __name__ == "__main__":
    main()
