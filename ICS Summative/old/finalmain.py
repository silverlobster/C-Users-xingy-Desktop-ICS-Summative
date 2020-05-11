import finalsprites
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))


def main():
   '''This function defines the 'mainline logic' for our game.'''
    
   # Display
   pygame.display.set_caption("Final Stand")
     
   # Entities
   background = pygame.Surface(screen.get_size())
   background.fill((255, 255, 255))
   screen.blit(background, (0, 0))
   
   allSprites= pygame.sprite.Group()
   bullet_list = pygame.sprite.Group()
   gunner = finalsprites.Gunner()
   #bullet = finalsprites.Bullet() 
   allSprites.add(gunner)
   
   
     
   # ACTION
     
   # Assign 
   keepGoing = True
   clock = pygame.time.Clock()
    
   # Loop
   while keepGoing:
     
      # Time
      clock.tick(30)
     
      # Events
      for event in pygame.event.get():
         
         if event.type == pygame.QUIT:
            keepGoing = False
         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               gunner.go_left()
            if event.key == pygame.K_RIGHT:
               gunner.go_right()
            if event.key == pygame.K_UP:
               gunner.go_up()
            if event.key == pygame.K_DOWN:
               gunner.go_down()
            if event.key == pygame.K_w:
               bullet = finalsprites.Bullet() 
               bullet.rect.x = gunner.rect.x
               bullet.rect.y = gunner.rect.y
               allSprites.add(bullet)
               bullet_list.add(bullet)
               
         
      # Refresh screen
      allSprites.clear(screen, background)
      allSprites.update()
      allSprites.draw(screen)
         
      pygame.display.flip()
 
   # Close the game window
   pygame.quit()     
       
# Call the main function

main()   