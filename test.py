import pygame
import sys
import os
from ffpyplayer.player import MediaPlayer

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Настройки цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game with Levels and Transitions")
clock = pygame.time.Clock()

# Загрузка спрайтов
map_1 = pygame.image.load("map_lvl_1/map_1.png")
player_sprite = pygame.image.load("player_sprites/player_sprite.png")
player_sprite = pygame.transform.scale(player_sprite, (50, 50))
move_distance = 50

# Функция для воспроизведения видео с помощью ffpyplayer
def play_video(video_path):
    if not os.path.exists(video_path):
        print(f"Видео {video_path} не найдено!")
        return

    player = MediaPlayer(video_path)
    running = True

    while running:
        frame, val = player.get_frame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.close_player()
                pygame.quit()
                sys.exit()

        if frame is not None:
            img, t = frame
            if img is not None:
                img_data = bytes(img.to_bytearray()[0])
                width, height = img.get_size()
                video_frame = pygame.image.frombuffer(img_data, (width, height), "RGB")
                screen.blit(pygame.transform.scale(video_frame, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
                pygame.display.flip()

        clock.tick(FPS)  # Синхронизация по FPS

        if val == 'eof':  # Конец видео
            running = False

    player.close_player()

# Базовый класс уровня
class Level:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.arrows["up"].collidepoint(mouse_pos):
                    self.player_pos[1] -= move_distance
                elif self.arrows["down"].collidepoint(mouse_pos):
                    self.player_pos[1] += move_distance
                elif self.arrows["left"].collidepoint(mouse_pos):
                    self.player_pos[0] -= move_distance
                elif self.arrows["right"].collidepoint(mouse_pos):
                    self.player_pos[0] += move_distance


    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(FPS)

# Уровень 1
class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)
        self.player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.target_pos = [100, 700]  # Целевая точка
        self.background = map_1
        self.player = player_sprite
        # Координаты стрелок
        self.arrows = {
            "up": pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - (SCREEN_HEIGHT - 10), 50, 50),
            "down": pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 100, 50, 50),
            "left": pygame.Rect(SCREEN_WIDTH - (SCREEN_WIDTH - 10), SCREEN_HEIGHT // 2, 50, 50),
            "right": pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2, 50, 50),
        }

                

    def handle_events(self):
        super().handle_events()
        move_distance = 50

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.arrows["up"].collidepoint(mouse_pos):
                    self.player_pos[1] -= move_distance
                elif self.arrows["down"].collidepoint(mouse_pos):
                    self.player_pos[1] += move_distance
                elif self.arrows["left"].collidepoint(mouse_pos):
                    self.player_pos[0] -= move_distance
                elif self.arrows["right"].collidepoint(mouse_pos):
                    self.player_pos[0] += move_distance


    def update(self):
        # Проверка достижения цели
        if abs(self.player_pos[0] - self.target_pos[0]) < 10 and abs(self.player_pos[1] - self.target_pos[1]) < 10:
            # Смена фона и возвращение игрока в центр
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill(WHITE)
            self.player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player, (self.player_pos[0], self.player_pos[1]))
        # Рисуем стрелки
        arrow_up = pygame.image.load("arrows_sprites/arrow_up.png")
        arrow_down = pygame.image.load("arrows_sprites/arrow_down.png")
        arrow_left = pygame.image.load("arrows_sprites/arrow_left.png")
        arrow_right = pygame.image.load("arrows_sprites/arrow_right.png")
        # Resize the images (e.g., to 50x50 pixels)
        arrow_up = pygame.transform.scale(arrow_up,      (80, 80))
        arrow_down = pygame.transform.scale(arrow_down,  (80, 80))
        arrow_left = pygame.transform.scale(arrow_left,  (80, 80))
        arrow_right = pygame.transform.scale(arrow_right,(80, 80))
        
        # Blit the scaled images onto the screen
        self.screen.blit(arrow_up, self.arrows["up"])
        self.screen.blit(arrow_down, self.arrows["down"])
        self.screen.blit(arrow_left, self.arrows["left"])
        self.screen.blit(arrow_right, self.arrows["right"])


# Уровень 2
class Level2(Level):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        # Логика уровня 2
        pass

    def draw(self):
        self.screen.fill(BLACK)
        # Рисуем элементы уровня 2
        font = pygame.font.Font(None, 36)
        text = font.render("Level 2", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))

# Главная функция игры
def main():
    # Уровень 1
    level1 = Level1(screen)
    level1.run()

    # Переход между уровнями (видео)
    play_video("video/gate_lvl.mp4")

    # Уровень 2
    level2 = Level2(screen)
    level2.run()

    # Переход между уровнями (видео)
    play_video("transition2.mp4")

    # Конец игры
    print("Game Over!")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
