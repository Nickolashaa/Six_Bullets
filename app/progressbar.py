import pygame


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, max_value, *groups):
        super().__init__(*groups)
        self.x, self.y = 50, 550
        self.width, self.height = 300, 50
        self.max_value = max_value
        self.current_value = 0
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self._update_image()

    def add_progress(self, amount):
        self.current_value = min(self.current_value + amount, self.max_value)
        self._update_image()

    def _update_image(self):
        self.image.fill((0, 0, 0, 0))

        border_color = (212, 175, 55)
        pygame.draw.rect(self.image, border_color, (0, 0, self.width, self.height), 3)
 
        fill_width = int((self.current_value / self.max_value) * (self.width - 6))

        if fill_width > 0:
            fill_color = (0, 200, 0)
            pygame.draw.rect(self.image, fill_color, (3, 3, fill_width, self.height - 6))

    def reset(self):
        self.current_value = 0
        self._update_image()
