#!/usr/bin/env python

from pitftscreen import PiTFT_Screen
import sys,os,time,pdb

os.chdir('/home/pi/tft')

pitft = PiTFT_Screen()

if len(sys.argv) >= 2:
	for i in sys.argv[1:]:
		if i == 'on':
			print 'Screen On'
			pitft.Backlight(True)
		if i == 'off':
			print 'Screen Off'
			os.system('fbi -T 2 -d /dev/fb1 -noverbose -a black-wallpaper-HD.jpg')
			pitft.Backlight(False)
		if i == 'reset':
			print 'Screen Reset'
			pitft = PiTFT_Screen()
		if i == 'black':
			print 'Screen Black'
			os.system('fbi -T 2 -d /dev/fb1 -noverbose black.jpg')
		if i == 'red':
			print 'Screen Red'
			os.system('fbi -T 2 -d /dev/fb1 -noverbose red.jpg')
		if i == 'green':
			print 'Screen Green'
			os.system('fbi -T 2 -d /dev/fb1 -noverbose green.jpg')
			time.sleep(10)
			pitft.Backlight(False)			
		if i == 'lastsnap':
			os.system('scp -r pi@192.168.0.40:/home/pi/motion/lastsnap.jpg /home/pi/tft/temp/')
			os.system('fbi -T 2 -d /dev/fb1 -noverbose -a /home/pi/tft/temp/lastsnap.jpg')
		if i == 'lastdet':
			os.system('scp -r pi@192.168.0.40:/home/pi/motion/lastdet.jpg /home/pi/tft/temp/')
			os.system('fbi -T 2 -d /dev/fb1 -noverbose -a /home/pi/tft/temp/lastdet.jpg')





#convert black.jpg    -resize 320x240\!  test.gif
