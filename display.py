import sys
import pygame
import pygame.freetype
from logic import BingoLogic

print("Bingo started")

#settings
MAX_NUMBER = 99
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

#colors,fonts etc
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 160, 210)
FONT_SIZE_L = 96
FONT_SIZE_S = 24
GRID_COLS = 10
GRID_ROWS = 10
GRID_PADDING = 10

#initializations
pygame.init()
print("pygame init")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bingo Ε' Τάξης")
font_large = pygame.font.SysFont(None, FONT_SIZE_L)
font_small = pygame.font.SysFont(None, FONT_SIZE_S)
freetype_font = pygame.freetype.SysFont(None, FONT_SIZE_L)
clock = pygame.time.Clock()

logic = BingoLogic(MAX_NUMBER)
print("logic initialized with max number: ", MAX_NUMBER)

#button setup
button_rect = pygame.Rect((WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 60))
start_button_rect = pygame.Rect((WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 100, 200, 60))

def draw_button(surface, rect, text, mouse_pos):
    color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(surface, color, rect, border_radius = 8)
    label = font_small.render(text, True, TEXT_COLOR)
    label_rect = label.get_rect(center = rect.center)
    surface.blit(label, label_rect)

def draw_startup(surface, mouse_pos):
    title = font_large.render("BINGO Ε' ΤΑΞΗΣ", True, TEXT_COLOR)
    title_rect = title.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
    surface.blit(title,title_rect)
    draw_button(surface, start_button_rect, "Πατήστε για εκκίνηση", mouse_pos)

def draw_current(surface, number):
    center_x = WINDOW_WIDTH // 2
    start_y = WINDOW_HEIGHT // 3
    if number is None:
        text = "Όλες οι μπάλες τραβήχτηκαν!\nΕλέξτε για νικητή"
        freetype_font.render_to(
            surface,
            (center_x, start_y),
            text,
            fgcolor = TEXT_COLOR,
            size = FONT_SIZE_L,
            style = pygame.freetype.STYLE_DEFAULT,
            bgcolor = None,
            rotation = 0
        )
        return
    
    img = font_large.render(str(number), True, TEXT_COLOR)
    rect = img.get_rect(center = (center_x, start_y))
    surface.blit(img, rect)

def draw_history(surface, drawn_list):
    cell_w = (WINDOW_WIDTH - 2 * GRID_PADDING) // GRID_COLS
    cell_h = (WINDOW_HEIGHT // 3 - GRID_PADDING) // GRID_ROWS

    for idx, num in enumerate(drawn_list):
        row = idx // GRID_COLS
        col = idx % GRID_COLS
        x = GRID_PADDING + col * cell_w
        y = WINDOW_HEIGHT // 3 + GRID_PADDING + row * cell_h
        pygame.draw.rect(surface, BUTTON_COLOR, (x, y, cell_w - 2, cell_h - 2), border_radius = 4)
        txt = font_small.render(str(num), True, TEXT_COLOR)
        txt_rect = txt.get_rect(center = (x + cell_w//2, y + cell_h//2))
        surface.blit(txt, txt_rect)

def main():
    current_number = None
    running = True
    state = 'startup'

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

