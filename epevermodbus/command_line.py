import argparse
import datetime

from epevermodbus.driver import EpeverChargeController


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--portname", help="Port name for example /dev/ttyUSB0", default="/dev/ttyUSB0"
    )
    parser.add_argument(
        "--slaveaddress", help="Slave address 1-247", default=1, type=int
    )

    parser.add_argument(
        "--baudrate", help="Baudrate to communicate with controller (default is 115200)", default=115200, type=int
    )

    parser.add_argument("--set-time", help="Set the RTC of the MPPT and exit", action="store_true")
    parser.add_argument("--set-battery-capacity", help="Set the battery capacity in Ah an exit", type=int)
    parser.add_argument(
        "--set-battery-temp-comp-coeff",
        help="Sets the batteries temperature compensation coefficient. Coefficient is in mV/°C/Cell without the sign",
        type=float,
    )
    args = parser.parse_args()

    controller = EpeverChargeController(args.portname, args.slaveaddress, args.baudrate)

    if args.set_time:
        print(f"Old RTC value: {controller.get_rtc()}")
        controller.set_rtc(datetime.datetime.now())
        print(f"New RTC value: {controller.get_rtc()}")

    if args.set_battery_capacity:
        print(f"Old capacity: {controller.get_battery_capacity()}AH")
        controller.set_battery_capacity(args.set_battery_capacity)
        print(f"New capacity: {controller.get_battery_capacity()}AH")

    if args.set_battery_temp_comp_coeff:
        print(
            "Old Temperature compensation coefficient: "
            f"{controller.get_temperature_compensation_coefficient()}mV/°C/Cell"
        )
        controller.set_temperature_compensation_coefficient(args.set_battery_temp_comp_coeff)
        print(
            "New Temperature compensation coefficient: "
            f"{controller.get_temperature_compensation_coefficient()}mV/°C/Cell"
        )

    if any([
        args.set_time,
        args.set_battery_capacity,
        args.set_battery_temp_comp_coeff,
    ]):
        exit(0)

    print("Real Time Data")
    print(f"Solar voltage: {controller.get_solar_voltage()}V")
    print(f"Solar current: {controller.get_solar_current()}A")
    print(f"Solar power: {controller.get_solar_power()}W")
    print(f"Load voltage: {controller.get_load_voltage()}V")
    print(f"Load current: {controller.get_load_current()}A")
    print(f"Load power: {controller.get_load_power()}W")
    print(f"Battery voltage: {controller.get_battery_voltage()}V")
    print(f"Battery current: {controller.get_battery_current()}A")
    print(f"Battery power: {controller.get_battery_power()}W")
    print(
        f"Battery state of charge: {controller.get_battery_state_of_charge()}%")
    print(f"Battery temperature: {controller.get_battery_temperature()}°C")
    print(
        f"Remote battery temperature: {controller.get_remote_battery_temperature()}°C"
    )
    print(
        f"Controller temperature: {controller.get_controller_temperature()}°C")
    print(f"Battery status: {controller.get_battery_status()}")
    print(
        f"Charging equipment status: {controller.get_charging_equipment_status()}")
    print(
        f"Discharging equipment status: {controller.get_discharging_equipment_status()}"
    )
    print(f"Day time: {controller.is_day()}")
    print(f"Night time: {controller.is_night()}")
    print(
        f"Maximum battery voltage today: {controller.get_maximum_battery_voltage_today()}V"
    )
    print(
        f"Minimum battery voltage today: {controller.get_minimum_battery_voltage_today()}V"
    )
    print(f"Maximum PV voltage today: {controller.get_maximum_pv_voltage_today()}V")
    print(f"Minimum PV voltage today: {controller.get_minimum_pv_voltage_today()}V")
    print(
        f"Device over temperature: {controller.is_device_over_temperature()}")
    print(f"Consumed energy today: {controller.get_consumed_energy_today()}kWh")
    print(f"Consumed energy this month: {controller.get_consumed_energy_this_month()}kWh")
    print(f"Consumed energy this year: {controller.get_consumed_energy_this_year()}kWh")
    print(f"Total consumed energy: {controller.get_total_consumed_energy()}kWh")
    print(f"Generated energy today: {controller.get_generated_energy_today()}kWh")
    print(f"Generated energy this month: {controller.get_generated_energy_this_month()}kWh")
    print(f"Generated energy this year: {controller.get_generated_energy_this_year()}kWh")
    print(f"Total generated energy: {controller.get_total_generated_energy()}kWh")
    print(f"Current device time: {controller.get_rtc()}")
    print("\n")

    print("Battery Parameters:")
    print(
        f"Rated charging current: {controller.get_rated_charging_current()}A")
    print(f"Rated load current: {controller.get_rated_load_current()}A")
    print(
        f"Battery real rated voltage: {controller.get_battery_real_rated_voltage()}V")
    print(f"Battery type: {controller.get_battery_type()}")
    print(f"Battery capacity: {controller.get_battery_capacity()}AH")
    print(
        "Temperature compensation coefficient: "
        f"{controller.get_temperature_compensation_coefficient()}mV/°C/Cell"
    )
    print("Battery Voltage Control Register Names:",
          controller.battery_voltage_control_register_names)
    print(
        f"Battery voltage control registers: {controller.get_battery_voltage_control_registers()}"
    )
    # controller.set_battery_voltage_control_registers(over_voltage_disconnect_voltage=14.7)
    print(
        f"Over voltage disconnect voltage: {controller.get_over_voltage_disconnect_voltage()}V"
    )
    print(
        f"Charging limit voltage: {controller.get_charging_limit_voltage()}V")
    print(
        f"Over voltage reconnect voltage: {controller.get_over_voltage_reconnect_voltage()}V"
    )
    print(
        f"Equalize charging voltage: {controller.get_equalize_charging_voltage()}V")
    print(
        f"Boost charging voltage: {controller.get_boost_charging_voltage()}V")
    print(
        f"Float charging voltage: {controller.get_float_charging_voltage()}V")
    print(
        f"Boost reconnect charging voltage: {controller.get_boost_reconnect_charging_voltage()}V"
    ),
    print(
        f"Low voltage reconnect voltage: {controller.get_low_voltage_reconnect_voltage()}V"
    )
    print(
        f"Under voltage recover voltage: {controller.get_under_voltage_recover_voltage()}V"
    )
    print(
        f"Under voltage warning voltage: {controller.get_under_voltage_warning_voltage()}V"
    )
    print(
        f"Low voltage disconnect voltage: {controller.get_low_voltage_disconnect_voltage()}V"
    )
    print(
        f"Discharging limit voltage: {controller.get_discharging_limit_voltage()}V")
    print(f"Battery rated voltage: {controller.get_battery_rated_voltage()}")
    print(
        "Default load on/off in manual mode:",
        controller.get_default_load_on_off_in_manual_mode(),
    )
    print(f"Equalize duration: {controller.get_equalize_duration()} min")
    print(f"Boost duration: {controller.get_boost_duration()} min")
    print(f"Battery discharge: {controller.get_battery_discharge()}%")
    print(f"Battery charge: {controller.get_battery_charge()}%")
    print(f"Charging mode: {controller.get_charging_mode()}")


if __name__ == "__main__":
    main()
