# epevermodbus

This package is intended to help you communicate with an EPever charge controller. It has been tested with an EPever Tracer AN but should work with other EPever devices.

![image](https://user-images.githubusercontent.com/613642/128763284-c5bbe67b-3905-479a-8a90-b1db16ff59fb.png)

## Project Overview

A Python library for communicating with EPEver charge controllers via Modbus protocol. This package provides a comprehensive interface for reading real-time data, managing battery parameters, and controlling EPEver solar charge controllers.

## Features
* Read real time data
* Read battery parameters
* Write battery parameters
* Automatic retries
* Comprehensive error handling
* Command-line interface for quick diagnostics

## File Structure
```
epevermodbus/
├── epevermodbus/
│   ├── __init__.py           # Package initialization
│   ├── command_line.py       # CLI interface implementation
│   ├── driver.py             # Main controller interface
│   └── extract_bits.py       # Utility for bit manipulation
├── examples/
│   └── write_battery_params.py  # Example for battery parameter configuration
├── test/
│   ├── __init__.py
│   └── test_extract_bits.py  # Unit tests for bit extraction
├── LICENSE                   # MIT License
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
└── setup.py                # Package configuration
```

## Connecting to the charge controller

I have only tested this package on Linux / Raspberry Pi but I see no reason why it should not work on other devices.

For the cable you have two options:

### 1. Official EPever cable

![image](https://user-images.githubusercontent.com/613642/128763357-c88e8ef6-481c-470f-9ca3-40dd7cf85914.png)

When using the official cable on Linux your device will show up something like `/dev/ttyXRUSB0`. You will need to use a custom driver to use this cable on Linux rather than the bundled cdc-acm driver. It can be difficult to get this driver working properly on Linux and Raspberry Pi.

On Windows you can use the driver provided by EPever and the cable should work fine so long as you check the rs485 checkbox in device manager.

### 2. Custom cable (Recommended for Linux)

You can quite easily make your own cable if you purchase a few parts, and with this approach you won't need a custom driver on Linux so it should be easier to get working. The device should show up as something like `/dev/ttyUSB0`.

For more information read: https://ross-warren.co.uk/2021/08/14/building-a-cable-to-connect-my-epever-charge-controller/

## Installation

### Requirements
* Python 3.x
* minimalmodbus
* retrying
* Serial port access (USB or RS485)

To install the package run:

```sh
pip install epevermodbus
```

This package requires Python 3, depending on your setup you might have to instead run:

```sh
pip3 install epevermodbus
```

For development installation:
```bash
git clone https://github.com/rosswarren/epevermodbus
cd epevermodbus
pip install -e .
```

## Usage

### Command Line Interface

To run the command line utility and see the debug output run the following on the command line:

```sh
epevermodbus --portname /dev/ttyUSB0 --slaveaddress 1 [--baudrate 115200]
```

```sh
usage: epevermodbus [-h] [--portname PORTNAME] [--slaveaddress SLAVEADDRESS] [--baudrate BAUDRATE]

optional arguments:
  -h, --help            show this help message and exit
  --portname PORTNAME   Port name for example /dev/ttyUSB0
  --slaveaddress SLAVEADDRESS
                        Slave address 1-247
  --baudrate BAUDRATE   Baudrate to communicate with controller (default is 115200)
```

### Python API

To use the library within your Python code:

```python
from epevermodbus.driver import EpeverChargeController

# Initialize controller
controller = EpeverChargeController("/dev/ttyUSB0", 1)

# Read real-time data
solar_voltage = controller.get_solar_voltage()
battery_voltage = controller.get_battery_voltage()
battery_soc = controller.get_battery_state_of_charge()

# Read battery parameters
battery_type = controller.get_battery_type()
battery_capacity = controller.get_battery_capacity()

# Configure battery parameters
controller.set_battery_capacity(100)  # Set capacity to 100Ah
controller.set_battery_voltage_control_registers(
    float_charging_voltage=13.6,
    boost_charging_voltage=14.4
)
```

See [driver.py](https://github.com/rosswarren/epevermodbus/blob/main/epevermodbus/driver.py) for all available methods.

## Example Output

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

## Troubleshooting Guide

### Common Issues

1. Connection Problems
   * Check cable connections
   * Verify port name (/dev/ttyUSB0 or /dev/ttyXRUSB0)
   * Confirm baudrate settings
   * Check slave address (default: 1)

2. Communication Errors
   * Verify cable integrity
   * Check for interference sources
   * Confirm controller is powered
   * Try reducing baudrate

3. Data Reading Issues
   * Check controller power
   * Verify register addresses
   * Confirm data scaling factors

### Error Handling
The library implements automatic retry mechanisms for common communication issues:
* 5 retry attempts with 200ms delay
* Automatic error recovery
* Comprehensive error reporting

## Development

### Testing
```bash
python -m unittest discover test
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit pull request

### Code Style
* Follow PEP 8 guidelines
* Include docstrings for new methods
* Add unit tests for new features

## Technical Notes

### Register Map
* 0x3100-0x311F: Real-time data
* 0x3200-0x321F: Status information
* 0x9000-0x900F: Battery parameters
* Full register map in driver.py

### Communication Protocol
* Modbus RTU
* Default: 115200 baud, 8N1
* Slave addresses: 1-247
* Automatic retry on failure

## Security Considerations
* No authentication in Modbus protocol
* Secure physical access to controller
* Use in trusted networks only
* Monitor for unexpected parameter changes

## License
MIT License - See LICENSE file for details

## Support
* GitHub Issues: [Project Issues](https://github.com/rosswarren/epevermodbus/issues)
* Documentation: See inline code documentation
* Examples: Check examples/ directory