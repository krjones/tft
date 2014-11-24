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
        self.font = pygame.font.SysFont('Arial', 30)
#         self.font.set_underline(1)
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
            elif line.split()[-1] == 'OT' or line.split()[-1] == 'Final':
                finished.append(line)
            else:
                current.append(line)
#         pdb.set_trace()
#         global current,upcoming,finished
        return current, upcoming, finished


        
    def upComing(self,upcoming):
        adj = 160 - (self.font.size('Upcoming Games')[0]/2)
        self.screen.blit(self.font.render('Upcoming Games', True, black), (adj, 40))
        adjx = 160 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        adjy = 120 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        self.screen.blit(pygame.image.load(imdir+'nfl.bmp'),(adjx,adjy))
        pygame.display.update()
        time.sleep(2)
        self.screen.fill(white)
        pygame.display.update()
        for game in upcoming:
            away = pygame.image.load(imdir+game.split()[1].lower()+'.bmp')
            home = pygame.image.load(imdir+game.split()[4].lower()+'.bmp')
            self.screen.blit(away,(0,120-(pygame.Surface.get_size(away)[1]/2)))
            self.screen.blit(home,(320-pygame.Surface.get_size(home)[0],120-(pygame.Surface.get_size(home)[1]/2)))
            self.font = pygame.font.SysFont('Arial', 36)
            adjTx = 160 - (self.font.size(game.split()[5])[0]/2)
            adjTy = (self.font.size(game.split()[5])[1]/2)
            self.screen.blit(self.font.render(game.split()[5], True, black), (adjTx, 120-adjTy))
            adjTx = 160 - (self.font.size(game.split()[6]+' '+game.split()[7])[0]/2)
            adjTy = (self.font.size(game.split()[6]+' '+game.split()[7])[1]/2)
            self.screen.blit(self.font.render(game.split()[6]+' '+game.split()[7], True, black), (adjTx, 120+adjTy))
            pygame.display.update()
            time.sleep(5)
            self.screen.fill(white)
            pygame.display.update()

    def cur(self,current):
        adj = 160 - (self.font.size('Current Games')[0]/2)
        self.screen.blit(self.font.render('Current Games', True, black), (adj, 40))
        adjx = 160 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        adjy = 120 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        self.screen.blit(pygame.image.load(imdir+'nfl.bmp'),(adjx,adjy))
        pygame.display.update()
        time.sleep(2)
        self.screen.fill(white)
        pygame.display.update()
        for game in current:
            away = pygame.image.load(imdir+game.split()[1].lower()+'.bmp')
            home = pygame.image.load(imdir+game.split()[5].lower()+'.bmp')
            self.screen.blit(away,(0,120-(pygame.Surface.get_size(away)[1]/2)-40))
            self.screen.blit(home,(320-pygame.Surface.get_size(home)[0],120-(pygame.Surface.get_size(home)[1]/2)-40))
            self.font = pygame.font.SysFont('Arial', 36)
            #away Score
            self.screen.blit(self.font.render(game.split()[2], True, black), (40, 135))
            #home score
            self.screen.blit(self.font.render(game.split()[6], True, black), (260, 135))
            if game.split()[-1] == 'Half':
                # Time
                adjTy = (self.font.size(game.split()[-1]+' '+game.split()[7])[1]/2)-40
                adjTx = 160 - (self.font.size(game.split()[-1])[0]/2)
                self.screen.blit(self.font.render(game.split()[-1], True, black), (adjTx, 120+adjTy))
            else:
                # Time
                adjTx = 160 - (self.font.size(game.split()[7])[0]/2)
                adjTy = (self.font.size(game.split()[6]+' '+game.split()[7])[1]/2)-40
                self.screen.blit(self.font.render(game.split()[7], True, black), (adjTx, 120+adjTy))
                # Quarter
                adjTx = 160 - (self.font.size(game.split()[10])[0]/2)
                self.screen.blit(self.font.render(game.split()[10], True, black), (adjTx, 120+adjTy+40))
            pygame.display.update()
            time.sleep(5)
            self.screen.fill(white)
            pygame.display.update()

    def fin(self,finished):
        adj = 160 - (self.font.size('Final Scores')[0]/2)
        self.screen.blit(self.font.render('Final Scores', True, black), (adj, 40))
        adjx = 160 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        adjy = 120 - (pygame.Surface.get_size(pygame.image.load(imdir+'nfl.bmp'))[0]/2)
        self.screen.blit(pygame.image.load(imdir+'nfl.bmp'),(adjx,adjy))
        pygame.display.update()
        time.sleep(2)
        self.screen.fill(white)
        pygame.display.update()
        for game in finished:
            away = pygame.image.load(imdir+game.split()[1].lower()+'.bmp')
            home = pygame.image.load(imdir+game.split()[5].lower()+'.bmp')
            self.screen.blit(away,(0,120-(pygame.Surface.get_size(away)[1]/2)-40))
            self.screen.blit(home,(320-pygame.Surface.get_size(home)[0],120-(pygame.Surface.get_size(home)[1]/2)-40))
            self.font = pygame.font.SysFont('Arial', 46)
            #away Score
            self.screen.blit(self.font.render(game.split()[2], True, black), (40, 135))
            #home score
            self.screen.blit(self.font.render(game.split()[6], True, black), (260, 135))
            self.font = pygame.font.SysFont('Arial', 36)
            adjTx = 160 - (self.font.size(game.split()[7])[0]/2)
            adjTy = (self.font.size(game.split()[7])[1]/2)-40
            self.screen.blit(self.font.render(game.split()[7], True, black), (adjTx, 120+adjTy))
            pygame.display.update()
            time.sleep(5)
            self.screen.fill(white)
            pygame.display.update()
#         pdb.set_trace()
        
    def run(self,current,upcoming,finished):
        if len(current) == 0 and len(finished) == 0:
            self.upComing(upcoming)
        if len(current) == 0 and len(finished) !=0:
            self.fin(finished)
            self.upComing(upcoming)
        if len(current) != 0 and len(finished) == 0:
            self.cur(current)
            self.upComing(upcoming)
        if len(current) != 0 and len(finished) != 0:
            self.cur(current)
            self.fin(finished)
            self.upComing(upcoming)
        
    def addText(self):
        global imdir
        imdir = '/home/pi/GitHub/tft/NFL/Images/'
        current, upcoming, finished = self.getScores()
        self.run(current,upcoming,finished)
#         pdb.set_trace()        
#                 pygame.display.flip()

if __name__ == '__main__':
    os.system('/home/pi/scripts/backlighton.sh')
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.putenv('SDL_MOUSEDEV' , '/dev/input/touchscreen')
    Pan3 = Pane()
    Pan3.addText()
    os.system('/home/pi/scripts/backlightoff.sh')
    pygame.quit(); sys.exit();
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit(); sys.exit();