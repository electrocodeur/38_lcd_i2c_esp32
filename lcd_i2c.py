import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    lcd.putstr("I2C LCD ESP32")
    sleep(2)
    lcd.clear()
    lcd.putstr("Lets Count 0-10!")
    sleep(2)
    lcd.clear()
    for i in range(11):
        lcd.putstr(str(i))
        sleep(1)
        lcd.clear()
    sleep(0.5)
    lcd.putstr("Ceci")
    lcd.move_to(1,1)
    lcd.putstr("est un")
    lcd.move_to(1,2)
    lcd.putstr("programme")
    lcd.move_to(1,3)
    lcd.putstr("sur 4 lignes")
    sleep(5)