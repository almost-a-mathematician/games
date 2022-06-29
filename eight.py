import random

import pygame
from constants import *
from functions import text_objects, button, car, things, things_dodget, crash

#стартуем в файле модули пайгейм
pygame.init()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Purina Run", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("RUN", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


#функция для запуска игры
def game_loop():
    #размещение первой машины
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    #размещение второй машины
    x1 = (display_width * 0.65)
    y1 = (display_height * 0.8)

    x_change = 0  #позиция
    x1_change = 0

    gameExit = False

    #базовое значение для dodged
    dodged = 0

    #параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    #thingCount = 1


    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            #блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_a:
                    x1_change = -5
                    
                elif event.key == pygame.K_d:
                    x1_change = 5
            
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    x1_change = 0
            
            
            #смена позиции
            x += x_change
            x1 += x1_change

        #фон
        gameDisplay.fill(white)
        #вызов things
        things(thing_startx, thing_starty)
        #things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed #скорость +

        #создаем машину
        car(carImg, x, y)
        car(carImg, x1, y1)
        things_dodget(dodged)

        #задаем границы
        if x > display_width - car_width or x < 0:
            #gameExit = True
            crash()
        if x1 > display_width - car_width or x1 < 0:
            crash()

        #логика для счетчика
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        #логика появления помех
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

            if y < thing_starty + thing_height:
                print('y crossover')

                if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                    crash()
          

        #проверяем на обновления дисплея
        pygame.display.update()
        #кадры в секунду = 60
        clock.tick(60)


game_intro()     
game_loop()
pygame.quit()
quit()