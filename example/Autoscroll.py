'''
# RPi_I2C_driver - LiquidCrystal Library - Autoscroll


'''
# include the library 
import RPi_I2C_driver
from time import *

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

lcd.setCursor(0, 0)

for thisChar in range(10):
  lcd.print(str(thisChar))
  sleep(0.5)


lcd.setCursor(16, 1)

lcd.autoscroll()

for thisChar in range(10):
  lcd.print(str(thisChar))
  sleep(0.5)

lcd.noAutoscroll()

lcd.clear()