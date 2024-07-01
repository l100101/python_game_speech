import pygame

class Monster:
    def __init__(self, x, y, main_image, sound_file):
        self.x = x
        self.y = y
        self.main_image = main_image
        self.sound = pygame.mixer.Sound(sound_file)
        self.animation_images = []
        self.current_image_index = 0
        self.animation_time = 0
        self.animation_delay = 100  # milliseconds

    def load_animation_images(self, image_files):
        for image_file in image_files:
            image = pygame.image.load(image_file).convert_alpha()
            self.animation_images.append(image)

    def update(self, dt):
        self.animation_time += dt
        if self.animation_time >= self.animation_delay:
            self.current_image_index = (self.current_image_index + 1) % len(self.animation_images)
            self.animation_time = 0

    def draw(self, surface):
        image = self.animation_images[self.current_image_index]
        surface.blit(image, (self.x, self.y))

    def on_click(self):
        self.sound.play()