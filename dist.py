import VL53L1X
import time
import datetime
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (1024,768)
#camera.start_preview()

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()
tof.start_ranging(3) #1 short 2 medium 3 long
setDist = tof.get_distance()
setDist = setDist/25.4

count = 1
while True:	
	now = datetime.datetime.now()
	distance_in_mm = tof.get_distance() #in mm
	inches = distance_in_mm/25.4
	print inches
	
	if inches <= setDist-6:
		count = count + 1
		
		camera.capture('piSec/%s.jpg' %str(now) )
		print "pic"
		time.sleep(3)
		
	
tof.stop_ranging()

