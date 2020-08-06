import pygame
from pygame.locals import *
import sys
import time
import random

class Game:
    def __init__(self):

        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % wpm:0'
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)

        pygame.init()
        self.open_img = pygame.image.load('typing-speed_open.jpg')
        self.open_img = pygame.transform.scale(self.open_img,(self.w,self.h))

        self.bg = pygame.image.load('background.png')
        self.bg = pygame.transform.scale(self.bg, (500,750))

        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Typing Speed Test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.reader(msg,1, color)
        text_rect = text.grt_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()
    def get_sentence(self):
        with open('sentences.txt','r') as f:
            sentences = f.split('\n')
            sentence = random.choice(sentences)
            return sentence
    def show_results(self, screen):
        if(not self.end):
            # clculate time
            self.ttal_time = time.time() - self.time_start

            # claculate accuracy
            count = 0
            for i,c in enumerate(self.world):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.world)*100

            # calculate words per minute
            self.wpa = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time: '+str(round(self.total_time)) +'secs Accuracy: '+ str(round(self.accuracy))+'%'+' wpa : '+str(round(self.wpa))

            # draw icon image
        self.time_img = pygame.image.load('icon.png')
        self.time_img = pygame.transform.scale(self.time_img, (150,150))
        #screen.blit(self.time_img, (80,320))
        screen.blit(self.time_img, (self.w/2-75,self.h-140))
        self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100))
        print(self.results)
        pygame.display.update()
