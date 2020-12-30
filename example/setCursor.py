'''
# RPi_I2C_driver - LiquidCrystal Library - setCursor 
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch prints to all the positions of the LCD using the
# setCursor() method:
#
# This example code is in the public domain.
# http://www.arduino.cc/en/Tutorial/LiquidCrystalSetCursor
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
# modified Python 21 June 2019
# by eleparts (yeon) (https://www.eleparts.co.kr/)
'''
# include the library 
import RPi_I2C_driver
from time import *

# size of your LCD :
numRows = 2
numCols = 16

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27, numCols, numRows)

while True:

    # loop from ASCII 'a' to ASCII 'z':
    for thisLetter in range(ord('a'), ord('z')):
        # loop over the columns:
        for thisRow in range(numRows):
            # loop over the rows:
            for thisCol in range(numCols):
                # set the cursor position:
                lcd.setCursor(thisCol, thisRow)
                # print the letter:
                lcd.write(thisLetter)
                sleep(0.2)

