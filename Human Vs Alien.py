#NC Asmaa Khalid
#Semester Project OOP
#Mid Project Report: Code
#This is approximately 40% of the total code

from __future__ import division
import pygame
import random

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.init()   #including pygame
pygame.mixer.init()  # For sound files in the game
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #to display the pygame screen
pygame.display.set_caption("Human Vs Alien") #Name of the game displayed on the screen
clock = pygame.time.Clock() #to sync FPS

font_name = pygame.font.match_font('arial') #font style


####################################################################################################################



#main menuscreen

def main_menu():
    global screen   #pygame screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "mainmenu.ogg"))   #path for the sound file "mainmenu.ogg"
    pygame.mixer.music.play(-1)

    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        event= pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [ENTER] to Continue", 40, WIDTH/2, HEIGHT/2)
            draw_text(screen, "Press [Q] to Quit", 40, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()


  def draw_text(surf, text, size, x, y):
    ## for displaying scores and other things on the screen
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    #if pct <0:
    #    pct=0
    
    pct = max(pct, 0) 
    ## moving them to top
    # bar_length = 100
    # bar_height = 10
    a=(pct/100)* bar_length
    fill= a;
    if a <=50
    half_fill=a;
    
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    halffill_rect=pygame.Rect(x,y,half_fill,bar_height)
    pygame.draw.rect(surf, GREEN, fill_rect) #for denoting full health
    pygame.draw.rect(surf, RED, halffill_rect) #for denoting half health
    pygame.draw.rect(surf, WHITE, outline_rect, 2) #when empty or outline of the bar
          
##########################################################################################################
    
##Player Definition

 class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.image.set_colorkey(BLACK) #for transparency
        self.rect = player.image.get_rect()
        self.radius = 23
        self.rect.centerx = WIDTH / 2   
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0 
        self.shield = 100
        self.shoot_delay = 200
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3 #max lives
        self.hidden = False
        self.h_timer = pygame.time.get_ticks()
        self.power = 1
        self.p_timer = pygame.time.get_ticks()

    def update(self):
        ## time out for powerups
        if self.power >=2 and pygame.time.get_ticks() - player.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        # unhide 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2           #screen adjustment
            self.rect.bottom = HEIGHT - 30

        #use weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()

       

        
    def shoot(self):         
        # to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                "FIRE!"
                lbullet = Bullet(self.rect.centerx, self.rect.top)               
                all_sprites.add(lbullet)
                lbullets.add(lbullet)
                firebullets_sound.play()
            if self.power == 2:
                "FIRE!"
                lbullet1 = Bullet(self.rect.left, self.rect.centery)
                lbullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(lbullet1)
                all_sprites.add(lbullet2)
                lbullets.add(lbullet1)
                lbullets.add(lbullet2)
                
                firebullet_sound.play()

            """ POWAAHHH """
            if self.power >= 3:
                lbullet = LaserBullet(self.rect.left, self.rect.centery)
                lbullet= LaserBullet(self.rect.right, self.rect.centery)
                missile1 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(lbullet1)
                all_sprites.add(lbullet2)
                all_sprites.add(missile1)
                lbullets.add(lbullet1)
                lbullets.add(lbullet2)
                bullets.add(missile1)
                firebullet_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

 ############################################################################################################       


## defines the sprite for bullets
class LaserBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = lbullet_img
        self.image.set_colorkey(BLACK)#for transparency
        self.rect = self.image.get_rect()
        # place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """Release"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()
            
# group for laser bullets
lbullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

############################################################################################################


##defines the sprite for missles
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)#for transparency
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """Release"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


##########################################################################################################
            
 ## defines the sprite for Powerups
class power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK) #for transparency
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.center = center
        self.speedy = 2

    def update(self):
        """Release"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > HEIGHT:
            self.kill()



#################################################################################################

            
## Loading game images

#for background
background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
background_rect = background.get_rect()

#for player
player_img = pygame.image.load(path.join(img_dir, 'player_ship.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (30, 20))

#for laser bullets
lbullet_img = pygame.image.load(path.join(img_dir, 'laserbullets.png')).convert()

#For missiles
missile_img = pygame.image.load(path.join(img_dir, 'missile.png')).convert()
player_mini_img.set_colorkey(BLACK) #for transparency


################################################################################################

##Loading game sounds

#for shooting Laser bullets
firebullet_sound = pygame.mixer.Sound(path.join(sound_folder, 'shoot.wav'))

#for missiles
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'missile.ogg'))

pygame.quit();
