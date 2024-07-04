import pygame

class Monster:
    def __init__(self, x, y, image_files, sound_file, animation_speed=100):
        self.x = x
        self.y = y
        self.image_files = image_files  # List of paths to the image frames
        self.sound_file = sound_file
        self.animation_speed = animation_speed  # How fast to cycle through the animation
        self.images = self.load_images()  # Load the frames
        self.current_frame = 0  # Start with the first frame
        self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        self.sound = pygame.mixer.Sound(self.sound_file)
        self.playing_sound = False
        self.last_update = pygame.time.get_ticks()  # Timestamp of the last animation frame update
        self.now_playing = False

    def load_images(self):
        frames = [pygame.image.load(img) for img in self.image_files]
        return frames

    def play_animation(self):
        if self.now_playing == True:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_speed:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]

                if self.current_frame == len(self.images) - 1:
                    self.now_playing = False

    def update(self, events):
        self.now_playing = True

    # def draw(self, surface):
    #     surface.blit(self.images, self.rect)
    def draw(self, surface):
        surface.blit(self.images[self.current_frame], self.rect)
        self.play_animation()

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.images[0].get_rect(topleft=(self.x, self.y))

    def play_sound(self):
        self.sound.play()
        # if not self.playing_sound:
        # self.playing_sound = True
