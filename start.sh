#!/bin/sh

echo "Create a driver file in the example code directory"

echo "./example/RPi_I2C_driver.py"
cp RPi_I2C_driver.py ./example/RPi_I2C_driver.py
echo "./original_example/RPi_I2C_driver.py"
cp RPi_I2C_driver.py ./original_example/RPi_I2C_driver.py
