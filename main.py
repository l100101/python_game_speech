import pygame
from sys import exit
from monster import Monster
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
# объявляем ширину и высоту экрана
width = 800
height = 450
screen = pygame.display.set_mode((width, height)) # создаём экран игры
fps = 60 # устанавливаем количество кадров в секунду

clock = pygame.time.Clock() # создаём объект таймера

width_ts = 200
height_ts = 200
test_surface = pygame.Surface((width_ts, height_ts)) # создаём поверхность по размерам
test_surface.fill('White') # добавляем цвет

# загружаем в переменную картинку из папки с нашим файлом
back = pygame.image.load('monsters.jpg')
pygame.display.set_caption("Speech Game") # даём название окну игры

# monster1 = pygame.image.load('monster1.png')
# monster2 = pygame.image.load('monster2.png')
# monster3 = pygame.image.load('monster3.png')
# monster1 = pygame.transform.scale(monster1, (200, 200))
# monster2 = pygame.transform.scale(monster2, (200, 200))
# monster3 = pygame.transform.scale(monster3, (200, 200))
# sound1 = pygame.mixer.Sound('monster1.mp3')
# sound2 = pygame.mixer.Sound('monster2.mp3')
# sound3 = pygame.mixer.Sound('monster3.mp3')

monster1 = Monster(100, 100, "gifs/doge.gif", "sounds/monster1.mp3")

pygame.mixer.music.load('sounds/Soundtrack.mp3')
pygame.mixer.music.play(-1)

game = True # объявляем переменную-флаг для цикла игры
# запускаем бесконечный цикл
while game:
    # получаем список возможных действий игрока
    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()# …останавливаем цикл
            exit() # добавляем корректное завершение работы
        elif event.type == pygame.QUIT:
            pygame.quit()# …останавливаем цикл
            exit() # добавляем корректное завершение работы
      #  elif event.type == pygame.MOUSEBUTTONDOWN:
    monster1.update(events)
    monster1.draw(screen)
            
    # размещаем новую поверхность на нашем экране — подготовленный jpeg
    screen.blit(back, (0, 0))
    # обновляем экран игры
    monster1.draw(screen)
    monster1.update(fps)
    pygame.display.flip()
    # добавляем к таймеру количество fps для частоты обновления основного цикла
    clock.tick(fps)