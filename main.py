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
orange = (255, 165, 0)

# Массивы объектов
objects_A_Box = []
objects_O_Box = []
objects_A = []
objects_O = []
objects_Y = []

# image_A_Box = pygame.image.load("alphabet/A_Box.png")
# image_O_Box = pygame.image.load("alphabet/O_Box.png")
image_A = pygame.image.load("alphabet/a_cursive.png")
image_O = pygame.image.load("alphabet/o_cursive.png")
image_Y = pygame.image.load("alphabet/Y.png")

# Создание объектов
# for i in range(10):
#     objects_A.append(pygame.Rect(50 + i * 70, 50, 30, 30))
#     objects_O.append(pygame.Rect(50 + i * 70, 200, 30, 30))
#     objects_A_Box.append(pygame.Rect(50 , 300, 50, 50)) # 10 рамок в 1 точке (50, 300) 
#     objects_O_Box.append(pygame.Rect(50 + i * 70, 400, 50, 50))

# Создание объектов
# for i in range(10):
#     x = random.randrange(50, 700, 50)
#     y = random.randrange(50, 400, 50)
objects_A.append(pygame.Rect(50,  50, 1, 1 ))
objects_A.append(pygame.Rect(250, 50, 1, 1))
objects_A.append(pygame.Rect(350, 50, 1, 1))
objects_A.append(pygame.Rect(450, 50, 1, 1))
objects_A.append(pygame.Rect(500, 50, 1, 1))


objects_O.append(pygame.Rect(150, 50, 30, 30))
objects_O.append(pygame.Rect(500, 50, 30, 30))


for i in range(10):
    objects_A_Box.append(pygame.Rect(50 , 500, 50, 50)) # 10 рамок в 1 точке (50, 300) 
    objects_O_Box.append(pygame.Rect(150 , 500, 50, 50))

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
            for obj in objects_O_Box:
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

    # for obj in objects_O_Box:
        # pygame.draw.rect(screen, red, obj, 5)
        # pygame.draw.circle(screen, orange, obj.center, 30, 5)

# Проверка пересечения объектов, рисование кругов
    for obj1 in objects_O_Box:
        intersecting = False
        for obj2 in objects_O:
            if obj1.colliderect(obj2):
                intersecting = True
                break
        if intersecting:
            pygame.draw.circle(screen, green, obj1.center, 30, 5)
            
        else:
            pygame.draw.circle(screen, orange, obj1.center, 30, 5)

# Проверка пересечения объектов, рисование квадратов
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