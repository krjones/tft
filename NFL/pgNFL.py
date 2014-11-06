#!/usr/bin/env python
import pygame
import sys,os
from pygame.locals import *
import urllib2,time

white = (255,255,255)
black = (0,0,0)


class Pane(object):
	def getScores():
		os.system('/home/pi/scripts/NFLscores.py')
		f = open('/home/pi/scripts/scores.txt','r').readlines()
		current = []
		upcoming = []
		finished = []
		for line in f:
			if len(line.split()) <= 9:
				finished.append(line)
			if len(line.split()) > 9:
				current.append(line)
			if line.split()[-1] == 'ET'
				upcoming.append(line)
		
		return current, upcoming, finished
		
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
	self.font.set_underline(1)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((320,240), 0, 32)
        self.screen.fill((black))
        pygame.display.update()

    def addText(self):
        f = urllib2.urlopen('http://192.168.0.40/twitter/total_trends.html').readlines()
        short_list = f[0].split("#000000'>")[1:11]
        trends = []
        for line in short_list:
            trends.append(line.split('</a>')[0])

        self.screen.blit(self.font.render('Twitter Trends', True, (255,255,255)), (10, 6))
        start_line = self.font.size('Twitter Trends')[1]
	self.font = pygame.font.SysFont('Arial', 17)
        for i in range(len(trends)):
            if i < 11:
                self.screen.blit(self.font.render(trends[i],True,(255,255,255)),(10,int(start_line)+11))
                start_line = start_line + self.font.size(trends[i])[1]
            else:
                print 'hi' 

        logo = '/home/pi/images/twitterLogo.bmp'
        img=pygame.image.load(logo) 
        self.screen.blit(img,(225,5))
        pygame.display.update()
        
        
        pygame.display.flip()

if __name__ == '__main__':
    os.system('/home/pi/scripts/backlighton.sh')
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')
    Pan3 = Pane()
    current, upcoming, finished = getScores()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();