import pygame, TankSprites, random
pygame.init()
screen = pygame.display.set_mode((680, 480))

def main():
    background = pygame.Surface(screen.get_size())
    #background = pygame.image.load("blackwhite.png")
    background = background.convert()
    background.fill((195, 195 , 195))
    screen.blit(background, (0, 0))
    
    enemy = TankSprites.Enemy(12, 8)
    bullet = TankSprites.Bullet()
    bullet2 = TankSprites.Bullet2()
    player = TankSprites.Player()
    score = TankSprites.ScoreKeeper()
    runner = TankSprites.Runner()
    explosion = TankSprites.Explosion(runner.rect.centerx, runner.rect.centery, 1)
    
    bricks_top = []
    bricks_right = []
    bricks_down = []
    bricks_left = []
    
    bottom_row = pygame.sprite.Group()
    top_row = pygame.sprite.Group()
    right_col = pygame.sprite.Group()
    left_col = pygame.sprite.Group()
    bulletsGroup = pygame.sprite.Group()
    bulletsGroup2 = pygame.sprite.Group()
    runnerGroup = pygame.sprite.Group()
    explosionGroup = pygame.sprite.Group()

    for row in range(17):
        bricks_top.append(TankSprites.Brick(row, 0))
        top_row.add(bricks_top)
        
    for col in range(12):
        bricks_left.append(TankSprites.Brick(0,col))
        #brick = TankSprites.Brick(0, col)
        left_col.add(bricks_left)
        
    for row in range(17):
        bricks_down.append(TankSprites.Brick(row, 11))
        #brick = TankSprites.Brick(row, 11)
        bottom_row.add(bricks_down)

    for col in range(12):
        bricks_right.append(TankSprites.Brick(16, col))
        #brick = TankSprites.Brick(16, col)
        right_col.add(bricks_right)
        
    del bricks_top[8]
    del bricks_left[5]
    del bricks_right[5]
    del bricks_down[8]
    
    enemyGroup = pygame.sprite.Group(enemy)
    bricksGroup = pygame.sprite.Group(bricks_top, bricks_left, bricks_down, bricks_right)
    allSprites = pygame.sprite.Group(player, bricksGroup, bulletsGroup, bulletsGroup2, enemyGroup, score, explosionGroup)
    
    
    clock = pygame.time.Clock()
    keepGoing = True
    points = 1
    ammo = 20
    time = 0  
    check = 1
    while keepGoing:
            
               # TIME
        clock.tick(30)
        lottery = random.randrange(1,5)
        attack = random.randrange(1, 150)
        spawn = random.randrange(0,50)
               # EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.JOYHATMOTION:
                player1.change_direction(event.value)
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                    
                if ammo > 0:
                    if event.key == pygame.K_w:
                        bullet = TankSprites.Bullet()
                        bullet.rect.centerx = player.rect.centerx
                        bullet.rect.centery = player.rect.centery
                        bullet.shoot_up()
                        allSprites.add(bullet)
                        bulletsGroup.add(bullet)
                        ammo -= 1
                        score.lose_ammo()
                        
                    if event.key == pygame.K_s:
                        bullet = TankSprites.Bullet()
                        bullet.rect.centerx = player.rect.centerx
                        bullet.rect.centery = player.rect.centery
                        bullet.shoot_down()
                        allSprites.add(bullet)
                        bulletsGroup.add(bullet)
                        ammo -= 1
                        score.lose_ammo()
                        
                    if event.key == pygame.K_d:
                        bullet = TankSprites.Bullet()
                        bullet.rect.centerx = player.rect.centerx
                        bullet.rect.centery = player.rect.centery
                        bullet.shoot_right()
                        allSprites.add(bullet)
                        bulletsGroup.add(bullet)
                        ammo -= 1
                        score.lose_ammo()
                        
                    if event.key == pygame.K_a:
                        bullet = TankSprites.Bullet()
                        bullet.rect.centerx = player.rect.centerx
                        bullet.rect.centery = player.rect.centery
                        bullet.shoot_left()
                        allSprites.add(bullet)
                        bulletsGroup.add(bullet)
                        ammo -= 1
                        score.lose_ammo()
                        
            if ammo == 0:
                #print "time:" + str(time)
                time += 1
            if time == 20:
                score.reset_ammo()
                ammo = 20
                time = 0
                            
                        
        hit_list = pygame.sprite.spritecollide(player, bricksGroup, False)  
        
        if pygame.sprite.spritecollide(player, top_row, False):
            player.stop_up()     
        if pygame.sprite.spritecollide(player, left_col, False):
            player.stop_left()        
        if pygame.sprite.spritecollide(player, bottom_row, False):
            player.stop_down()            
        if pygame.sprite.spritecollide(player, right_col, False):
            player.stop_right()
        
        pygame.sprite.spritecollide(player, bricksGroup, False)  
            
        for bullet in bulletsGroup:  
            if pygame.sprite.spritecollide(bullet, bricksGroup, False):
                bulletsGroup.remove(bullet)
                allSprites.remove(bullet)
        for bullet2 in bulletsGroup2:
            if pygame.sprite.spritecollide(bullet2, bricksGroup, False):
                bulletsGroup2.remove(bullet2)
                allSprites.remove(bullet2)
        for bullet2 in bulletsGroup2:
            if pygame.sprite.spritecollide(bullet2, runnerGroup, False):
                bulletsGroup2.remove(bullet2)
                allSprites.remove(bullet2)                
                
        for enemy in enemyGroup:
            if enemy.rect.bottom == (11 * 40) and enemy.rect.left == (8 * 40):
                enemy.go_left()
        
            if enemy.rect.top == (5 * 40) and enemy.rect.left == (1 * 40):
                enemy.go_up()
        
            if enemy.rect.top == (1 * 40) and enemy.rect.left == (8 * 40):
                enemy.go_right()    
        
            if enemy.rect.top == (5 * 40) and enemy.rect.right == (16 * 40):
                enemy.go_down()        
            
            if enemy.rect.bottom == (11 * 40) and enemy.rect.left == (1 * 40):
                enemy.go_up()
            
            if enemy.rect.top == (1 * 40) and enemy.rect.left == (1 * 40):
                enemy.go_right()  
            
            if enemy.rect.top == (1 * 40) and enemy.rect.right == (16 * 40):
                enemy.go_down()
            
            if enemy.rect.bottom == (11 * 40) and enemy.rect.right == (16 * 40):
                enemy.go_left()
        
        first = 1
        for bullet in bulletsGroup:    
            enemy_hit = pygame.sprite.spritecollide(bullet, enemyGroup, False)
            for enemy in enemyGroup:
                for enemy in enemy_hit:
                    bulletsGroup.remove(bullet)
                    allSprites.remove(bullet)
                    if lottery == 1:
                        enemy.reset(12, 8)
                        enemy.go_up()
                    if lottery == 2:
                        enemy.reset(5, -1)
                        enemy.go_right()
                    if lottery == 3:
                        enemy.reset(-1, 8)
                        enemy.go_down()
                    if lottery == 4:
                        enemy.reset(5, 18)
                        enemy.go_left()                    
                    #enemy.reset(lottery)
                    if first == 1:
                        score.scored()
                        first = 2
                        
        for bullet2 in bulletsGroup2:
            if player.rect.colliderect(bullet2):
            #if pygame.sprite.spritecollide(player, bullet2, False):
                score.lose_armor()
                bulletsGroup2.remove(bullet2)
                allSprites.remove(bullet2)
                
                        
        for enemy in enemyGroup:
            if player.rect.colliderect(enemy):
                explosion = TankSprites.Explosion(enemy.rect.centerx + 10, enemy.rect.centery + 10, 2)
                explosionGroup.add(explosion)
                allSprites.add(explosion)                
                score.scored()
                score.lose_armor()
                if lottery == 1:
                    enemy.reset(12, 8)
                    enemy.go_up()
                if lottery == 2:
                    enemy.reset(5, -1)
                    enemy.go_right()
                if lottery == 3:
                    enemy.reset(-1, 8)
                    enemy.go_down()
                if lottery == 4:
                    enemy.reset(5, 18)
                    enemy.go_left()                    
                    #enemy.reset(lottery)
                    
        first2 = 1
        for bullet in bulletsGroup:
            runner_hit = pygame.sprite.spritecollide(bullet, runnerGroup, False)
            for runner in runner_hit:
                bulletsGroup.remove(bullet)
                allSprites.remove(bullet)
                runner.kill()
                if first2 == 1:
                    score.scored()
                    first = 2                    
    
    
        for runner in runnerGroup:
            if player.rect.colliderect(runner):
                explosion = TankSprites.Explosion(runner.rect.centerx, runner.rect.centery, 1)
                explosionGroup.add(explosion)
                allSprites.add(explosion)
                score.scored()
                score.lose_armor()
                if lottery == 4:
                    runner.reset(5, -1)
                    runner.go_right()
                if lottery == 3:
                    runner.reset(12, 8)
                    runner.go_up()
                if lottery == 2:
                    runner.reset(-1, 8)
                    runner.go_down()
                if lottery == 1:
                    runner.reset(5, 18)
                    runner.go_left()                  
    
        once = 1
        if once == 1:
            if score.get_score() == points:
                print("check" + str(check))
                check += 1
                enemy = TankSprites.Enemy(12, 8)
                enemyGroup.add(enemy)
                allSprites.add(enemy)
                if lottery == 1:
                    enemy.reset(5, -1)
                    enemy.go_right()
                if lottery == 2:
                    enemy.reset(12, 8)
                    enemy.go_up()
                if lottery == 4:
                    enemy.reset(-1, 8)
                    enemy.go_down()
                if lottery == 3:
                    enemy.reset(5, 18)
                    enemy.go_left()
                points += 10
                #enemy.reset(lottery)
                once = 2
        
            
        #for enemy in enemyGroup:
        if attack == 13:
            for enemy in enemyGroup:
                bullet2 = TankSprites.Bullet2()
                bullet2.rect.centerx = enemy.rect.centerx
                bullet2.rect.centery = enemy.rect.centery
                bullet2.shoot_enemy(player.rect.centerx, player.rect.centery, enemy.rect.centerx, enemy.rect.centery)
                allSprites.add(bullet2)
                bulletsGroup2.add(bullet2)            
        
        if spawn == 15:
            runner = TankSprites.Runner()
            runnerGroup.add(runner)
            allSprites.add(runner)                
            if lottery == 4:
                runner.reset(5, -1)
                runner.go_right()
            if lottery == 3:
                runner.reset(12, 8)
                runner.go_up()
            if lottery == 2:
                runner.reset(-1, 8)
                runner.go_down()
            if lottery == 1:
                runner.reset(5, 18)
                runner.go_left()            
                            
               # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
                
        
           # Close the game window
    pygame.quit()     
            
       # Call the main function
main()        