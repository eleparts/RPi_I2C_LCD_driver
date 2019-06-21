# -*- coding: utf-8 -*-
"""
Compiled, mashed and generally mutilated 2014-2015 by Denis Pleic
Made available under GNU GENERAL PUBLIC LICENSE

# Modified Python I2C library for Raspberry Pi
# as found on http://www.recantha.co.uk/blog/?p=4849
# Joined existing 'i2c_lib.py' and 'lcddriver.py' into a single library
# added bits and pieces from various sources
# By DenisFromHR (Denis Pleic)
# 2015-02-10, ver 0.1

# Arduino LiquidCrystal_I2C Implement functionality
# https://www.arduino.cc/en/Reference/LiquidCrystal
# By eleparts (yeon)
# 1602 I2C LCD : https://www.eleparts.co.kr/EPXHVBKK
# 2019-06-21
#
"""
#
import smbus
from time import *

class i2c_device:
   def __init__(self, addr, port=1):
      self.addr = addr
      self.bus = smbus.SMBus(port)

# Write a single command
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001) 

# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.bus.write_byte_data(self.addr, cmd, data)
      sleep(0.0001)

# Write a block of data
   def write_block_data(self, cmd, data):
      self.bus.write_block_data(self.addr, cmd, data)
      sleep(0.0001)

# Read a single byte
   def read(self):
      return self.bus.read_byte(self.addr)

# Read
   def read_data(self, cmd):
      return self.bus.read_byte_data(self.addr, cmd)

# Read a block of data
   def read_block_data(self, cmd):
      return self.bus.read_block_data(self.addr, cmd)



# LCD Address
ADDRESS = 0x27

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00  #I2C only 4bit
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class lcd:

   _Entry_mode_set = LCD_ENTRYMODESET         # 0x04
   _Display_control = LCD_DISPLAYCONTROL      # 0x08
   _Function_set = LCD_FUNCTIONSET            # 0x20

   _row_offsets = [0x00, 0x40, 0x00, 0x40]
   _begin_set = 0x00

   _numlines = 2 # line 

   # initializes objects and lcd
   # default 0x27, 16 x 02, 5x8 Dot(0x00)
   def __init__(self, I2C_addr = None, cols = 16, lines = 2, dotsize = LCD_5x8DOTS):
      
      if I2C_addr is None:
         I2C_addr = ADDRESS

      # cols
      self.setRowOffsets(0x00, 0x40, 0x00 + cols, 0x40 + cols)
      # line (row)
      if (lines > 1) :
         self._begin_set |= LCD_2LINE
      else: 
         self._begin_set |= LCD_1LINE

      self._numlines = lines

      # dotsize
      if ((dotsize != LCD_5x8DOTS) and (lines == 1)):
         self._begin_set |= LCD_5x10DOTS
      else:
         self._begin_set |= LCD_5x8DOTS


      self.lcd_device = i2c_device(I2C_addr)

      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x03)  
      self.lcd_write(0x02)   

      self._Function_set = LCD_FUNCTIONSET | self._begin_set | LCD_4BITMODE
      self.lcd_write(self._Function_set)   

      self._Display_control = LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
      self.lcd_write(self._Display_control)                         

      self._Entry_mode_set = LCD_ENTRYMODESET | LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
      self.lcd_write(self._Entry_mode_set)

      self.lcd_write(LCD_CLEARDISPLAY)
      
      sleep(0.2)


   # clocks EN to latch command
   def lcd_strobe(self, data):
      self.lcd_device.write_cmd(data | En | LCD_BACKLIGHT)
      sleep(.0005)
      self.lcd_device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
      sleep(.0001)

   def lcd_write_four_bits(self, data):
      self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
      self.lcd_strobe(data)

   # write a command to lcd
   def lcd_write(self, cmd, mode=0):
      self.lcd_write_four_bits(mode | (cmd & 0xF0))
      self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

   # write a character to lcd (or character rom) 0x09: backlight | RS=DR<
   # works!
   def lcd_write_char(self, charvalue, mode=1):
      self.lcd_write_four_bits(mode | (charvalue & 0xF0))
      self.lcd_write_four_bits(mode | ((charvalue << 4) & 0xF0))
  
   # put string function
   def lcd_display_string(self, string, line):
      if line == 1:
         self.lcd_write(0x80)
      if line == 2:
         self.lcd_write(0xC0)
      if line == 3:
         self.lcd_write(0x94)
      if line == 4:
         self.lcd_write(0xD4)

      for char in string:
         self.lcd_write(ord(char), Rs)

   # clear lcd and set to home
   def lcd_clear(self):
      self.lcd_write(LCD_CLEARDISPLAY)
      self.lcd_write(LCD_RETURNHOME)

   # define backlight on/off (lcd.backlight(1); off= lcd.backlight(0)
   def backlight(self, state): # for state, 1 = on, 0 = off
      if state == 1:
         self.lcd_device.write_cmd(LCD_BACKLIGHT)
      elif state == 0:
         self.lcd_device.write_cmd(LCD_NOBACKLIGHT)

   # add custom characters (0 - 7)
   def lcd_load_custom_chars(self, fontdata):
      self.lcd_write(0x40)
      for char in fontdata:
         for line in char:
            self.lcd_write_char(line)         
         
   # define precise positioning (addition from the forum)
   def lcd_display_string_pos(self, string, line, pos):
      if line == 1:
         pos_new = self._row_offsets[0] + pos
      elif line == 2:
         pos_new = self._row_offsets[1] + pos
      elif line == 3:
         pos_new = self._row_offsets[2] + pos
      elif line == 4:
         pos_new = self._row_offsets[3] + pos

      self.lcd_write(0x80 + pos_new)

      for char in string:
         self.lcd_write(ord(char), Rs)

   '''
   # LiquidCrystal Library
   # https://www.arduino.cc/en/Reference/LiquidCrystal
   '''

   def setRowOffsets(self, row0, row1, row2, row3):
      self._row_offsets[0] = row0
      self._row_offsets[1] = row1
      self._row_offsets[2] = row2
      self._row_offsets[3] = row3

   def command(self, data):
      self.lcd_write(data)

   
   # >> User Function 

   ### RPi_I2C_driver.lcd(I2C ADDR, LCD Col, LCD Row, Dot(5x8 == 0)) 
   # LiquidCrystal() / begin()
   # > mylcd = RPi_I2C_driver.lcd(0x27)
   # > mylcd = RPi_I2C_driver.lcd(0x27, 16, 2)
   
   # LCD 내용 지우기 & 커서위치 좌측 상단으로 이동
   def clear(self):
      self.command(LCD_CLEARDISPLAY)
      sleep(1)

   # 커서위치 좌측 상단으로 이동
   def home(self):
      self.command(LCD_RETURNHOME)
      sleep(1)

   # 커서위치 이동 home : (0,0)
   def setCursor(self, col, row):
      if row == 0:
         row_value = self._row_offsets[0]
      elif row == 1:
         row_value = self._row_offsets[1]
      elif row == 2:
         row_value = self._row_offsets[2]
      elif row == 3:
         row_value = self._row_offsets[3]
      else:
         row_value = 0x00

      if row > self._numlines:
         row = self._numlines-1    # we count rows starting 0
      
      self.command(LCD_SETDDRAMADDR | (row_value  + col))

   # LCD에 글자 출력 (HEX, DEC, BIN 입력)
   def write(self, data, delay = 0):
      try: 
         self.lcd_write(data, Rs)
         sleep(delay)
      except TypeError:
         self.print(data, delay)

   # LCD에 글자/문자열 출력
   def print(self, string, delay = 0):
      string = str(string)

      for char in string:
         self.lcd_write(ord(char), Rs)
         #self.lcd_write_char(ord(char))
         sleep(delay)


   # Turns the underline cursor on/off
   def cursor(self):
      self._Display_control |= LCD_CURSORON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)
  


   def noCursor(self):
      self._Display_control &= ~LCD_CURSORON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)

   # Turn on and off the blinking cursor
   def blink(self):
      self._Display_control |= LCD_BLINKON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)

   def noBlink(self):
      self._Display_control &= ~LCD_BLINKON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)

   # Turn the display on/off (quickly)
   def display(self):
      self._Display_control |= LCD_DISPLAYON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)

   def noDisplay(self):
      self._Display_control &= ~LCD_DISPLAYON
      self.command(LCD_DISPLAYCONTROL | self._Display_control)

   # These commands scroll the display without changing the RAM
   def scrollDisplayLeft(self):
      self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)

   def scrollDisplayRight(self):
      self.command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

   # This will 'right justify' text from the cursor
   def autoscroll(self):
      self._Entry_mode_set |= LCD_ENTRYSHIFTINCREMENT
      self.command(LCD_ENTRYMODESET | self._Entry_mode_set)

   # This will 'left justify' text from the cursor
   def noAutoscroll(self):
      self._Entry_mode_set &= ~LCD_ENTRYSHIFTINCREMENT         # LCD_ENTRYSHIFTDECREMENT
      self.command(LCD_ENTRYMODESET | self._Entry_mode_set)

   # This is for text that flows Left to Right
   def leftToRight(self):
      self._Entry_mode_set |= LCD_ENTRYLEFT
      self.command(LCD_ENTRYMODESET | self._Entry_mode_set)

   # This is for text that flows Right to Left
   def rightToLeft(self):
      self._Entry_mode_set &= ~LCD_ENTRYLEFT                   # LCD_ENTRYRIGHT
      self.command(LCD_ENTRYMODESET | self._Entry_mode_set)

   # Allows us to fill the first 8 CGRAM locations
   # with custom characters
   def createChar(self, location, charmap = []):
      location &= 0x7 # we only have 8 locations 0-7
      self.command(LCD_SETCGRAMADDR | (location << 3))
      for i in range(8):
         self.write(charmap[i])
