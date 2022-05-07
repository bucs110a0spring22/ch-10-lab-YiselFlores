import pygame
import random
from src import hero
#model

class Explosion:
    def __init__(self, x, y, img_file):
        """"sets the rectangle up"""
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def blitty(self, screen):
        """blits rectangle on screen"""
        self.screen = screen
        self.screen.blit(self.image, (self.rect.x,self.rect.y))
        




















#class Explosion:
    #def __init__(self,background,x,y,img_file):
        #initialize all the Sprite functionality
        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen
        #self.image = pygame.image.load(img_file).convert_alpha()
        #self.rect = self.image.get_rect()
        #x = hero.Hero.x 
        #y = hero.Hero.y
        #self.background = background
        #return self.background.blit(img_file, [x,y]) 
        #create surface object image
        #get the rectangle for positioning
        #explosion.spawn(self.screen,"assets/explo.png",)
        

   # def spawn(self, background, image):
     # self.background = background
      #self.image = image
     # return self.background.blit(image, [1, .5]) 
      #
        
       
