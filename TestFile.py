import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 12)


BLUE = (137, 207, 240)
WHITE = (255, 255, 255)
YELLOW = (151, 141, 67)
GREEN = (144, 178, 112)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

# change screen color to white
screen.fill(BLUE)

MOVE_SIDE = 100
clock = pygame.time.Clock()

move_side_event = pygame.USEREVENT + 1

pygame.time.set_timer(move_side_event, MOVE_SIDE)

move_left = True

rectX = 100
rectY = 100
#pygame.draw.rect(screen, WHITE, (rectX, rectY, 30, 30), 5, 5)
#pygame.draw.rect(screen, RED, (enemyX, enemyY, 30, 30), 5, 5)
pygame.display.flip()

#outline_list = pygame.sprite.Group()

class Border (pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
    
class Enemies (pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.radius = 5

        pygame.draw.circle(self.image, RED, (10//2, 10//2), 5)

class Coins (pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.radius = 5

        pygame.draw.circle(self.image, YELLOW, (10//2, 10//2), 5)

class Finish (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 280))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 10

player = Player ()
finish = Finish ()
border_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
coins_list = pygame.sprite.Group()

for i in range(9):
    enemy = Enemies(300, 25 + i*30)
    enemy_list.add(enemy)

for i in range(9):
    coin = Coins(250, 25 + i*30)
    coins_list.add(coin)

border_thickness = 10
right_border_edge = 300
bottom_border_edge = 400
border1 = Border(BLACK, bottom_border_edge, border_thickness, 0, 0)
border2 = Border(BLACK, border_thickness, 300, 0, 0)
border3 = Border(BLACK, border_thickness, 300, bottom_border_edge - border_thickness, 0)
border4 = Border(BLACK, bottom_border_edge, border_thickness, 0, right_border_edge - border_thickness)
border_list.add(border1)
border_list.add(border2)
border_list.add(border3)
border_list.add(border4)

#outline_list.add(pygame.Rect(0, 0, 400, 30))
#outline_list.add(pygame.Rect(0, 0, 30, 300))
#outline_list.add(pygame.Rect(370, 0, 30, 300))
#outline_list.add(pygame.Rect(0, 270, 400, 30))

up_text = my_font.render('Up!', True, (255, 255, 255))
down_text = my_font.render('Down!', True, (255, 255, 255))
left_text = my_font.render('Left!', True, (255, 255, 255))
right_text = my_font.render('Right!', True, (255, 255, 255))

coinsCollected = 0
playerWin = False

# Game loop
running = True
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == move_side_event and playerWin == False:
            if move_left:
                for enemy in enemy_list:
                    enemy.rect.x -= 5
            else:
                for enemy in enemy_list:
                    enemy.rect.x += 5

            for enemy in enemy_list:
                if enemy.rect.x < 50:
                    move_left = False
                if enemy.rect.x > 350:
                    move_left = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.rect.y -= 5
                print("Move the character forwards")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.y += 5
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.rect.y += 5
                print("Move the character backwards")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.y -= 5
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.rect.x -= 5
                print("Move the character left")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.x += 5
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.rect.x += 5
                print("Move the character right")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.x -= 5

    #rect = pygame.Rect(rectX, rectY, 30, 30)
    collide = False
    completed = False
    

    if pygame.sprite.spritecollide(player, enemy_list, False, pygame.sprite.collide_circle):
        collide = True
    
    if pygame.sprite.spritecollide(player, coins_list, True, pygame.sprite.collide_circle):
        coinsCollected += 1
        print(f"Coins: {coinsCollected}")

    if pygame.sprite.collide_rect(player, finish) and coinsCollected == 9:
        completed = True
        print("Finished")
        playerWin = True
        time.sleep(2)
        running = False

    screen.fill(BLUE)
    border_list.draw(screen)
    for enemy in enemy_list:
        screen.blit(enemy.image, enemy.rect)
    for coin in coins_list:
        screen.blit(coin.image, coin.rect)
    screen.blit(player.image, player.rect)
    screen.blit(finish.image, finish.rect)
    pygame.display.flip()

    if collide:
        time.sleep(2)
        print("Collision")
        running = False
            
    if event.type == pygame.QUIT:
        running = False

# Quit Pygame
pygame.quit()
