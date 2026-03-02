import pygame
import sys
import time

SCENE_MENU = "menu"
SCENE_CREDITS = "credits"
SCENE_GAME = "game"
SCENE_WIN = "win"

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 12)

BLUE = (137, 207, 240)
WHITE = (255, 255, 255)
YELLOW = (151, 141, 67)
GREEN = (144, 178, 112)
RED = (255, 0, 0)
BLACK = (34, 34, 34)

border_thickness = 10
right_border_edge = 400
bottom_border_edge = 300

def menu(screen):
    # Set up the game window
    pygame.display.set_caption("World's Hardest Game")

    screen.fill(BLUE)
    start_button = pygame.Rect(150, 60, 100, 30)
    credits_button = pygame.Rect((150, 120, 100, 30))
    pygame.draw.rect(screen, GREEN, start_button)
    pygame.draw.rect(screen, GREEN, credits_button)

    def draw_centered_text(surface, text, font, color, rect):
        text_surface = font.render(text, True, color)

        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        surface.blit(text_surface, text_rect)


    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (start_button.collidepoint(pygame.mouse.get_pos())):
                    print("Start")
                    return SCENE_GAME
                if (credits_button.collidepoint(pygame.mouse.get_pos())):
                    print("Credits")
                    return SCENE_CREDITS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, start_button)
        pygame.draw.rect(screen, GREEN, credits_button)
        draw_centered_text(screen, "Play Game", my_font, BLACK, start_button)
        draw_centered_text(screen, "Credits", my_font, BLACK, credits_button)
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
