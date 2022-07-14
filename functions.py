import time
import pygame 
from constants import carImg, carImg2, black, display_width, display_height, gameDisplay


#счетчик
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Purina ran: " + str(count), True, black)
    gameDisplay.blit(text,(0, 0))


#функция для появляющихся элементов на дороге
def things(thingx, thingy):
    gameDisplay.blit(carImg2,[thingx, thingy])


#отрисовка авто
def car(img, x, y):
    gameDisplay.blit(img, (x, y))
    
    
def crash():
    message_display('PURINA DIED!')


def button(msg, x, y, w, h, ic, ac, action = None):
    mouse1 = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse1[0] > x and y + h > mouse1[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

#обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    
    from eight import game_loop
    game_loop()


