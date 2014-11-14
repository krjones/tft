#!/usr/bin/env python

from pitftscreen import PiTFT_Screen
import sys,os,time,pdb



def initialize():
	global pitft
	global dir
	dir = '/home/pi/tft/'
	os.chdir(dir)
	pitft = PiTFT_Screen()

def checkArgLen():
	if len(sys.argv) < 2:
		print "Please use at leaset one or more argument(s)."
		print "Arguments can be run as multiples in sequence"
		print "Usage: sudo ./tft.py [on] [off] [black] [red]"
		print "[green] [lastsnap] [lastdet] [wx]"
		sys.exit()

def reset():
	black()
	os.system('sudo pkill fbi')
	off()
def on():
	print 'Screen On'
	pitft.Backlight(True)

def off():
	print 'Screen Off'
	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a black-wallpaper-HD.jpg')
	pitft.Backlight(False)
	
def black():
	print 'Screen Black'
	os.system('fbi -T 2 -d /dev/fb1 -noverbose black.jpg')
	
def red():
	print 'Screen Red'
	os.system('fbi -T 2 -d /dev/fb1 -noverbose red.jpg')

def green():
	print 'Screen Green'
	os.system('fbi -T 2 -d /dev/fb1 -noverbose green.jpg')
	time.sleep(10)
	pitft.Backlight(False)	
	
def lastsnap():
	on()
	os.system('scp -r pi@192.168.0.40:/home/pi/motion/lastsnap.jpg /home/pi/tft/temp/')
	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a /home/pi/tft/temp/lastsnap.jpg')
	
def lastdet():
	on()
	os.system('scp -r pi@192.168.0.40:/home/pi/motion/lastdet.jpg /home/pi/tft/temp/')
	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a /home/pi/tft/temp/lastdet.jpg')

def wx():
	os.system('/home/pi/scripts/ModifiedFiles/RPI/weather-script.sh')
	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a /home/pi/tft/wx-current.png')
	time.sleep(20)
#	os.chdir(dir+'wx/images')
# 	print 'Downloading WX Images'
# 	os.system('wget http://192.168.0.40/weewx/daytempdew.png')
# 	os.system('wget http://192.168.0.40/weewx/daytempchill.png')
# 	os.system('wget http://192.168.0.40/weewx/.png')
# 	os.system('wget http://192.168.0.40/weewx/daybarometer.png')
# 	os.system('wget http://192.168.0.40/weewx/daywinddir.png')
# 	os.system('wget http://192.168.0.40/weewx/dayinside.png')
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daytempdew.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daytempchill.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daytempdew.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daywind.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daybarometer.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a daywinddir.png')
# 	time.sleep(5)
# 	os.system('fbi -T 2 -d /dev/fb1 -noverbose -a dayinside.png')
# 	time.sleep(5)
# 	os.chdir(dir)
	

def runArgs():
	for i in sys.argv[1:]:
		if i == 'on':
			reset()
			on()
		elif i == 'off':
			reset()
			off()
		elif i == 'black':
			black()
			reset()
		elif i == 'red':
			red()
			reset()
		elif i == 'green':
			green()
			reset()		
		elif i == 'lastsnap':
			reset()
			lastsnap()
			time.sleep(20)
			reset()
		elif i == 'lastdet':
			reset()
			lastdet()
			time.sleep(20)
			reset()
		elif i == 'wx':
			wx()
			reset()
		else:
			print 'Input "'+ i +'" Not Recognized...Ignoring...'

def main():
	initialize()
	checkArgLen()
	runArgs()
	
main()



#convert black.jpg    -resize 320x240\!  test.gif
