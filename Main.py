import pygame
import sys
import time
import random
import Menu
import Game
import WinScreen

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

border_thickness = 10
right_border_edge = 400
bottom_border_edge = 300

SCENE_MENU = "menu"
SCENE_CREDITS = "credits"
SCENE_GAME = "game"
SCENE_WIN = "win"

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

def main():
    scene = SCENE_MENU

    while True:
        if scene == SCENE_MENU:
            scene = Menu.menu(screen) # menu() returns the next scene
        elif scene == SCENE_GAME:
            scene = Game.game(screen) # game() returns the next scene
        elif scene == SCENE_WIN:
            scene = WinScreen.win(screen)
        elif scene == SCENE_CREDITS:
            print("Implement Credits Screen")
            scene = Menu.menu(screen)

if __name__ == "__main__":
    main()
        
