'''
# RPi_I2C_driver - TEST program

# The circuit:
# RaspberryPi       - 1602 I2C LCD
# Vcc               - Vcc
# GND               - GND
# GPIO02 (PIN3/SDA) - SDA
# GPIO03 (PIN5/SCL) - SCL
# 
# ※ I2C Enable is required in Raspberry Pi configuration.
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V Level convector is recommended.

# by eleparts (yeon) (https://www.eleparts.co.kr/)
'''
# include the library 
import RPi_I2C_driver
from time import *

# make custom characters - eleparts logo:
elelogo_1 = [
  0b00000,
  0b00000,
  0b00000,
  0b01101,
  0b10011,
  0b10010,
  0b10000,
  0b01100
]

elelogo_2 = [
  0b00000,
  0b01100,
  0b10101,
  0b01010,
  0b01010,
  0b01110,
  0b00000,
  0b00000
]

elelogo_3 = [
  0b00000,
  0b00000,
  0b00000,
  0b10000,
  0b11000,
  0b00100,
  0b00010,
  0b00100
]

elelogo_4 = [
  0b00100,
  0b00100,
  0b00110,
  0b00010,
  0b00001,
  0b00000,
  0b00000,
  0b00000
]

elelogo_5 = [
  0b00000,
  0b11100,
  0b10100,
  0b10100,
  0b01100,
  0b01001,
  0b00110,
  0b00000
]

elelogo_6 = [
  0b00110,
  0b00001,
  0b00001,
  0b01001,
  0b10110,
  0b00000,
  0b00000,
  0b00000
]


# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

# create a new character
lcd.createChar(0, elelogo_1)
# create a new character
lcd.createChar(1, elelogo_2)
# create a new character
lcd.createChar(2, elelogo_3)
# create a new character
lcd.createChar(3, elelogo_4)
# create a new character
lcd.createChar(4, elelogo_5)
# create a new character
lcd.createChar(5, elelogo_6)

lcd.setCursor(0,0)

lcd.write(0)
lcd.write(1)
lcd.write(2)

lcd.setCursor(0,1)

lcd.write(3)
lcd.write(4)
lcd.write(5)
