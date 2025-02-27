import pygame
from app.functions import load_image


class Fon(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('app/assets/fon.png')
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width // 3
        self.rect.y = -self.rect.height // 3

    def is_inside(self, inner_rect):
        return (
            inner_rect.left >= self.rect.left and
            inner_rect.right <= self.rect.right and
            inner_rect.top >= self.rect.top and
            inner_rect.bottom <= self.rect.bottom
        )
