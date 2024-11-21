import pygame

# Инициализация pygame
pygame.init()
pygame.font.init()

# Настройка шрифта
font = pygame.font.Font("font.ttf", 75)  # Используется пользовательский шрифт

# Создание окна
screen_width = 1024
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Название игры
pygame.display.set_caption("Учусь читать")

# Цвета
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

# Буквы для замены изображений
letters = {
    "а": font.render("а", True, (0, 0, 0)),
    "о": font.render("о", True, (0, 0, 0)),
    "у": font.render("о", True, (0, 0, 0)),
    "ю": font.render("о", True, (0, 0, 0)),
    "ц": font.render("о", True, (0, 0, 0)),
    "т": font.render("о", True, (0, 0, 0)),
    "б": font.render("о", True, (0, 0, 0)),
    "д": font.render("о", True, (0, 0, 0)),
    "л": font.render("о", True, (0, 0, 0)),
    "м": font.render("о", True, (0, 0, 0)),
    "е": font.render("о", True, (0, 0, 0)),
    "г": font.render("о", True, (0, 0, 0)),
    "и": font.render("о", True, (0, 0, 0)),
    "н": font.render("о", True, (0, 0, 0)),
    "к": font.render("о", True, (0, 0, 0)),
    "п": font.render("о", True, (0, 0, 0)),
    "р": font.render("о", True, (0, 0, 0)),
    "ф": font.render("о", True, (0, 0, 0))
   
}


# Создание массивов объектов
objects_A = [pygame.Rect(50, 50, *letters["а"].get_size())]
objects_O = [pygame.Rect(150, 50, *letters["о"].get_size())]

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
