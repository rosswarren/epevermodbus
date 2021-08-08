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

    print("Solar voltage: ", controller.get_solar_voltage())
    print("Solar current: ", controller.get_solar_current())
    print("Solar power: ", controller.get_solar_current())
    print("Load voltage: ", controller.get_load_voltage())
    print("Load current: ", controller.get_load_current())
    print("Load power: ", controller.get_load_power())
    print("Battery capacity: ", controller.get_battery_capacity())
    print("Battery voltage: ", controller.get_battery_voltage())
    print("Battery state of charge: ", controller.get_battery_state_of_charge())
    print("Battery temperature: ", controller.get_battery_temperature())
    print("Remote battery temperature: ", controller.get_remote_battery_temperature())
    print("Controller temperature: ", controller.get_controller_temperature())
    print("Battery status: ", controller.get_battery_status())
    print("Charging equipment status: ", controller.get_charging_equipment_status())
    print(
        "Discharging equipment status: ", controller.get_discharging_equipment_status()
    )
    print("Day or night", controller.get_day_night())


if __name__ == "__main__":
    main()
