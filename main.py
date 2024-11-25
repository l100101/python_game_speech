#Дописать кнопку выхода
#Name   File "main.py", line 75, in <module>
#NameError: name 'quit' is not defined

import pygame
pygame.init()
pygame.font.init()


font = pygame.font.Font("font.ttf", 75)  # Используется пользовательский шрифт AmadeusAP
# Создание окна
screen_width = 1024
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Название игры
pygame.display.set_caption("Жирафик-дисграфик")

# Цвета
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

# Буквы 
letters = {
    "а": font.render("а", True, "black"),
    "о": font.render("о", True, "black"),
    "б": font.render("б", True, "black"),
    "у": font.render("у", True, "black"),
    "ю": font.render("ю", True, "black"),
    "ц": font.render("ц", True, "black"),
    "т": font.render("т", True, "black"),
    "д": font.render("д", True, "black"),
    "л": font.render("л", True, "black"),
    "м": font.render("м", True, "black"),
    "е": font.render("е", True, "black"),
    "г": font.render("г", True, "black"),
    "и": font.render("и", True, "black"),
    "н": font.render("н", True, "black"),
    "к": font.render("к", True, "black"),
    "п": font.render("п", True, "black"),
    "р": font.render("р", True, "black"),
    "ф": font.render("ф", True, "black")   
}

# Создание массивов объектов
objects_A = [pygame.Rect(50, 50, *letters["а"].get_size())]
objects_O = [pygame.Rect(150, 50, *letters["о"].get_size())]
objects_B = [pygame.Rect(250, 50, *letters["б"].get_size())]
objects_U = [pygame.Rect(350, 50, *letters["у"].get_size())]
objects_Y = [pygame.Rect(450, 50, *letters["ю"].get_size())]
objects_C = [pygame.Rect(550, 50, *letters["ц"].get_size())]
objects_T = [pygame.Rect(650, 50, *letters["т"].get_size())]
objects_D = [pygame.Rect(750, 50, *letters["д"].get_size())]
objects_L = [pygame.Rect(850, 50, *letters["л"].get_size())]
objects_M = [pygame.Rect(950, 50, *letters["м"].get_size())]
objects_E = [pygame.Rect(50, 100, *letters["е"].get_size())]
objects_G = [pygame.Rect(150, 100, *letters["г"].get_size())]
objects_I = [pygame.Rect(250, 100, *letters["и"].get_size())]
objects_N = [pygame.Rect(350, 100, *letters["н"].get_size())]
objects_K = [pygame.Rect(450, 100, *letters["к"].get_size())]
objects_P = [pygame.Rect(550, 100, *letters["п"].get_size())]
objects_R = [pygame.Rect(650, 100, *letters["р"].get_size())]
objects_F = [pygame.Rect(750, 100, *letters["ф"].get_size())]


objects_A_Box = [pygame.Rect(50, 500, 75, 75)]
objects_O_Box = [pygame.Rect(150, 500, 75, 75)]

# Переменная для хранения перетаскиваемого объекта
dragging = None

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in objects_A_Box + objects_O_Box:
                if obj.collidepoint(event.pos):
                    dragging = obj
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None
        elif event.type == pygame.MOUSEMOTION and dragging:
            dragging.x = event.pos[0] - dragging.width // 2
            dragging.y = event.pos[1] - dragging.height // 2

    # Очистка экрана
    screen.fill(white)

    # Рисование букв
    for rect in objects_A:
        screen.blit(letters["а"], rect)
    for rect in objects_O:
        screen.blit(letters["о"], rect)
    for rect in objects_B:
        screen.blit(letters["б"], rect)
    for rect in objects_U:
        screen.blit(letters["у"], rect)
    for rect in objects_Y:
        screen.blit(letters["ю"], rect)
    for rect in objects_C:
        screen.blit(letters["ц"], rect)
    for rect in objects_T:
        screen.blit(letters["т"], rect)
    for rect in objects_D:
        screen.blit(letters["д"], rect)
    for rect in objects_L:
        screen.blit(letters["л"], rect)
    for rect in objects_M:
        screen.blit(letters["м"], rect)
    for rect in objects_E:
        screen.blit(letters["е"], rect)
    for rect in objects_G:
        screen.blit(letters["г"], rect)
    for rect in objects_I:
        screen.blit(letters["и"], rect)
    

    # Рисование границ
    for rect in objects_A_Box:
        pygame.draw.rect(screen, blue, rect, 5)
    # for rect in objects_O_Box:
    #     pygame.draw.rect(screen, orange, rect, 5)

    # Проверка нахождения объектов внутри границ
    for obj1 in objects_O_Box:
        contained = False
        for obj2 in objects_O:
            if obj1.contains(obj2):  # Проверка, находится ли буква "о" внутри квадрата
                contained = True
                break
        if contained:
            pygame.draw.circle(screen, green, obj1.center, 35, 5)
        else:
            pygame.draw.circle(screen, orange, obj1.center, 35, 5)

    for obj1 in objects_A_Box:
        contained = False
        for obj2 in objects_A:
            if obj1.contains(obj2):  # Проверка, находится ли буква "а" внутри квадрата
                contained = True
                break
        if contained:
            pygame.draw.rect(screen, green, obj1, 5)
        else:
            pygame.draw.rect(screen, blue, obj1, 5)

    # Обновление экрана
    pygame.display.flip()
    # Ограничение скорости игры
    pygame.time.Clock().tick(60)
