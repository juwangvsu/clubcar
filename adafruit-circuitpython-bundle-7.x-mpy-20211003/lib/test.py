from time import sleep
import board
import adafruit_ds1841
from analogio import AnalogIn

i2c = board.I2C()
ds1841 = adafruit_ds1841.DS1841(i2c)
wiper_output = AnalogIn(board.A0)