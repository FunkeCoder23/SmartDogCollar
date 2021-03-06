import I2C_LCD_driver
import rssi
from time import sleep
import board
import busio
import adafruit_lsm9ds1

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

interface = 'wlan0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['pi-mobile']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.

mylcd = I2C_LCD_driver.lcd()
while True:
    #get Gyro data
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro

    #get RSSI data
    ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
    name = ap_info[0]["ssid"]
    signal = ap_info[0]["signal"]

    #Write RSSI info
    mylcd.lcd_clear()
    mylcd.lcd_display_string(u"SSID: {}".format(name), 1)
    mylcd.lcd_display_string(u"RSSI: {} dBm".format(signal), 2)
    sleep(3)
    #Write Gyro info
    mylcd.lcd_clear()
    mylcd.lcd_display_string(u"Accel:({0:0.3f}x,".format(accel_x), 1)
    mylcd.lcd_display_string(u"{0:0.3f}y,{0:0.3f}z".format(accel_y, accel_z), 2)
    sleep(3)
    mylcd.lcd_clear()
    mylcd.lcd_display_string(u"Mag: ({0:0.3f}x)".format(mag_x), 1)
    mylcd.lcd_display_string(u"{0:0.3f}y,{0:0.3f}z".format(mag_y, mag_z), 2)
    sleep(3)
    mylcd.lcd_clear()
    mylcd.lcd_display_string(u"Gyro: ({0:0.3f}x)".format(gyro_x),1)
    mylcd.lcd_display_string(u"{0:0.3f}y,{0:0.3f}z".format(gyro_y, gyro_z), 2)
    sleep(3)