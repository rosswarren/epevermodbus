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

## Python usage

To use the library within your Python code

```python
from epevermodbus.driver import EpeverChargeController


controller = EpeverChargeController("/dev/ttyUSB0", 1)

controller.get_solar_voltage()
```
