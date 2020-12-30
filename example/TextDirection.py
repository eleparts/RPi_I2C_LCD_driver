'''
# RPi_I2C_driver - LiquidCrystal Library - TextDirection 
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch demonstrates how to use leftToRight() and rightToLeft()
# to move the cursor.
#
# This example code is in the public domain.
# http://www.arduino.cc/en/Tutorial/LiquidCrystalTextDirection
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

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

lcd.cursor()

thisChar = 'a'

while True:

    # reverse directions at 'm':
    if (thisChar == 'm') :
        # go right for the next letter
        lcd.rightToLeft()
    
    # reverse again at 's':
    if (thisChar == 's') :
        # go left for the next letter
        lcd.leftToRight()
    
    # reset at 'z':
    if (thisChar > 'z') :
        # go to (0,0):
        lcd.home()
        # start again at 0
        thisChar = 'a'
    
    # print the character
    lcd.write(thisChar)
    # wait a second:
    sleep(1)
    # Retrieve the ASCII code value of the character and store it as a character after +1
    thisChar = chr(ord(thisChar) + 1)
