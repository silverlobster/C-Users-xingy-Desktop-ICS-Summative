import pygame
pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.centery -= 5

class Gunner(pygame.sprite.Sprite):
    '''Our Box class inherits from the Sprite class'''
    def __init__(self):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Set the image attribute for our Box sprite
        self.image = pygame.image.load("pacman-right.gif")
        self.image = self.image.convert()
         
        # Set the rect attribute for our Box sprite
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 200
        self.__directionx = 0
        self.__directiony = 5
    
        
        
        
    def go_left(self):
        self.image = pygame.image.load("pacman-left.gif")
        self.image = self.image.convert()
        self.__directionx = -5
        self.__directiony = 0
        
    def go_right(self):
        self.image = pygame.image.load("pacman-right.gif")
        self.image = self.image.convert()
        self.__directionx = 5
        self.__directiony = 0
        
    def go_up(self):
        self.image = pygame.image.load("pacman-up.gif")
        self.image = self.image.convert()
        self.__directiony = -5
        self.__directionx = 0
        
    def go_down(self):
        self.image = pygame.image.load("pacman-down.gif")
        self.image = self.image.convert()
        self.__directiony = 5
        self.__directionx = 0
 
    def update(self):
        
        self.rect.left += self.__directionx
        self.rect.top += self.__directiony
        
        if (self.rect.left > 640):
            self.rect.left = 0
            
        if (self.rect.left < 0):
            self.rect.right = 640
            
        if (self.rect.top < 0):
            self.rect.top = 480
            
        if (self.rect.top > 480):
            self.rect.top = 0
            
    