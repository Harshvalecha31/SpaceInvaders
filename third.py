import pygame
import random
import csv
pygame.init()

# dataset values
p_x = 0
p_y = 0
e_x = 0
e_y = 0
hit = 0
file = open('mydata2.csv','a')
writer = csv.writer(file)
#writer.writerow(['player x','player y','enemy x','enemy y','enemy left','enemy right','hit'])

def data_reset():
    global p_x,p_y,e_x,e_y,e_left,e_right,hit
    p_x,p_y,e_x,e_y,e_left,e_right,hit = 0,0,0,0,0,0,0
    


# window config
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Space invadors')

# setting icon
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# player display settings
plyer = pygame.image.load('spaceship.png')

plyer_x = 225
plyer_y = 380

# player movement coordinates
left = False
right = False
up = False
down = False

def player(x,y):
    win.fill((255,255,255))
    win.blit(plyer,(x,y))


# score Count
score = 0

# font settings
font = pygame.font.Font(pygame.font.get_default_font(), 18)
def scorer(score):
    text_surface = font.render('Score:'+str(score), True, (0, 0, 0))
    return text_surface

    
# enemy display settings
anyme = pygame.image.load('enemy2.png')
enemy_x = random.randint(0,436)
enemy_y = random.randint(0,100)
enemy_alive = True

def enemy(x,y):
    win.blit(anyme,(enemy_x,enemy_y))
    

enemy_change = 0.1

enemy_left = 0
enemy_right = 1

# bullet 
goli = pygame.image.load('bullet2.png')
bullet_x = plyer_x+16
bullet_y = plyer_y-20
bullet_state = False
def bult(x,y):
    win.blit(goli,(x,y))


# main loop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

        # key clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plyer_x-=0.2
                left = True
                right = up = down = False
            if event.key == pygame.K_RIGHT:
                plyer_x+=0.2
                right = True
                left = up = down = False
            if event.key == pygame.K_UP:
                plyer_y-=0.2
                up = True
                left = right = down = False
            if event.key == pygame.K_DOWN:
                plyer_y+=0.2
                down = True
                left = right = up = False
            if event.key == pygame.K_SPACE:
                # filling value in dataset variables
                p_x = plyer_x
                p_y = plyer_y
                e_x = enemy_x
                e_y = enemy_y
                e_left = enemy_left
                e_right = enemy_right
                
                bullet_state = True
            
                
        # key released
        if event.type == pygame.KEYUP:
            pass
            


    # movement settler
    if left:
        plyer_x-=0.2

    if right:
        plyer_x+=0.2
    if up:
        plyer_y-=0.2
    if down:
        plyer_y+=0.2
        


    # player boundaries
    if plyer_x<=0:
        plyer_x = 0

    if plyer_x>=436:
        plyer_x = 436

    if plyer_y<=0:
        plyer_y = 0

    if plyer_y>=436:
        plyer_y = 436

    # enemy movements and boundaries
    if enemy_alive:
        if enemy_x<=0:
            enemy_x = 0
            enemy_change = 0.1
            enemy_y+=5
            enemy_right = 1
            enemy_left = 0
            
        if enemy_x>=436:
            enemy_x = 436
            enemy_change = -0.1
            enemy_y+=5
            enemy_right = 0
            enemy_left = 1
    else:
        score+=10
        #print(score)
        enemy_alive = True
        enemy_x = random.randint(0,436)
        enemy_y = random.randint(0,100)
        bullet_x = plyer_x+16
        bullet_y = plyer_y-20
        


    enemy_x+=enemy_change
    player(plyer_x,plyer_y)
    enemy(enemy_x,enemy_y)

 

    
    if bullet_state:
        bullet_y-=0.2
        if (bullet_x>=enemy_x and bullet_x<=enemy_x+64) and (bullet_y>=enemy_y and bullet_y<=enemy_y+64):
            hit = 1
            #print(p_x,p_y,e_x,e_y,e_left,e_right,hit)
            writer.writerow([p_x,p_y,e_x,e_y,e_left,e_right,hit])
            data_reset()
            bullet_state = False
            enemy_alive = False

            
        if bullet_y>=0:
            bult(bullet_x,bullet_y)
        else:
            # if bullet doesn't hit the alien
            #print(p_x,p_y,e_x,e_y,e_left,e_right,hit)
            writer.writerow([p_x,p_y,e_x,e_y,e_left,e_right,hit])
            data_reset()
            bullet_state = False
            bullet_x = plyer_x+16
            bullet_y = plyer_y-20
    # score display
    win.blit(scorer(score), dest=(415,0))
        
    pygame.display.update()

file.close()
pygame.quit()


