import pygame

# Инициализация Pygame
pygame.init()

# Создаем экран
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Плавное движение с анимацией")

# Загрузка кадров анимации для ходьбы персонажа (например, 4 кадра для движения вправо)
walk_right = [pygame.image.load(f"player_sprites/walk_right_{i}.png") for i in range(1, 5)]
walk_left = [pygame.image.load(f"player_sprites/walk_left_{i}.png") for i in range(1, 5)]
walk_up = [pygame.image.load(f"player_sprites/walk_up_{i}.png") for i in range(1, 5)]
walk_down = [pygame.image.load(f"player_sprites/walk_down_{i}.png") for i in range(1, 5)]

# Масштабируем изображения
walk_right = [pygame.transform.scale(img, (50, 50)) for img in walk_right]
walk_left = [pygame.transform.scale(img, (50, 50)) for img in walk_left]
walk_up = [pygame.transform.scale(img, (50, 50)) for img in walk_up]
walk_down = [pygame.transform.scale(img, (50, 50)) for img in walk_down]

# Установки персонажа
character_x = 400
character_y = 300
character_speed = 10  # скорость движения в пикселях
character_direction = "right"  # текущее направление персонажа
frame = 0  # текущий кадр анимации
walk_animation_delay = 10  # задержка смены кадра анимации
animation_counter = 0  # счетчик для управления анимацией

# Прямоугольник для проверки попадания и анимации
character_rect = pygame.Rect(character_x, character_y, 50, 50)

# Главный цикл
running = True
while running:
    screen.fill((255, 255, 255))  # Очищаем экран

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление анимацией и движением
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        character_direction = "right"
        character_x += character_speed
    elif keys[pygame.K_LEFT]:
        character_direction = "left"
        character_x -= character_speed
    elif keys[pygame.K_UP]:
        character_direction = "up"
        character_y -= character_speed
    elif keys[pygame.K_DOWN]:
        character_direction = "down"
        character_y += character_speed

    # Обновляем прямоугольник персонажа
    character_rect.topleft = (character_x, character_y)

    # Управление анимацией ходьбы
    if character_direction == "right":
        screen.blit(walk_right[frame], character_rect)
    elif character_direction == "left":
        screen.blit(walk_left[frame], character_rect)
    elif character_direction == "up":
        screen.blit(walk_up[frame], character_rect)
    elif character_direction == "down":
        screen.blit(walk_down[frame], character_rect)
    # Обновление кадров анимации
    animation_counter += 1
    if animation_counter >= walk_animation_delay:
        animation_counter = 0
        frame = (frame + 1) % len(walk_right)  # Зацикливаем анимацию

    # Обновление экрана
    pygame.display.flip()

    # Задержка для плавного движения
    pygame.time.delay(10)

# Завершение программы
pygame.quit()
