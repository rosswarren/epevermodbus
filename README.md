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

To run the command line utility and see the debug output run the following on the command line

```sh
epevermodbus
```

Example output

```sh
Real Time Data
Solar voltage:  23.28
Solar current:  0.16
Solar power:  0.17
Solar power L: 3.65
Solar power H: 0.0
Load voltage:  0.0
Load current:  0.0
Load power:  0.0
Load power L: 0.0
Load power H: 0.0
Battery capacity:  40
Battery current L:  0.28
Battery current H:  0.0
Battery voltage:  13.55
Battery state of charge:  0.98
Battery temperature:  23.49
Remote battery temperature:  0.0
Controller temperature:  27.56
Battery status:  0.0
Charging equipment status:  0.07
Discharging equipment status:  0.0
Day time: True
Night time: False
Maximum battery voltage today: 14.74
Minimum battery voltage today: 13.47
Device over temperature: False


Battery Parameters
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
