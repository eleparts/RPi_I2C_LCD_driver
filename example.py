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
# ※ When the voltage of the LCD / I2C board is 5V, use of 3.3V logic level converter is recommended.

# by eleparts (yeon) (https://www.eleparts.co.kr/)
# 2019-06-25
'''
# include the library 
import RPi_I2C_driver
from time import *

# make custom characters - eleparts logo:
# https://maxpromer.github.io/LCD-Character-Creator/
eleLogo1 = [
    0b00000,
    0b00000,
    0b00110,
    0b01001,
    0b10001,
    0b10000,
    0b10000,
    0b01110
]

eleLogo2 = [
    0b00011,
    0b00100,
    0b01001,
    0b01010,
    0b10010,
    0b10001,
    0b00000,
    0b00000
]
eleLogo3 = [
    0b00000,
    0b10000,
    0b00110,
    0b01001,
    0b01000,
    0b10000,
    0b00000,
    0b00000
]

eleLogo4 = [
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b10000,
    0b01000,
    0b01000,
    0b10000
]

eleLogo5 = [
    0b00010,
    0b00100,
    0b00100,
    0b00010,
    0b00001,
    0b00000,
    0b00000,
    0b00000
]

eleLogo6 = [
    0b00000,
    0b00000,
    0b00011,
    0b00100,
    0b00100,
    0b11001,
    0b00010,
    0b00001
]

eleLogo7 = [
    0b00000,
    0b00000,
    0b00000,
    0b10011,
    0b10101,
    0b00100,
    0b01000,
    0b10000
]

eleLogo8 = [
    0b11000,
    0b00100,
    0b00010,
    0b00010,
    0b00100,
    0b11000,
    0b00000,
    0b00000
]

##### START EXAMPLE #####

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

# Turn on the cursor:
lcd.cursor()

# Print a message to the LCD.
lcd.print("Hello")

sleep(1)

# At 0.5c second interval " World!!!" Print
lcd.print(" World!!!", 0.5)

sleep(2)

lcd.clear()

# Turn off the cursor:
lcd.noCursor()

lcd.print("eleparts")

# set the cursor position:
lcd.setCursor(5,1)
lcd.print(".co.kr")

# create a new character
lcd.createChar(0, eleLogo1)
lcd.createChar(1, eleLogo2)
lcd.createChar(2, eleLogo3)
lcd.createChar(3, eleLogo4)
lcd.createChar(4, eleLogo5)
lcd.createChar(5, eleLogo6)
lcd.createChar(6, eleLogo7)
lcd.createChar(7, eleLogo8)

lcd.setCursor(12,0)

# print 'createChar'
lcd.write(0)
lcd.write(1)
lcd.write(2)
lcd.write(3)

lcd.setCursor(12,1)

lcd.write(4)
lcd.write(5)
lcd.write(6)
lcd.write(7)

sleep(2)

lcd.setCursor(11,1)

# Turn on the blinking cursor:
lcd.blink()

sleep(3)

# screen moving
for a in range(2):

    for i in range(2):
        # Move the screen to the right
        lcd.scrollDisplayLeft()
        sleep(0.4)

    for i in range(4):
        # Move the screen to the right
        lcd.scrollDisplayRight()
        sleep(0.4)

    for i in range(2):
        # Move the screen to the right
        lcd.scrollDisplayLeft()
        sleep(0.4)