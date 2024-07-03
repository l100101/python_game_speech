import pygame
from sys import exit
from monster import Monster
from pygame.locals import *
from menu import Menu

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

menu_image = pygame.image.load('menu_sprite.jpg')
menu_surface = pygame.Surface((width, height)) # создаём поверхность по размерам
menu_surface.blit(menu_image, (0, 0))


# загружаем в переменную картинку из папки с нашим файлом
back = pygame.image.load('monsters.jpg')
pygame.display.set_caption("Speech Game") # даём название окну игры

# Загрузка изображений для анимации монстра
doge_image_files = [
    'sprites_doge/doge (1).gif',
    'sprites_doge/doge (2).gif',
    'sprites_doge/doge (3).gif',
    'sprites_doge/doge (4).gif',
    'sprites_doge/doge (5).gif',
    'sprites_doge/doge (6).gif',
    'sprites_doge/doge (7).gif',
    'sprites_doge/doge (8).gif',
    'sprites_doge/doge (9).gif',
    'sprites_doge/doge (10).gif',
    'sprites_doge/doge (11).gif',
    'sprites_doge/doge (12).gif',
    # Добавьте столько путей, сколько есть кадров анимации
]

meow_image_files = [
    'sprites_meow/meow (1).gif',
    'sprites_meow/meow (2).gif',
    'sprites_meow/meow (3).gif',
    'sprites_meow/meow (4).gif',
    'sprites_meow/meow (5).gif',
    'sprites_meow/meow (6).gif',
    'sprites_meow/meow (7).gif',
    'sprites_meow/meow (8).gif',
    'sprites_meow/meow (9).gif',
    'sprites_meow/meow (10).gif',
    'sprites_meow/meow (11).gif',
    'sprites_meow/meow (12).gif',
    'sprites_meow/meow (13).gif',
    'sprites_meow/meow (14).gif',
    'sprites_meow/meow (15).gif',
    'sprites_meow/meow (16).gif',
    'sprites_meow/meow (17).gif',
    'sprites_meow/meow (18).gif',
    'sprites_meow/meow (19).gif',
    'sprites_meow/meow (20).gif',
    'sprites_meow/meow (21).gif',
    'sprites_meow/meow (22).gif',
    'sprites_meow/meow (23).gif',
    'sprites_meow/meow (24).gif',
    'sprites_meow/meow (25).gif',
    'sprites_meow/meow (26).gif',
    'sprites_meow/meow (27).gif'
]

ping_image_files = [
    'sprites_ping/ping (1).gif',
    'sprites_ping/ping (2).gif',
    'sprites_ping/ping (3).gif',
    'sprites_ping/ping (4).gif',
    'sprites_ping/ping (5).gif',
    'sprites_ping/ping (6).gif',
    'sprites_ping/ping (7).gif',
    'sprites_ping/ping (8).gif',
    'sprites_ping/ping (9).gif',
    'sprites_ping/ping (10).gif',
    'sprites_ping/ping (11).gif',
    'sprites_ping/ping (12).gif',
    'sprites_ping/ping (13).gif',
    'sprites_ping/ping (14).gif',
    'sprites_ping/ping (15).gif',
    'sprites_ping/ping (16).gif',
    'sprites_ping/ping (17).gif',
    'sprites_ping/ping (18).gif',
    'sprites_ping/ping (19).gif',
    'sprites_ping/ping (20).gif',
    'sprites_ping/ping (21).gif',
    'sprites_ping/ping (22).gif'
]
Monster1_pos = [100, 300]
Monster2_pos = [300, 300]
Monster3_pos = [500, 300]

monster1 = Monster(Monster1_pos[0], Monster1_pos[1], doge_image_files, "sounds/monster2.mp3", animation_speed=50)
monster2 = Monster(Monster2_pos[0], Monster2_pos[1], meow_image_files, "sounds/monster3.mp3", animation_speed=50)
monster3 = Monster(Monster3_pos[0], Monster3_pos[1], ping_image_files, "sounds/monster1.mp3", animation_speed=100)

# menu = Menu(screen, ["Play", "Level Selection", "Settings", "Exit"])

pygame.mixer.music.load('sounds/soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

game = True # объявляем переменную-флаг для цикла игры
in_menu = True # объявляем переменную-флаг для цикла меню
exit_rect = pygame.Rect(350, 150, 120, 30)
# запускаем бесконечный цикл

while True:
    while in_menu:  
        screen.blit(menu_image, (0, 0))
        pygame.draw.rect(screen, "Red", exit_rect, 2, 2)
        pygame.display.flip()
        
        events = pygame.event.get()
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                in_menu = False
                game = False
            elif event.type == pygame.QUIT:
                in_menu = False
                game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    in_menu = not in_menu
                    game = True
                
    # цикл игры
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    in_menu = not in_menu
                    game = False
                    
                if monster1.rect.collidepoint(event.pos):
                    monster1.play_sound()
                if monster2.rect.collidepoint(event.pos):
                    monster2.play_sound()
                if monster3.rect.collidepoint(event.pos):
                    monster3.play_sound()
        # размещаем новую поверхность на нашем экране — подготовленный jpeg
        screen.blit(back, (0, 0))
        # test_surface.blit(screen, (10,10))
        pygame.draw.rect(screen, "Red", exit_rect, 2, 2)
        monster1.draw(screen)
        monster2.draw(screen)
        monster3.draw(screen)
        # обновляем экран игры
        monster1.update(fps)
        monster2.update(fps)
        monster3.update(fps)
        pygame.display.flip()
        # добавляем к таймеру количество fps для частоты обновления основного цикла
        clock.tick(fps) 