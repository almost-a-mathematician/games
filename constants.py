from pygame import display, time, image, transform


#размер окна
display_width = 800  #параметр высоты
display_height = 600  #параметр ширины

#цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

#параметры для машины
crashed = False
car_width = 73
car_speed = 0

#кадры в секунду
clock = time.Clock()

#игрок
carImg = image.load("bin/car1.png")  #картинка для игрока
carImg = transform.scale(carImg, (70, 80))  #задаем размер картинки, если большая
carImg2 = image.load("bin/car2.png")  #картинка для игрока
carImg2 = transform.scale(carImg2, (70, 80))  #задаем размер картинки, если большая




#окно игры
gameDisplay = display.set_mode((display_width, display_height))  #размер
display.set_caption("Purina Run!")  #название


