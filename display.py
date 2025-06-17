import sys
import pygame
import pygame.freetype
from logic import BingoLogic

print("Bingo started")

#settings
MAX_NUMBER = 99
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 750

#colors,fonts etc
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (0, 255, 0)
FONT_SIZE_L = 96
FONT_SIZE_S = 30
CELL_SIZE = 60
GRID_COLS = 20
GRID_ROWS = 10
CELL_SPACING = 8
GRID_PADDING = 20

#initializations
pygame.init()
print("pygame init")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bingo Ε' Τάξης")
font_large = pygame.font.SysFont(None, FONT_SIZE_L)
font_small = pygame.font.SysFont(None, FONT_SIZE_S)
freetype_font = pygame.freetype.SysFont(None, FONT_SIZE_L)
clock = pygame.time.Clock()
first_click = False

logic = BingoLogic(MAX_NUMBER)
print("logic initialized with max number: ", MAX_NUMBER)

#button setup
button_rect = pygame.Rect((WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 60))
start_button_rect = pygame.Rect((WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT - 100, 300, 60))

def draw_button(surface, rect, text, mouse_pos):
    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(surface, color, rect, border_radius = 8)
    label = font_small.render(text, True, TEXT_COLOR)
    label_rect = label.get_rect(center = rect.center)
    surface.blit(label, label_rect)

def draw_multiline(surface, text, font, color, center_x, start_y):
    lines = text.split('\n')
    line_height = font.get_linesize()
    for i, line in enumerate(lines):
        img = font.render(line, True, color)
        rect = img.get_rect(center = (center_x, start_y + i * line_height))
        surface.blit(img, rect)

def draw_startup(surface, mouse_pos):
    title = font_large.render("BINGO Ε' ΤΑΞΗΣ", True, TEXT_COLOR)
    title_rect = title.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
    surface.blit(title,title_rect)
    draw_button(surface, start_button_rect, "Πατήστε για εκκίνηση", mouse_pos)

def draw_current(surface, number):
    center_x = WINDOW_WIDTH // 2
    start_y = WINDOW_HEIGHT // 6
    if number is None:
        if first_click == True:
            text = "Όλες οι μπάλες τραβήχτηκαν!\nΕλέξτε για νικητή"
            draw_multiline(surface, text, font_large, TEXT_COLOR, center_x, start_y)
        else:
            text = "Το παιχνίδι ξεκίνησε!\nΤραβήξτε την πρώτη μπάλα"
            draw_multiline(surface, text, font_large, TEXT_COLOR, center_x, start_y)
    else:
        img = font_large.render(str(number), True, TEXT_COLOR)
        rect = img.get_rect(center = (center_x, start_y))
        surface.blit(img, rect)

def draw_history(surface, drawn_list):
    for idx, num in enumerate(drawn_list):
        row = idx // GRID_COLS
        col = idx % GRID_COLS
        x = GRID_PADDING + col * (CELL_SIZE + CELL_SPACING)
        y = WINDOW_HEIGHT // 3 + GRID_PADDING + row * (CELL_SIZE + CELL_SPACING)
        pygame.draw.rect(
            surface,
            BUTTON_COLOR,
            (x, y, CELL_SIZE, CELL_SIZE),
            border_radius = 4
        )
        txt = font_small.render(str(num), True, TEXT_COLOR)
        txt_rect = txt.get_rect(center = (x + CELL_SIZE/2, y + CELL_SIZE/2))
        surface.blit(txt, txt_rect)

def main():
    current_number = None
    running = True
    state = 'startup'
    global first_click

    print("entering main loop")
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit event received")
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == 'startup':
                    if start_button_rect.collidepoint(event.pos):
                        state = 'game'
                elif state == 'game':
                    if button_rect.collidepoint(event.pos):
                        current_number = logic.draw()
                        first_click = True

        screen.fill(BG_COLOR)
        if state == 'startup':
            draw_startup(screen, mouse_pos)
        else:
            draw_current(screen, current_number)
            draw_history(screen, logic.get_drawn())
            draw_button(screen, button_rect, "Τράβηξε μπάλα", mouse_pos)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    print("pygame quit")
    sys.exit()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback; traceback.print_exc()
        input("Error occurred—press Enter to exit.")

