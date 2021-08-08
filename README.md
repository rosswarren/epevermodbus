# epevermodbus

This package is intended to help you communicate with an EPever charge controller. It has been tested with an EPever Tracer AN but should work with other devices.

## Connecting to the charge controller

You have two options

* Official EPever cable
* Your own custom cable

## Installing the package

To install the package run

```sh
pip install epevermodbus
```

## Command line utility

To run the command line utility and see the debug output run the following on the command line:

```sh
epevermodbus --portname /dev/ttyUSB0 --slaveaddress 1
```

```sh
usage: epevermodbus [-h] [--portname PORTNAME] [--slaveaddress SLAVEADDRESS]

optional arguments:
  -h, --help            show this help message and exit
  --portname PORTNAME   Port name for example /dev/ttyUSB0
  --slaveaddress SLAVEADDRESS
                        Slave address 1-247
```

Example output

```sh
Real Time Data
Solar voltage: 0.0
Solar current: 0.0
Solar power: 0.0
Solar power L: 0.0
Solar power H: 0.0
Load voltage: 0.0
Load current: 0.0
Load power: 0.0
Load power L: 0.0
Load power H: 0.0
Battery capacity: 40
Battery current L: 0.0
Battery current H: 0.0
Battery voltage: 13.27
Battery state of charge: 0.87
Battery temperature: 17.08
Remote battery temperature: 0.0
Controller temperature: 16.42
Battery status: {'wrong_identifaction_for_rated_voltage': False, 'battery_inner_resistence_abnormal': False, 'temperature_warning_status': 'NORMAL', 'battery_status': 'NORMAL'}
Charging equipment status: {'input_voltage_status': 'NORMAL', 'charging_mosfet_is_short_circuit': False, 'charging_or_anti_reverse_mosfet_is_open_circuit': False, 'anti_reverse_mosfet_is_short_circuit': False, 'input_over_current': False, 'load_over_current': False, 'load_short_circuit': False, 'load_mosfet_short_circuit': False, 'disequilibrium_in_three_circuits': False, 'pv_input_short_circuit': False, 'charging_status': 'NO_CHARGING', 'fault': False, 'running': True}
Discharging equipment status: {'input_voltage_status': 'NORMAL', 'output_power_load': 'LIGHT', 'short_circuit': False, 'unable_to_discharge': False, 'unable_to_stop_discharging': False, 'output_voltage_abnormal': False, 'input_over_voltage': False, 'short_circuit_in_high_voltage_side': False, 'boost_over_voltage': False, 'output_over_voltage': False, 'fault': False, 'running': False}
Day time: False
Night time: True
Maximum battery voltage today: 14.74
Minimum battery voltage today: 13.27
Device over temperature: False


Battery Parameters:
Rated charging current: 20.0
Rated load current: 20.0
Battery real rated voltage: 12.0
```

## Python usage

To use the library within your Python code

```python
from epevermodbus.driver import EpeverChargeController


controller = EpeverChargeController("/dev/ttyUSB0", 1)

controller.get_solar_voltage()
```
