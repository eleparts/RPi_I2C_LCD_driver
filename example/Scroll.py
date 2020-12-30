'''
# RPi_I2C_driver - LiquidCrystal Library - scrollDisplayLeft() and scrollDisplayRight()
#
# This example has been implemented to enable Python in Raspberry Pi.
# 
# This sketch prints "Hello World!" to the LCD and uses the
# scrollDisplayLeft() and scrollDisplayRight() methods to scroll
# the text.
#
# This example code is in the public domain.
# http://www.arduino.cc/en/Tutorial/LiquidCrystalScroll
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

# Print a message to the LCD
lcd.print("hello, world!")

sleep(1)

while True:

    # scroll 13 positions (string length) to the left
    # to move it offscreen left:
    for i in range(13) :
        # scroll one position left:
        lcd.scrollDisplayLeft()
        # wait a bit:
        sleep(0.15)
    

    # scroll 29 positions (string length + display length) to the right
    # to move it offscreen right:
    for i in range(29) :
        # scroll one position right:
        lcd.scrollDisplayRight()
        # wait a bit:
        sleep(0.15)
    

    # scroll 16 positions (display length + string length) to the left
    # to move it back to center:
    for i in range(16) :
        # scroll one position left:
        lcd.scrollDisplayLeft()
        # wait a bit:
        sleep(0.15)
    

    # delay at the end of the full loop:
    sleep(1)
