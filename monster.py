import pygame

class Monster:
    def __init__(self, x, y, gif_file, sound_file):
        self.x = x
        self.y = y
        self.gif_file = gif_file
        self.sound_file = sound_file
        self.image = self.load_static_image()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.animation = []  # Define animation as an instance variable
        self.sound = pygame.mixer.Sound(self.sound_file)
        self.playing_sound = False

    def load_static_image(self):
        gif_data = pygame.image.load(self.gif_file)
        self.animation = self.load_animation()  # Assign the animation to the instance variable
        return gif_data.subsurface(self.animation[0])

    def load_animation(self):
        gif_data = pygame.image.load(self.gif_file)
        frames = []
        for i in range(gif_data.get_width() // gif_data.get_height()):
            rect = pygame.Rect(i * gif_data.get_height(), 0, gif_data.get_height(), gif_data.get_height())
            frames.append(gif_data.subsurface(rect))
        return frames

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.play_animation()

    def play_animation(self):
        if not self.playing_sound:
            self.sound.play()
            self.playing_sound = True
        self.image = self.animation[int(pygame.time.get_ticks() // 100) % len(self.animation)]

    def draw(self, surface):
        surface.blit(self.image, self.rect)