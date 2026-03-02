import pygame
import sys

SCENE_MENU = "menu"
SCENE_CREDITS = "credits"
SCENE_GAME = "game"
SCENE_WIN = "win"

def win(screen):
    BLUE = (137, 207, 240)
    WHITE = (255, 255, 255)
    YELLOW = (151, 141, 67)
    GREEN = (144, 178, 112)
    RED = (255, 0, 0)
    BLACK = (34, 34, 34)

    pygame.display.set_caption("Winner!")
    screen.fill(BLUE)

    my_font = pygame.font.SysFont('Times New Roman', 12)

    text_surface = my_font.render('YOU WIN!', True, BLACK)
    text_rect = text_surface.get_rect(center=(200, 10))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    start_button = pygame.Rect(150, 60, 100, 30)
    pygame.draw.rect(screen, GREEN, start_button)

    def draw_centered_text(surface, text, font, color, rect):
        text_surface = font.render(text, True, color)

        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        surface.blit(text_surface, text_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (start_button.collidepoint(pygame.mouse.get_pos())):
                    print("Start")
                    return SCENE_MENU
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, start_button)
        draw_centered_text(screen, "Back to Menu", my_font, BLACK, start_button)
        pygame.display.flip()