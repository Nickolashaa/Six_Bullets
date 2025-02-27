import pygame
from random import randint
from app.functions import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group, level, fon, target, progressBar):
        super().__init__(*group)
        self.level = level
        self.target = target
        self.progressBar = progressBar
        self.image = load_image(f'app/assets/enemy/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, fon.rect.width - 20)
        self.rect.y = randint(20, fon.rect.height - 20)
        self.speed = self.level * 1.5
        self.health = 1

    def update(self, enemys):
        if self.health <= 0:
            self.kill()
            self.progressBar.add_progress(1)
            return
        
        if self.rect.colliderect(self.target.rect):
            self.target.health -= 1
            self.kill()
        
        target_pos = pygame.Vector2(self.target.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        
        direction = (target_pos - enemy_pos).normalize() if enemy_pos != target_pos else pygame.Vector2()
        
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed

        collided_enemies = pygame.sprite.spritecollide(self, enemys, False)
        for other_enemy in collided_enemies:
            if other_enemy != self:
                push_direction = pygame.Vector2(self.rect.center) - pygame.Vector2(other_enemy.rect.center)
                if push_direction.length() > 0:
                    push_direction = push_direction.normalize()
                self.rect.x += push_direction.x * self.speed
                self.rect.y += push_direction.y * self.speed
