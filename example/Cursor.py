'''
# RPi_I2C_driver - LiquidCrystal Library - Cursor
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch prints "Hello World!" to the LCD and
# uses the cursor()  and noCursor() methods to turn
# on and off the cursor.
#
# This example code is in the public domain.
# https://www.arduino.cc/en/Tutorial/LiquidCrystalCursor
#
# The circuit:
# RaspberryPi       - 1602 I2C LCD
# Vcc               - Vcc
# GND               - GND
# GPIO02 (PIN3/SDA) - SDA
# GPIO03 (PIN5/SCL) - SCL
# 
# ※ I2C Enable is required in Raspberry Pi configuration.
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V logic level converter is recommended.
#
# Library originally added 18 Apr 2008
# by David A. Mellis
# library modified 5 Jul 2009
# by Limor Fried (http://www.ladyada.net)
# example added 9 Jul 2009
# by Tom Igoe
# modified 22 Nov 2010
# by Tom Igoe
# modified 7 Nov 2016
# by Arturo Guadalupi
# modified Python 20 June 2019
# by eleparts (yeon) (https://www.eleparts.co.kr/)
'''
# include the library 
import RPi_I2C_driver
from time import *

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

# Print a message to the LCD.
lcd.print("hello, world!")

while True:

    # Turn off the cursor:
    lcd.noCursor()
    sleep(0.5)
    # Turn on the cursor:
    lcd.cursor()
    sleep(0.5)
