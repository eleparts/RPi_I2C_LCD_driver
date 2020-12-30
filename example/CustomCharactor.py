'''
# RPi_I2C_driver - LiquidCrystal Library - Custom Characters
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch prints "I <heart> Ras Pi!!" and a little dancing man
# to the LCD.
#
# example code
# https://www.arduino.cc/en/Reference/LiquidCrystalCreateChar
#
# Based on Adafruit's example at
# https://github.com/adafruit/SPI_VFD/blob/master/examples/createChar/createChar.pde
#
# The circuit:
# RaspberryPi       - 1602 I2C LCD
# Vcc               - Vcc
# GND               - GND
# GPIO02 (PIN3/SDA) - SDA
# GPIO03 (PIN5/SCL) - SCL
#
# Modified to not use poterntiometer and analog input.
# 
# ※ I2C Enable is required in Raspberry Pi configuration.
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V logic level converter is recommended.
#
 created 21 Mar 2011
 by Tom Igoe
 modified 11 Nov 2013
 by Scott Fitzgerald
 modified 7 Nov 2016
 by Arturo Guadalupi
# modified Python 21 June 2019
# by eleparts (yeon) (https://www.eleparts.co.kr/)
'''
# include the library 
import RPi_I2C_driver
from time import *

# make some custom characters:
heart = [
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000
]

smiley = [ 
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b10001,
    0b01110,
    0b00000
]

frownie = [
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b10001
]

armsDown = [
    0b00100,
    0b01010,
    0b00100,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010
]

armsUp = [
    0b00100,
    0b01010,
    0b00100,
    0b10101,
    0b01110,
    0b00100,
    0b00100,
    0b01010
]

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

# create a new character
lcd.createChar(0, heart)
# create a new character
lcd.createChar(1, smiley)
# create a new character
lcd.createChar(2, frownie)
# create a new character
lcd.createChar(3, armsDown)
# create a new character
lcd.createChar(4, armsUp)


# set the cursor to the top left
lcd.setCursor(0, 0)

# Print a message to the lcd.
lcd.print("I ")
lcd.write(0) # when calling lcd.write() '0' must be cast as a byte
lcd.print(" Ras Pi! ")
lcd.write(1)

while True:

    lcd.setCursor(4, 1)
    # draw the little man, arms down:
    lcd.write(3)
    sleep(0.3)

    lcd.setCursor(4, 1)
    # draw him arms up:
    lcd.write(4)
    sleep(0.3)