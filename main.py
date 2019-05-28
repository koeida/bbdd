import pygame
from random import randint
from math import sin

def get_center_x(w, num, gap):
    total_width = num * (w + gap) - gap
    start_x = (width - total_width) / 2
    return start_x

def make_text(text, size = 50, color = (255, 255, 255), font_type = None):
    text = str(text)
    if font_type == None:
        font = pygame.font.SysFont("Terminal", size)
    else:
        font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    return text

pygame.init()

size = width, height = (1280, 1024)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
word = ""
colors = [(255,255,255), (255,0,0), (255,138,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (145,17,164)]
curcolor = 0
highlight = 1

while(True):
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            k = event.key
            c = chr(k)
            if k == pygame.K_ESCAPE:
                exit()
            if c in "abcdefghijklmnopqrstuvwxyz":
                word += c
            elif event.key == 8: # backspace
                word = word[:-1]
            elif event.key == 9: # tab
                curcolor += 1 
            elif c == "[":
                if highlight > 0:
                    highlight -= 1 
            elif c == "]":
                highlight += 1
            else:
                print(event.key)

    font_size = int(int(height * 1.25) * 1/(0.25 * len(word) + 1))
    col = colors[curcolor % len(colors)]
    t = make_text(word, font_size, col)
    wordx = get_center_x(t.get_width(), 1, 1)
    wordy = (height / 2) - (font_size / 3)
    screen.blit(t, (wordx, wordy))
    pygame.display.flip()
