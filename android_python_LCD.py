'''from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.putchar(chr(247))
'''
'''
from smbus2 import SMBu
import smbus2 as smbus

import time

class LCD:
    def __init__(self, pi_rev = 2, i2c_addr = 0x3F, backlight = True):

        # device constants
        self.I2C_ADDR  = i2c_addr
        self.LCD_WIDTH = 16   # Max. characters per line

        self.LCD_CHR = 1 # Mode - Sending data
        self.LCD_CMD = 0 # Mode - Sending command

        self.LCD_LINE_1 = 0x80 # LCD RAM addr for line one
        self.LCD_LINE_2 = 0xC0 # LCD RAM addr for line two

        if backlight:
            # on
            self.LCD_BACKLIGHT  = 0x08
        else:
            # off
            self.LCD_BACKLIGHT = 0x00

        self.ENABLE = 0b00000100 # Enable bit

        # Timing constants
        self.E_PULSE = 0.0005
        self.E_DELAY = 0.0005

        # Open I2C interface
        if pi_rev == 2:
            # Rev 2 Pi uses 1
            self.bus = smbus.SMBus(1)
        elif pi_rev == 1:
            # Rev 1 Pi uses 0
            self.bus = smbus.SMBus(0)
        else:
            raise ValueError('pi_rev param must be 1 or 2')

        # Initialise display
        self.lcd_byte(0x33, self.LCD_CMD) # 110011 Initialise
        self.lcd_byte(0x32, self.LCD_CMD) # 110010 Initialise
        self.lcd_byte(0x06, self.LCD_CMD) # 000110 Cursor move direction
        self.lcd_byte(0x0C, self.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28, self.LCD_CMD) # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01, self.LCD_CMD) # 000001 Clear display

    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = 1 for data, 0 for command

        bits_high = mode | (bits & 0xF0) | self.LCD_BACKLIGHT
        bits_low = mode | ((bits<<4) & 0xF0) | self.LCD_BACKLIGHT

        # High bits
        self.bus.write_byte(self.I2C_ADDR, bits_high)
        self.toggle_enable(bits_high)

        # Low bits
        self.bus.write_byte(self.I2C_ADDR, bits_low)
        self.toggle_enable(bits_low)

    def toggle_enable(self, bits):
        time.sleep(self.E_DELAY)
        self.bus.write_byte(self.I2C_ADDR, (bits | self.ENABLE))
        time.sleep(self.E_PULSE)
        self.bus.write_byte(self.I2C_ADDR,(bits & ~self.ENABLE))
        time.sleep(self.E_DELAY)

    def message(self, string, line = 1):
        # display message string on LCD line 1 or 2
        if line == 1:
            lcd_line = self.LCD_LINE_1
        elif line == 2:
            lcd_line = self.LCD_LINE_2
        else:
            raise ValueError('line number must be 1 or 2')

        string = string.ljust(self.LCD_WIDTH," ")

        self.lcd_byte(lcd_line, self.LCD_CMD)

        for i in range(self.LCD_WIDTH):
            self.lcd_byte(ord(string[i]), self.LCD_CHR)

    def clear(self):
        # clear LCD display
        self.lcd_byte(0x01, self.LCD_CMD)


        '''

from asukiaaa_py_i2c_lcd.core import I2cLcd, AQM1602_ADDR

I2C_BUS_NUM = 1

lcd = I2cLcd(I2C_BUS_NUM, AQM1602_ADDR)
lcd.setCursor(0,0)
lcd.write("Hello")
lcd.setCursor(3,1)
lcd.write("World")

'''
import subprocess
import argparse
import os
from glob import glob


def _build_wheel(source_dir, destination_dir):
    try:
        subprocess.check_call(['python', 'setup.py', 'bdist_wheel', '--dist-dir', destination_dir], cwd=source_dir)
    except subprocess.CalledProcessError:
        print('Error while building wheel from {} directory'.format(source_dir))


def build_wheels(sources, wheels):
    """
    Trying to create wheel for package in each subdirectory from specified sources dir.
    """
    dest_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), wheels))
    for src_dir in glob(os.path.join(sources, '*')):
        if os.path.isdir(src_dir):
            _build_wheel(src_dir, dest_dir)


parser = argparse.ArgumentParser(
    description='Build wheels for all packages from sources dir specified.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--sources-dir", dest="sources", required=False, default="./venv/src", help="sources directory path")
parser.add_argument("--wheels-dir", dest="wheels", required=False, default="./wheels", help="path to directory with wheels")

args = parser.parse_args()
kwargs = args.__dict__
build_wheels(**kwargs)
'''

