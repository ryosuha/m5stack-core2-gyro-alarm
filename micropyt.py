import os, sys, io
import M5
import network
import time
from M5 import *


def setup():

  M5.begin()
  Widgets.fillScreen(0x222222)
  print('setup')

def loop():
  M5.update()

def gyro_sensor():
  print(Imu.getGyro()[0])
  Speaker.begin()
  Speaker.setVolumePercentage(0.5)
  labelx1 = Widgets.Label("Text", 0, 0, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  labely1 = Widgets.Label("Text", 0, 24, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  labelz1 = Widgets.Label("Text", 0, 48, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  labelx2 = Widgets.Label("Text", 0, 72, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  labely2 = Widgets.Label("Text", 0, 96, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  labelz2 = Widgets.Label("Text", 0,120, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)
  while True:
    x1 = Imu.getGyro()[0]
    y1 = Imu.getGyro()[1]
    z1 = Imu.getGyro()[2]
    print("x1=" + str(x1) + " y1=" + str(y1) + " z1=" + str(z1))
    message = "x1=" + str(x1) + " y1=" + str(y1) + " z1=" + str(z1)
    labelx1.setText("x1=" + str(x1))
    labely1.setText("y1=" + str(y1))
    labelz1.setText("z1=" + str(z1))
    time.sleep_ms(50)

    x2 = Imu.getGyro()[0]
    y2 = Imu.getGyro()[1]
    z2 = Imu.getGyro()[2]
    print("x2=" + str(x2) + " y2=" + str(y2) + " z2=" + str(z2))
    message = "x2=" + str(x2) + " y2=" + str(y2) + " z2=" + str(z2)
    labelx2.setText("x2=" + str(x2))
    labely2.setText("y2=" + str(y2))
    labelz2.setText("z2=" + str(z2))

    if abs(x1 - x2) > 4.0:
      Speaker.tone(2000, 1000)
    if abs(y1 - y2) > 4.0:
      Speaker.tone(2000, 1000)
    if abs(z1 - z2) > 4.0:
      Speaker.tone(2000, 1000)
      
    time.sleep_ms(50)
  Speaker.stop()
  

if __name__ == '__main__':
  try:
    setup()

    # Gyro sensor task
    gyro_sensor()

  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
