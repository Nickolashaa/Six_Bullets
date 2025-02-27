import pygame
from app.functions import load_image, resource_path
from app.config import BULLETS_SPEED
from random import randint


class Bullet(pygame.sprite.Sprite):
    def __init__(self, *group, vector=None, unit=None, fon=None):
        super().__init__(*group)
        self.vector = vector
        self.unit = unit
        if unit is None and vector is None:
            self.image = load_image('app/assets/bullets/bullet.png')
            self.rect = self.image.get_rect()
            self.rect.x = randint(20, fon.rect.width - self.rect.width - 1 - 20)
            self.rect.y = randint(20, fon.rect.height - self.rect.height - 1 - 20)
        else:
            if unit.bullets > 0:
                pygame.mixer.Sound(resource_path('app/assets/sfx/attack.mp3')).play()
                unit.bullets -= 1
                self.image = unit.bullet_image
                self.rect = self.image.get_rect()
                if self.unit.status == 'Run_L':
                    self.rect.x = unit.rect.x + unit.rect.width // 2 + 48
                else:
                    self.rect.x = unit.rect.x + unit.rect.width // 2 - 48
                
                self.rect.y = unit.rect.y + unit.rect.height // 2 + 16
                self.vector = vector
                if self.vector == 'w':
                    self.rect.y -= unit.rect.height // 2
                    self.rect.x += unit.rect.width // 3
                if self.vector == 's':
                    self.rect.y += unit.rect.height // 2
                    self.rect.x += unit.rect.width // 3
                if self.vector == 'd':
                    self.rect.x += unit.rect.width // 2
            else:
                self.kill()
    
    def update(self, fon, enemys):
        for enemy in enemys:
            if enemy.rect.colliderect(self.rect) and self.unit:
                enemy.health -= 1
                self.kill()
                return
        
        if self.vector:
            if self.vector == 'w':
                self.rect.y -= BULLETS_SPEED
            if self.vector == 'a':
                self.rect.x -= BULLETS_SPEED
            if self.vector == 's':
                self.rect.y += BULLETS_SPEED
            if self.vector == 'd':
                self.rect.x += BULLETS_SPEED
        
                if not fon.rect.colliderect(self.rect):
                    self.kill()