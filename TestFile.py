import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 12)


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

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
enemyX = 300
enemyY = 50
#pygame.draw.rect(screen, WHITE, (rectX, rectY, 30, 30), 5, 5)
pygame.draw.rect(screen, RED, (enemyX, enemyY, 30, 30), 5, 5)
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
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

player = Player ()
border_list = pygame.sprite.Group()


border1 = Border(RED, 400, 30, 0, 0)
border2 = Border(RED, 30, 300, 0, 0)
border3 = Border(RED, 30, 300, 370, 0)
border4 = Border(RED, 400, 30, 0, 270)
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

# Game loop
running = True
while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == move_side_event:
            if move_left:
                enemyX -= 5
            else:
                enemyX += 5

            if enemyX < 30:
                move_left = False
            if enemyX > 370:
                move_left = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_w:
                player.rect.y -= 10
                print("Move the character forwards")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.y += 10
            elif event.key == pygame.K_s:
                player.rect.y += 10
                print("Move the character backwards")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.y -= 10
            elif event.key == pygame.K_a:
                player.rect.x -= 10
                print("Move the character left")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.x += 10
            elif event.key == pygame.K_d:
                player.rect.x += 10
                print("Move the character right")
                if pygame.sprite.spritecollide(player, border_list, False):
                    player.rect.x -= 10

    #rect = pygame.Rect(rectX, rectY, 30, 30)
    collide = False
    enemy_list = []
    for i in range(5):
        enemy_list.append(pygame.Rect(enemyX, enemyY + i*60, 30, 30))
    #for i in range(5):
    #    if collide == False:
    #        collide = rect.colliderect(enemy_list[i])
    #playerColor = (255, 0, 0) if collide else (255, 255, 255)
    enemyColor = (255, 0, 0)
    screen.fill(BLUE)
    #pygame.draw.rect(screen, playerColor, rect, 5, 5)
    for i in range(5):
        pygame.draw.rect(screen, enemyColor, enemy_list[i], 5, 5)
    #for i in range(len(outline_list)):
    #    pygame.draw.rect(screen, (0, 0, 0), outline_list[i])
    border_list.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

    if collide:
        time.sleep(2)
        print("Collision")
        running = False
            
    if event.type == pygame.QUIT:
        running = False

# Quit Pygame
pygame.quit()
