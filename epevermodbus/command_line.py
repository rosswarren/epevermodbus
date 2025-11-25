import argparse
import datetime
import json

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

    parser.add_argument("--json", help="Make a json output", action="store_true")
    parser.add_argument("--set-time", help="Set the RTC of the MPPT and exit", action="store_true")
    parser.add_argument(
        "--set-battery-type",
        help="Set the battery type (USER_DEFINED, SEALED, GEL, FLOODED, LIFEPO4, LI_NICOMN_02",
        type=str
    )
    parser.add_argument("--set-battery-capacity", help="Set the battery capacity in Ah an exit", type=int)
    parser.add_argument(
        "--set-battery-temp-comp-coeff",
        help="Sets the batteries temperature compensation coefficient. Coefficient is in mV/°C/Cell without the sign",
        type=float,
    )
    parser.add_argument(
        "--set-over-voltage-disconnect-voltage",
        help="Set the over-voltage disconnect voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-over-voltage-reconnect-voltage",
        help="Set the over-voltage reconnect voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-charging-limit-voltage",
        help="Set the charging voltage limit and exit",
        type=float
    )
    parser.add_argument(
        "--set-discharging-limit-voltage",
        help="Set the discharging limit voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-boost-charging-voltage",
        help="Set the boost charging voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-boost-reconnect-charging-voltage",
        help="Set the boost reconnect charging voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-equalize-charging-voltage",
        help="Set the equalize charging voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-float-charging-voltage",
        help="Set the float charging voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-low-voltage-disconnect-voltage",
        help="Set the low-voltage disconnect voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-low-voltage-reconnect-voltage",
        help="Set the low voltage reconnect voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-under-voltage-warning-voltage",
        help="Set the under-voltage warning voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-under-voltage-recover-voltage",
        help="Set the under-voltage recover voltage and exit",
        type=float
    )
    parser.add_argument(
        "--set-boost-duration",
        help="Set the boost voltage duration and exit",
        type=float
    )
    parser.add_argument(
        "--set-equalize-duration",
        help="Set the equalize voltage duration and exit",
        type=float
    )
    parser.add_argument(
        "--set-low-temp-charging-limit",
        help="Set the low temperature limit (-40C to 10C) for charging and exit",
        type=float
    )
    parser.add_argument(
        "--set-low-temp-discharging-limit",
        help="Set the low temperature limit (-40C to 10C) for discharging and exit",
        type=float
    )
    parser.add_argument(
        "--disable-low-temp-charging-limit",
        help="Disable the low temperature limit for charging and exit",
        action="store_true"
    )
    parser.add_argument(
        "--disable-low-temp-discharging-limit",
        help="Disable the low temperature limit for discharging and exit",
        action="store_true"
    )
    args = parser.parse_args()

    controller = EpeverChargeController(args.portname, args.slaveaddress, args.baudrate)

    if args.set_time:
        print(f"Old RTC value: {controller.get_rtc()}")
        controller.set_rtc(datetime.datetime.now())
        print(f"New RTC value: {controller.get_rtc()}")

    if args.set_battery_type:
        print(f"Old type: {controller.get_battery_type()}")
        controller.set_battery_type(args.set_battery_type)
        print(f"New type: {controller.get_battery_type()}")

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

    if args.set_over_voltage_disconnect_voltage:
        print(f"Old over-voltage disconnect voltage: {controller.get_over_voltage_disconnect_voltage()}V")
        controller.set_battery_voltage_control_registers(
                over_voltage_disconnect_voltage=args.set_over_voltage_disconnect_voltage
        )
        print(f"New over-voltage disconnect voltage: {controller.get_over_voltage_disconnect_voltage()}V")

    if args.set_over_voltage_reconnect_voltage:
        print(f"Old over-voltage reconnect voltage: {controller.get_over_voltage_reconnect_voltage()}V")
        controller.set_battery_voltage_control_registers(
            over_voltage_reconnect_voltage=args.set_over_voltage_reconnect_voltage
        )
        print(f"New over-voltage reconnect voltage: {controller.get_over_voltage_reconnect_voltage()}V")

    if args.set_charging_limit_voltage:
        print(f"Old charging limit voltage: {controller.get_charging_limit_voltage()}V")
        controller.set_battery_voltage_control_registers(
            charging_limit_voltage=args.set_charging_limit_voltage
        )
        print(f"New charging limit voltage: {controller.get_charging_limit_voltage()}V")

    if args.set_discharging_limit_voltage:
        print(f"Old discharging limit voltage: {controller.get_discharging_limit_voltage()}V")
        controller.set_battery_voltage_control_registers(
            discharging_limit_voltage=args.set_discharging_limit_voltage
        )
        print(f"New discharging limit voltage: {controller.get_discharging_limit_voltage()}V")

    if args.set_boost_charging_voltage:
        print(f"Old boost charging voltage: {controller.get_boost_charging_voltage()}V")
        controller.set_battery_voltage_control_registers(boost_charging_voltage=args.set_boost_charging_voltage)
        print(f"New boost charging voltage: {controller.get_boost_charging_voltage()}V")

    if args.set_boost_reconnect_charging_voltage:
        print(f"Old boost reconnect charging voltage: {controller.get_boost_reconnect_charging_voltage()}V")
        controller.set_battery_voltage_control_registers(
            boost_reconnect_charging_voltage=args.set_boost_reconnect_charging_voltage
        )
        print(f"New boost reconnect charging voltage: {controller.get_boost_reconnect_charging_voltage()}V")

    if args.set_equalize_charging_voltage:
        print(f"Old equalize charging voltage: {controller.get_equalize_charging_voltage()}V")
        controller.set_battery_voltage_control_registers(
            equalize_charging_voltage=args.set_equalize_charging_voltage
        )
        print(f"New equalize charging voltage: {controller.get_equalize_charging_voltage()}V")

    if args.set_float_charging_voltage:
        print(f"Old float charging voltage: {controller.get_float_charging_voltage()}V")
        controller.set_battery_voltage_control_registers(float_charging_voltage=args.set_float_charging_voltage)
        print(f"New float charging voltage: {controller.get_float_charging_voltage()}V")

    if args.set_low_voltage_disconnect_voltage:
        print(f"Old low-voltage disconnect voltage: {controller.get_low_voltage_disconnect_voltage()}V")
        controller.set_battery_voltage_control_registers(
            low_voltage_disconnect_voltage=args.set_low_voltage_disconnect_voltage
        )
        print(f"New low-voltage disconnect voltage: {controller.get_low_voltage_disconnect_voltage()}V")

    if args.set_low_voltage_reconnect_voltage:
        print(f"Old low-voltage reconnect voltage: {controller.get_low_voltage_reconnect_voltage()}V")
        controller.set_battery_voltage_control_registers(
            low_voltage_reconnect_voltage=args.set_low_voltage_reconnect_voltage
        )
        print(f"New low-voltage reconnect voltage: {controller.get_low_voltage_reconnect_voltage()}V")

    if args.set_under_voltage_warning_voltage:
        print(f"Old under-voltage warning voltage: {controller.get_under_voltage_warning_voltage()}V")
        controller.set_battery_voltage_control_registers(
            under_voltage_warning_voltage=args.set_under_voltage_warning_voltage
        )
        print(f"New under-voltage warning voltage: {controller.get_under_voltage_warning_voltage()}V")

    if args.set_under_voltage_recover_voltage:
        print(f"Old under-voltage recover voltage: {controller.get_under_voltage_recover_voltage()}V")
        controller.set_battery_voltage_control_registers(
            under_voltage_recover_voltage=args.set_under_voltage_recover_voltage
        )
        print(f"New under-voltage recover voltage: {controller.get_under_voltage_recover_voltage()}V")

    if args.set_boost_duration is not None:
        print(f"Old boost duration: {controller.get_boost_duration()} min")
        controller.set_boost_duration(args.set_boost_duration)
        print(f"New boost duration: {controller.get_boost_duration()} min")

    if args.set_equalize_duration is not None:
        print(f"Old equalize duration: {controller.get_equalize_duration()} min")
        controller.set_equalize_duration(args.set_equalize_duration)
        print(f"New equalize duration: {controller.get_equalize_duration()} min")

    if args.set_low_temp_charging_limit is not None:
        print(f"Old low temperature charging limit: {controller.get_low_temperature_charging_limit()}°C")
        controller.set_low_temperature_charging_limit(args.set_low_temp_charging_limit)
        controller.set_low_temperature_charging_limit_enabled(True)
        print(f"New low temperature charging limit: {controller.get_low_temperature_charging_limit()}°C")

    if args.set_low_temp_discharging_limit is not None:
        print(f"Old low temperature discharging limit: {controller.get_low_temperature_discharging_limit()}°C")
        controller.set_low_temperature_discharging_limit(args.set_low_temp_discharging_limit)
        controller.set_low_temperature_discharging_limit_enabled(True)
        print(f"New low temperature discharging limit: {controller.get_low_temperature_discharging_limit()}°C")

    if args.disable_low_temp_charging_limit:
        print(f"Old low temperature charging limit enabled: {controller.get_low_temperature_charging_limit_enabled()}")
        controller.set_low_temperature_charging_limit_enabled(False)
        print(f"New low temperature charging limit enabled: {controller.get_low_temperature_charging_limit_enabled()}")

    if args.disable_low_temp_discharging_limit:
        print(f"Old low temperature discharging limit enabled: {controller.get_low_temperature_discharging_limit_enabled()}")
        controller.set_low_temperature_discharging_limit_enabled(False)
        print(f"New low temperature charging limit enabled: {controller.get_low_temperature_charging_limit_enabled()}")

    if any([
        args.set_time,
        args.set_battery_type,
        args.set_battery_capacity,
        args.set_battery_temp_comp_coeff,
        args.set_over_voltage_disconnect_voltage,
        args.set_over_voltage_reconnect_voltage,
        args.set_charging_limit_voltage,
        args.set_discharging_limit_voltage,
        args.set_boost_charging_voltage,
        args.set_boost_reconnect_charging_voltage,
        args.set_equalize_charging_voltage,
        args.set_float_charging_voltage,
        args.set_low_voltage_disconnect_voltage,
        args.set_low_voltage_reconnect_voltage,
        args.set_under_voltage_warning_voltage,
        args.set_under_voltage_recover_voltage,
        args.set_boost_duration is not None,
        args.set_equalize_duration is not None,
        args.set_low_temp_charging_limit is not None,
        args.set_low_temp_discharging_limit is not None,
        args.disable_low_temp_charging_limit,
        args.disable_low_temp_discharging_limit,
    ]):
        exit(0)

    if args.json:
        output = {}
        output["solar_voltage"] = controller.get_solar_voltage()
        output["solar_current"] = controller.get_solar_current()
        output["solar_power"] = controller.get_solar_power()
        output["load_voltage"] = controller.get_load_voltage()
        output["load_current"] = controller.get_load_current()
        output["load_power"] = controller.get_load_power()
        output["battery_voltage"] = controller.get_battery_voltage()
        output["battery_current"] = controller.get_battery_current()
        output["battery_power"] = controller.get_battery_power()
        output["battery_state_of_charge"] = controller.get_battery_state_of_charge()
        output["battery_temperature"] = controller.get_battery_temperature()
        output["remote_battery_temperature"] = controller.get_remote_battery_temperature()
        output["controller_temperature"] = controller.get_controller_temperature()
        output["battery_status"] = controller.get_battery_status()
        output["charging_equipment_status"] = controller.get_charging_equipment_status()
        output["discharging_equipment_status"] = controller.get_discharging_equipment_status()
        output["day_time"] = controller.is_day()
        output["night_time"] = controller.is_night()
        output["maximum_battery_voltage_today"] = controller.get_maximum_battery_voltage_today()
        output["minimum_battery_voltage_today"] = controller.get_minimum_battery_voltage_today()
        output["maximum_pv_voltage_today"] = controller.get_maximum_pv_voltage_today()
        output["minimum_pv_voltage_today"] = controller.get_minimum_pv_voltage_today()
        output["device_over_temperature"] = controller.is_device_over_temperature()
        output["consumed_energy_today"] = controller.get_consumed_energy_today()
        output["consumed_energy_this_month"] = controller.get_consumed_energy_this_month()
        output["consumed_energy_this_year"] = controller.get_consumed_energy_this_year()
        output["total_consumed_energy"] = controller.get_total_consumed_energy()
        output["generated_energy_today"] = controller.get_generated_energy_today()
        output["generated_energy_this_month"] = controller.get_generated_energy_this_month()
        output["generated_energy_this_year"] = controller.get_generated_energy_this_year()
        output["total_generated_energy"] = controller.get_total_generated_energy()
        output["current_device_time"] = controller.get_rtc().isoformat()
        output["rated_charging_current"] = controller.get_rated_charging_current()
        output["rated_load_current"] = controller.get_rated_load_current()
        output["battery_real_rated_voltage"] = controller.get_battery_real_rated_voltage()
        output["battery_type"] = controller.get_battery_type()
        output["battery_capacity"] = controller.get_battery_capacity()
        output["temperature_compensation_coefficient"] = controller.get_temperature_compensation_coefficient()
        output["over_voltage_disconnect_voltage"] = controller.get_over_voltage_disconnect_voltage()
        output["charging_limit_voltage"] = controller.get_charging_limit_voltage()
        output["over_voltage_reconnect_voltage"] = controller.get_over_voltage_reconnect_voltage()
        output["equalize_charging_voltage"] = controller.get_equalize_charging_voltage()
        output["boost_charging_voltage"] = controller.get_boost_charging_voltage()
        output["float_charging_voltage"] = controller.get_float_charging_voltage()
        output["boost_reconnect_charging_voltage"] = controller.get_boost_reconnect_charging_voltage()
        output["low_voltage_reconnect_voltage"] = controller.get_low_voltage_reconnect_voltage()
        output["under_voltage_recover_voltage"] = controller.get_under_voltage_recover_voltage()
        output["under_voltage_warning_voltage"] = controller.get_under_voltage_warning_voltage()
        output["low_voltage_disconnect_voltage"] = controller.get_low_voltage_disconnect_voltage()
        output["discharging_limit_voltage"] = controller.get_discharging_limit_voltage()
        output["battery_rated_voltage"] = controller.get_battery_rated_voltage()
        output["default_load_on_off_in_manual_mode"] = controller.get_default_load_on_off_in_manual_mode()
        output["equalize_duration"] = controller.get_equalize_duration()
        output["boost_duration"] = controller.get_boost_duration()
        output["battery_discharge"] = controller.get_battery_discharge()
        output["battery_charge"] = controller.get_battery_charge()
        output["charging_mode"] = controller.get_charging_mode()
        output["low_temperature_charging_limit"] = controller.get_low_temperature_charging_limit()
        output["low_temperature_discharging_limit"] = controller.get_low_temperature_discharging_limit()
        output["low_temperature_charging_limit_enabled"] = controller.get_low_temperature_charging_limit_enabled()
        output["low_temperature_discharging_limit_enabled"] = controller.get_low_temperature_discharging_limit_enabled()
        print(json.dumps(output))
    else:
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
        print(f"Low temperature charging limit: {controller.get_low_temperature_charging_limit()}")
        print(f"Low temperature discharging limit: {controller.get_low_temperature_discharging_limit()}")
        print(f"Low temperature charging limit enabled: {controller.get_low_temperature_charging_limit_enabled()}")
        print(f"Low temperature discharging limit enabled: {controller.get_low_temperature_discharging_limit_enabled()}")


if __name__ == "__main__":
    main()
