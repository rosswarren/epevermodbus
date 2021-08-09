# epevermodbus

This package is intended to help you communicate with an EPever charge controller. It has been tested with an EPever Tracer AN but should work with other devices.

![image](https://user-images.githubusercontent.com/613642/128763284-c5bbe67b-3905-479a-8a90-b1db16ff59fb.png)

## Connecting to the charge controller

You have two options

* Official EPever cable

![image](https://user-images.githubusercontent.com/613642/128763357-c88e8ef6-481c-470f-9ca3-40dd7cf85914.png)

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
Solar voltage: 0.02V
Solar current: 0.0A
Solar power: 0.0W
Solar power L: 0.0W
Solar power H: 0.0W
Load voltage: 0.0V
Load current: 0.0A
Load power: 0.0W
Load power L: 0.0W
Load power H: 0.0W
Battery current L: 0.0A
Battery current H: 0.0A
Battery voltage: 13.25V
Battery state of charge: 86%
Battery temperature: 16.91°C
Remote battery temperature: 0.0°C
Controller temperature: 16.55°C
Battery status: {'wrong_identifaction_for_rated_voltage': False, 'battery_inner_resistence_abnormal': False, 'temperature_warning_status': 'NORMAL', 'battery_status': 'NORMAL'}
Charging equipment status: {'input_voltage_status': 'NORMAL', 'charging_mosfet_is_short_circuit': False, 'charging_or_anti_reverse_mosfet_is_open_circuit': False, 'anti_reverse_mosfet_is_short_circuit': False, 'input_over_current': False, 'load_over_current': False, 'load_short_circuit': False, 'load_mosfet_short_circuit': False, 'disequilibrium_in_three_circuits': False, 'pv_input_short_circuit': False, 'charging_status': 'NO_CHARGING', 'fault': False, 'running': True}
Discharging equipment status: {'input_voltage_status': 'NORMAL', 'output_power_load': 'LIGHT', 'short_circuit': False, 'unable_to_discharge': False, 'unable_to_stop_discharging': False, 'output_voltage_abnormal': False, 'input_over_voltage': False, 'short_circuit_in_high_voltage_side': False, 'boost_over_voltage': False, 'output_over_voltage': False, 'fault': False, 'running': False}
Day time: False
Night time: True
Maximum battery voltage today: 14.5V
Minimum battery voltage today: 13.25V
Device over temperature: False


Battery Parameters:
Rated charging current: 20.0A
Rated load current: 20.0A
Battery real rated voltage: 12.0V
Battery type: USER_DEFINED
Battery capacity: 40AH
Temperature compensation coefficient: 0
Over voltage disconnect voltage: 14.7V
Charging limit voltage: 14.4V
Over voltage reconnect voltage: 14.6V
Equalize charging voltage: 14.4V
Boost charging voltage: 14.4V
Float charging voltage: 13.6V
Boost reconnect charging voltage: 13.3V
Low voltage reconnect voltage: 12.0V
Under voltage recover voltage: 12.0V
Under voltage warning voltage: 11.5V
Low voltage disconnect voltage: 11.0V
Discharging limit voltage: 11.0V
Battery rated voltage: 12V
Default load on/off in manual mode: OFF
Equalize duration: 0 min
Boost duration: 180 min
Battery discharge: 30%
Battery charge: 100%
Charging mode: VOLTAGE_COMPENSATION
```

## Python usage

To use the library within your Python code

```python
from epevermodbus.driver import EpeverChargeController


controller = EpeverChargeController("/dev/ttyUSB0", 1)

controller.get_solar_voltage()
```

See https://github.com/rosswarren/epevermodbus/blob/main/epevermodbus/driver.py for all available methods
