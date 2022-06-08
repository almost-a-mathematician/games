import pygame

#игрок
carImg = pygame.image.load("bin/car1.png")  #картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  #задаем размер картинки, если большая
car_width = 73
