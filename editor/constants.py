import pygame

LVL_WIDTH  = 64
LVL_HEIGHT = 64
CMD_WIDTH  = 512
PRG_WIDTH  = CMD_WIDTH - LVL_WIDTH

TKN_WIDTH  = 152
TKN_HEIGHT = 48
TKN_PDDNG  = ( CMD_WIDTH - 3 * TKN_WIDTH ) / 4

TOKEN_SIZE = 24
TITLE_SIZE = 30

def hex_to_rgb(hx):
    r = int(hx[1:3], 16)
    g = int(hx[3:5], 16)
    b = int(hx[5:7], 16)
    return (r, g, b)

def get_font(size):
    return pygame.font.Font("resources/VT323-Regular.ttf", size)
