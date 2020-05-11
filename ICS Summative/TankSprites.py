import pygame
import random
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       
        
        self.image = pygame.image.load("player_tank.png")
        #self.image.set_colorkey((0, 0, 0)) 
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        self.image_up = pygame.image.load("player_tank.png")
        #self.image_up.set_colorkey((0, 0, 0)) 
        self.image_up = self.image_up.convert()
        
        self.image_up2 = pygame.image.load("player_tank2.png")
        self.image_up = self.image_up.convert()
        
        self.image_down = pygame.image.load("player_tank_down.png")
        #self.image_down.set_colorkey((0, 0, 0)) 
        self.image_down = self.image_down.convert()              
        
        self.image_right = pygame.image.load("player_tank_right.png")
        #self.image_right.set_colorkey((0, 0, 0)) 
        self.image_right = self.image_right.convert()              
        
        self.image_left = pygame.image.load("player_tank_left.png")
        #self.image_left.set_colorkey((0, 0, 0)) 
        self.image_left = self.image_left.convert()              
        
        self.image.set_colorkey((0, 0, 0)) 
        self.flash = 1
        
        self.rect.left = 320
        self.rect.top = 240
        
        self.__dx = 0
        self.__dy = 0
        
    def go_left(self):
        self.image = self.image_left
        self.__dx = -5
        self.__dy = 0
        
    def go_right(self):
        self.image = self.image_right
        self.__dx = 5
        self.__dy = 0
        
    def go_down(self):
        self.image = self.image_down
        self.__dy = 5
        self.__dx = 0
        
    def go_up(self):
        if self.flash == 1:
            self.image = self.image_up
        else:
            self.image = self.image_up2
            
        self.__dy = -5
        self.__dx = 0
        
    def stop_left(self):
        self.rect.left -= self.__dx
        self.rect.top -= self.__dy
        if self.__dx > 0:
            self.rect.left += self.__dx
        if self.__dy > 0:
            self.rect.top += self.__dy
        if self.__dy < 0:
            self.rect.top += self.__dy        
        
    def stop_right(self):
        self.rect.left -= self.__dx
        self.rect.top -= self.__dy
        if self.__dx < 0:
            self.rect.left += self.__dx
        if self.__dy < 0:
            self.rect.top += self.__dy
        if self.__dy > 0:
            self.rect.top += self.__dy
            
    def stop_up(self):
        self.rect.left -= self.__dx
        self.rect.top -= self.__dy
        if self.__dy > 0:
            self.rect.top += self.__dy
        if self.__dx < 0:
            self.rect.left += self.__dx
        if self.__dx > 0:
            self.rect.left += self.__dx
            
    def stop_down(self):
        self.rect.left -= self.__dx
        self.rect.top -= self.__dy
        if self.__dy < 0:
            self.rect.top += self.__dy
        if self.__dx > 0:
            self.rect.left += self.__dx
        if self.__dx < 0:
            self.rect.left += self.__dx
        

        
        
    def update(self):
        if self.flash == 1:
            self.flash = 2
        else:
            self.flash = 1
        self.image.set_colorkey((0, 0, 0)) 
        self.rect.left += self.__dx
        self.rect.top += self.__dy
        
        
class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("brick.png")
        self.image.convert()
        
        self.rect = self.image.get_rect()
        self.rect.left = row * 40
        self.rect.top = col * 40
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((5,5))
        self.image.convert()
        self.flash = 1
        self.rect = self.image.get_rect()
        self.__dy = 1
        self.__dx = 1
        
    def shoot_up(self):
        self.__dy = -self.__dy
        self.__dx = 0
        
    def shoot_down(self):
        self.__dy = self.__dy
        self.__dx = 0
        
    def shoot_right(self):
        self.__dx = self.__dx
        self.__dy = 0
        
    def shoot_left(self):
        self.__dx = -self.__dx
        self.__dy = 0
        
    def shoot_upright(self):
        self.__dy = 1
        self.__dx = 1
        
    def shoot_enemy(self, playerx, playery, enemyx, enemyy):
        slopey = playery - enemyy
        slopex = playerx - enemyx
        distance = float(math.sqrt(pow(slopex, 2) + pow(slopey, 2)))
        steps = self.__distance / 7 
        self.__dx = slopex / steps
        self.__dy = slopey / steps
        
        
        #distance = float(math.hypo(slopex, slopey))
        #self.__dx = slopex / float(distance)
        #self.__dy = slopey / float(distance)
        
    def update(self):
        if self.flash == 1:
            self.image = pygame.Surface((5,5))
            self.image.fill((255, 0, 0))
            self.image.convert()
            self.flash = 2
        else:
            self.image = pygame.Surface((5,5))
            self.image.fill((0, 0, 0))
            self.image.convert()    
            self.flash = 1          
        self.rect.centery += self.__dy * 7
        self.rect.centerx += self.__dx * 7
        
class Bullet2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill((255, 0, 0))
        self.image.convert()        
        self.flash = 1
        self.rect = self.image.get_rect()
        self.__dy = 5
        self.__dx = 5
        
        
    def shoot_enemy(self, playerx, playery, enemyx, enemyy):
        slopey = playery - enemyy
        slopex = playerx - enemyx
        distance = math.hypot(slopex, slopey)
        self.__dx = slopex / distance
        self.__dy = slopey / distance  
        
    def update(self):
        self.rect.centery += (self.__dy * 5)
        self.rect.centerx += (self.__dx * 5  )  
        if self.flash == 1:
            self.image = pygame.Surface((5,5))
            self.image.fill((255, 0, 0))
            self.image.convert()
            self.flash = 2
        else:
            self.image = pygame.Surface((5,5))
            self.image.fill((0, 0, 0))
            self.image.convert()    
            self.flash = 1        
                   
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, col, row):
        pygame.sprite.Sprite.__init__(self)
        self.col = col
        self.row = row
        self.image = pygame.image.load("enemy_shooter.png") 
        self.image = self.image.convert()
        
        self.image_up = pygame.image.load("enemy_shooter_up.png")
        self.image_up = self.image_up.convert()
    
        self.rect = self.image.get_rect()
        self.rect.left = self.row * 40
        self.rect.bottom = self.col * 40
        self.__dx = 0
        self.__dy = -5
        
        self.image.set_colorkey((0, 0, 0))
        
        
    def go_left(self):
        self.image = pygame.image.load("enemy_shooter_up.png")
        self.image = self.image.convert()
        self.__dx = -5
        self.__dy = 0
        
    def go_up(self):
        self.image = pygame.image.load("enemy_shooter.png")
        self.image = self.image.convert()
        self.__dx = 0
        self.__dy = -5
        
    def go_down(self):
        self.image = pygame.image.load("enemy_shooter_left.png")
        self.image = self.image.convert()
        self.__dy = 5
        self.__dx = 0
        
    def go_right(self):
        self.image = pygame.image.load("enemy_shooter_down.png")
        self.image = self.image.convert()
        self.__dy = 0
        self.__dx = 5
 
            
        
    def reset(self, col, row):
        """
        if lottery == 1:
            print "1"
            self.rect.left = 8 * 40
            self.rect.top = 12 * 40                  
            self.__dx = 0
            self.__dy = -5
        if lottery == 2:
            print "2"
            self.rect.left = -1 * 40
            self.rect.top = 5 * 40                  
            self.__dy = 0
            self.__dx = 5
        if lottery == 3:
            print "3"
            self.rect.left = 8 * 40
            self.rect.top = -1 * 40                  
            self.__dy = 5
            self.__dx = 0
        if lottery == 4:
            print "4"
            self.rect.left = 18 * 40
            self.rect.top = 5 * 40                  
            self.__dx = -5
            self.__dy = 0
        """
        self.rect.left = row * 40
        self.rect.top = col * 40      
        
    def update(self):
        self.image.set_colorkey((0, 0, 0))
        self.rect.left += self.__dx
        self.rect.bottom += self.__dy
    
        """if self.flash == 1:
            self.image = pygame.image.load("alien1.png")
            self.image.convert()
            self.flash = 2
        else:
            self.image = pygame.image.load("alien2.png")
            self.image.convert()    
            self.flash = 1        
        self.image.set_colorkey((255, 255, 255))
        """
        
class Runner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((20,20))
        self.image.fill((0, 255, 0))
        self.image.convert()
        self.rect = self.image.get_rect()
        
        self.rect.left = -2 * 40
        self.rect.bottom = -2 * 40        
        
        self.__dx = 0
        self.__dy = 0
        
    def go_left(self):
        self.__dx = -5
        self.__dy = 0
               
    def go_up(self):
        self.__dx = 0
        self.__dy = -5
               
    def go_down(self):
        self.__dy = 5
        self.__dx = 0
               
    def go_right(self):
        self.__dy = 0
        self.__dx = 5    
        
    def reset(self, col, row):
        self.rect.left = row * 40
        self.rect.top = col * 40   

    def update(self):
        self.rect.centerx += self.__dx
        self.rect.centery += self.__dy
        
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.Font("mario_font.ttf", 15)
        self.__score = 0
        self.__armor = 100
        self.__ammo = 20
         
    def scored(self):
        '''This method adds one to the score for player 1'''
        self.__score += 1
        
    def get_score(self):
        return self.__score
 
    def lose_armor(self):
        '''This method adds one to the score for player 1'''
        self.__armor -= 1
        
    def lose_ammo(self):
        self.__ammo -= 1
        
    def reset_ammo(self):
        self.__ammo = 20
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        
        message = "Score: %d   Armor: %d   Ammo: %d" %\
                (self.__score, self.__armor, self.__ammo)
        
        message2 = "Score: %d   Armor: %d   Ammo: Reloading" %\
                    (self.__score, self.__armor) 
        
        if self.__ammo == 0:
            self.image = self.__font.render(message2, 1, (0, 0, 0))
        else:
            self.image = self.__font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (330, 240)
                  
                  
class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, runnerx, runnery, version):
        pygame.sprite.Sprite.__init__(self)
        self.version = version
        self.frame = 1
        #print "inner_frame:" + str(self.frame)
        self.explosion = []
        for image in range(1, 22):
            self.explosion.append("poof_" + str(image) + ".png")
            
        self.explosion2 = []
        for image in range(0, 33):
            self.explosion2.append(str(image) + ".png")        
            
        self.image = pygame.image.load(self.explosion[self.frame])
        self.rect = self.image.get_rect()
        
        self.rect.centerx = runnerx 
        self.rect.centery = runnery 
        
    def update(self): 
        if self.version == 1:
            if self.frame <= 20:
                self.image = pygame.image.load(self.explosion[self.frame])
                self.frame += 1
            else:
                self.frame = 1
                self.kill()
        if self.version == 2:
            if self.frame <= 32:
                self.image = pygame.image.load(self.explosion2[self.frame])
                self.frame += 1
            else:
                self.frame = 1
                self.kill()
               
        