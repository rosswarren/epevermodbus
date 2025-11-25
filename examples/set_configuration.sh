#!/bin/bash
#
# Notes from https://diysolarforum.com/threads/struggling-with-basic-lifepo4-settings-in-epever-tracer.17785/
#
# Load-related:
# Over voltage disconnect : if the battery voltage exceeds this, the load outputs disconnect from the load from the battery.
# Over Voltage reconnect: if the load outputs have been disconnected due to the battery exceeding over voltage a reconnect will occur at this value.
# Low voltage disconnect: load outputs are disconnected from the battery at this voltage.
# Low voltage reconnect: if the load outputs have been disconnected due to a low battery, this voltage is the turn on value.
# Under voltage warning: warning set at this voltage.
# Under voltage warning reconnect: warning turned off at this voltage.
# Discharging limit voltage: other than issuing a warning at the set voltage the stand alone unit cannot do anything about this.
#
# Charging-related:
# Charging limit voltage: if the battery voltage exceeds this, charging the battery from solar is stopped.
# Boost charge voltage: under the boost mode, the controller will charge the battery at maximum power from the solar panels until this value is reached.
# Float charge voltage: once the boost duration has been completed the controller will modify the maximum power search and load the panels to produce a constant float voltage at the battery.
# Boost reconnect voltage: once the unit is in float mode the voltage may vary due to solar conditions and any load on the battery. If the battery voltage falls to this value the controller re enters the Boost stage.
# Boost Duration: once the boost voltage has been reached the voltage will be held constant for this period. This is the absorption period where the battery is completely charged.


PORTNAME=/dev/ttyS5
PYSCRIPT_PATH="../epevermodbus"

# This is for a Lead Acid AGM battery
#python3 command_line.py \
#    --portname ${PORTNAME} \
#    --set-battery-capacity 75 \
#    --set-battery-type USER_DEFINED \
#    --set-float-charging-voltage 13.5 \
#    --set-low-voltage-reconnect-voltage 12.4 \
#    --set-low-voltage-disconnect-voltage 11.7 \
#    --set-discharging-limit-voltage 11.6 \
#    --set-equalize-duration 0 \
#    --set-boost-duration 120 \
#    --set-time

# This is for a LiFePo4 battery.  
# Minimum voltage at zero SOC is about 10.0V, but we set it higher to avoid 100% depth of discharge.
# 11.3V is around 5% SoC.
# Note: The voltages seem to be required to be set in decreasing order, or they won't take effect.
# User Manual says: When the default battery type is selected, the battery voltage
# control parameters will be set by default and can‟t be changed. To change
# these parameters, select "User" battery type.

python3 ${PYSCRIPT_PATH}/command_line.py \
    --portname ${PORTNAME} \
    --set-battery-type USER_DEFINED \
    --set-battery-capacity 100 \
    --set-over-voltage-disconnect-voltage 14.7 \
    --set-over-voltage-reconnect-voltage 14.6 \
    --set-charging-limit-voltage 14.55 \
    --set-equalize-charging-voltage 14.55 \
    --set-boost-charging-voltage 14.5 \
    --set-float-charging-voltage 13.5 \
    --set-boost-reconnect-charging-voltage 13.4 \
    --set-low-voltage-reconnect-voltage 12.4 \
    --set-low-voltage-disconnect-voltage 11.3 \
    --set-discharging-limit-voltage 11.3 \
    --set-equalize-duration 0 \
    --set-boost-duration 180 \
    --set-low-temp-charging-limit 2 \
    --set-low-temp-discharging-limit -20 \
    --set-time
echo

python3 ${PYSCRIPT_PATH}/command_line.py \
    --portname ${PORTNAME}
