#!/usr/bin/python

# Monitor temperature using a MCP9808 High Accuracy I2C Temperature Sensor Breakout Board on a BeagleBone Black then
# display results on a 16 * 2 Character LCD screen

import math
import time
import Adafruit_CharLCD as LCD
import Adafruit_MCP9808.MCP9808 as MCP9808
import pyowm

# Set API Key
owm = pyowm.OWM('Your API Key')

# BeagleBone Black LCD configuration:
lcd_rs        = 'P8_8'
lcd_en        = 'P8_10'
lcd_d4        = 'P8_18'
lcd_d5        = 'P8_16'
lcd_d6        = 'P8_14'
lcd_d7        = 'P8_12'
lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# For the Beaglebone Black the library assumes bus 1 by default, which is exposed with SCL = P9_19 and SDA = P9_20.
sensor = MCP9808.MCP9808()

# Start communication with MCP9808
sensor.begin()

# Read current temperature
temp = sensor.readTempC()

# Convert float to  String
tempStr = str(temp)

# Temperature to display message for Apt(Apartment)
displayTemp = "Apt : " + tempStr

# Search for current weather in Vancouver, Canada
observation = owm.weather_at_place('Vancouver,CA')
w = observation.get_weather()

CityTemp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

CityTempCurrent = CityTemp.get("temp")

# Convert float to String
TempCurrentStr = str(CityTempCurrent)

# Temperature to display message for City
displayCurrentTemp = "City: " + TempCurrentStr

# Final message to be displayed
DisplayLCD = "" + displayTemp + "\n" + displayCurrentTemp

# Print a two line message
lcd.clear()
lcd.message(DisplayLCD)

# Sleep for 14 mins (840 seconds)
time.sleep(840.0)

quit()
