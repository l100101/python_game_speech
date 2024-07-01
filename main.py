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
pygame.display.set_caption("Monsters Game") # даём название окну игры

monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')
monster3 = pygame.image.load('monster3.png')
monster1 = pygame.transform.scale(monster1, (200, 200))
monster2 = pygame.transform.scale(monster2, (200, 200))
monster3 = pygame.transform.scale(monster3, (200, 200))
sound1 = pygame.mixer.Sound('monster1.mp3')
sound2 = pygame.mixer.Sound('monster2.mp3')
sound3 = pygame.mixer.Sound('monster3.mp3')

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()
        
pygame.mixer.music.load('Soundtrack.mp3')
pygame.mixer.music.play(-1)

game = True # объявляем переменную-флаг для цикла игры
# запускаем бесконечный цикл
while game:
    # получаем список возможных действий игрока
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        # если пользователь нажал на крестик закрытия окна…
            if event.key == K_ESCAPE:
                pygame.quit()# …останавливаем цикл
                exit() # добавляем корректное завершение работы
        elif event.type == pygame.QUIT:
                pygame.quit()# …останавливаем цикл
                exit() # добавляем корректное завершение работы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if monster1.get_rect(topleft=(100, 250)).collidepoint(mouse_pos):
                sound1.play()
            elif monster2.get_rect(topleft=(300, 250)).collidepoint(mouse_pos):
                sound2.play()
            elif monster3.get_rect(topleft=(500, 250)).collidepoint(mouse_pos):
                sound3.play()

    # размещаем новую поверхность на нашем экране — подготовленный jpeg
    screen.blit(back, (0, 0))
    # screen.blit(test_surface, (300, 100))
    screen.blit(monster1, (100, 250))
    screen.blit(monster2, (300, 250))
    screen.blit(monster3, (500, 250))
   # обновляем экран игры
    pygame.display.update()
    # добавляем к таймеру количество fps для частоты обновления основного цикла
    clock.tick(fps)