import pygame
import random

# Инициализация pygame
pygame.init()

# Создание окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Название игры
pygame.display.set_caption("Учусь читать")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Массивы объектов
objects_A_Box = []
objects_O_Box = []
objects_A = []
objects_O = []
objects_Y = []

# image_A_Box = pygame.image.load("alphabet/A_Box.png")
# image_O_Box = pygame.image.load("alphabet/O_Box.png")
image_A = pygame.image.load("alphabet/A.png")
image_O = pygame.image.load("alphabet/O.png")
image_Y = pygame.image.load("alphabet/Y.png")

# Создание объектов
for i in range(10):
    objects_A.append(pygame.Rect(50 + i * 70, 50, image_A.get_width(), image_A.get_height()))
    objects_O.append(pygame.Rect(50 + i * 70, 200, image_O.get_width(), image_O.get_height()))
    objects_A_Box.append(pygame.Rect(50 , 300, 50, 50)) # 10 рамок в 1 точке (50, 300) 
    objects_O_Box.append(pygame.Rect(50 + i * 70, 400, 50, 50))
    
# Переменная для хранения перетаскиваемого объекта
dragging = None

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects_A_Box:
                if obj.collidepoint(event.pos):
                    dragging = obj
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pygame.MOUSEMOTION and dragging:
            dragging.x = event.pos[0] - dragging.width // 2
            dragging.y = event.pos[1] - dragging.height // 2

    # Очистка экрана
    screen.fill(white)

    # Рисование объектов
    for obj in objects_A:
        screen.blit(image_A, obj)
    for obj in objects_O:
        screen.blit(image_O, obj)
    for obj in objects_A_Box:
        pygame.draw.rect(screen, blue, obj, 5)
    for obj in objects_O_Box:
        pygame.draw.rect(screen, red, obj, 5)


# Проверка пересечения объектов
    for obj1 in objects_A_Box:
        intersecting = False
        for obj2 in objects_A:
            if obj1.colliderect(obj2):
                intersecting = True
                break
        if intersecting:
            pygame.draw.rect(screen, green, obj1, 5)
        else:
            pygame.draw.rect(screen, blue, obj1, 5)

    # Обновление экрана
    pygame.display.flip()
    # Ограничение скорости игры
    pygame.time.Clock().tick(60)