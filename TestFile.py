import pygame
import sys
import time

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
pygame.draw.rect(screen, WHITE, (rectX, rectY, 30, 30), 5, 5)
pygame.draw.rect(screen, RED, (enemyX, enemyY, 30, 30), 5, 5)
pygame.display.flip()

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
                rectY -= 10
                print("Move the character forwards")
            elif event.key == pygame.K_s:
                rectY += 10
                print("Move the character backwards")
            elif event.key == pygame.K_a:
                rectX -= 10
                print("Move the character left")
            elif event.key == pygame.K_d:
                rectX += 10
                print("Move the character right")

    rect = pygame.Rect(rectX, rectY, 30, 30)
    collide = False
    enemy_list = []
    for i in range(5):
        enemy_list.append(pygame.Rect(enemyX, enemyY + i*60, 30, 30))
    for i in range(5):
        if collide == False:
            collide = rect.colliderect(enemy_list[i])
    playerColor = (255, 0, 0) if collide else (255, 255, 255)
    enemyColor = (255, 0, 0)
    screen.fill(BLUE)
    pygame.draw.rect(screen, playerColor, rect, 5, 5)
    for i in range(5):
        pygame.draw.rect(screen, enemyColor, enemy_list[i], 5, 5)
    pygame.display.flip()

    if collide:
        time.sleep(2)
        print("Collision")
        running = False
            
    if event.type == pygame.QUIT:
        running = False

# Quit Pygame
pygame.quit()
