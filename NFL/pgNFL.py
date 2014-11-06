#!/usr/bin/env python
import pygame
import sys,os,time
from pygame.locals import *
import urllib2,time,pdb

white = (255,255,255)
black = (0,0,0)


class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        self.font.set_underline(1)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((320,240), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def getScores(self):
        os.system('/home/pi/scripts/NFLscores.py')
        f = open('/home/pi/scripts/scores.txt','r').readlines()
        current = []
        upcoming = []
        finished = []
        for line in f:
            if line.split()[-1] == 'ET':
                upcoming.append(line)
            elif line.split()[-1] == 'ET' and len(line.split()) <= 9:
                finished.append(line)
            if line.split()[-1] == 'ET' and len(line.split()) > 9:
                current.append(line)
        
        return current, upcoming, finished

    def addText(self):
        imdir = '/home/pi/GitHub/tft/NFL/Images/'
        current, upcoming, finished = self.getScores()
#         pdb.set_trace()
        
        if len(current) == 0 and len(finished) == 0:
            for game in upcoming:
#                 pdb.set_trace()
                away = pygame.image.load(imdir+game.split()[1].lower()+'.bmp')
                home = pygame.image.load(imdir+game.split()[4].lower()+'.bmp')
                self.screen.blit(away,(0,0))
                self.screen.blit(home,(200,0))
#         self.screen.blit(self.font.render('Twitter Trends', True, (255,255,255)), (10, 6))
#         start_line = self.font.size('Twitter Trends')[1]
#         self.font = pygame.font.SysFont('Arial', 17)
#         for i in range(len(trends)):
#             if i < 11:
#                 self.screen.blit(self.font.render(trends[i],True,(255,255,255)),(10,int(start_line)+11))
#                 start_line = start_line + self.font.size(trends[i])[1]
#             else:
#                 print 'hi' 

#         logo = '/home/pi/images/twitterLogo.bmp'
                pygame.display.update()
                time.sleep(5)
                self.screen.fill(white)
                pygame.display.update()
        
#                 pygame.display.flip()

if __name__ == '__main__':
    os.system('/home/pi/scripts/backlighton.sh')
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')
    Pan3 = Pane()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();