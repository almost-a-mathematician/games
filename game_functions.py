import pygame
from player import carImg

#функция для появляющихся элементов на дороге
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

#размер окна
display_width = 800  #параметр высоты
display_height = 600  #параметр ширины

#окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  #размер
pygame.display.set_caption("Don't crush my car, dude!")  #название