import pygame
from app.functions import load_image, lose, resource_path
from app.config import WIDTH, HEIGHT, PLAYER_SPEED, CNT_BULLETS, HEALTH


class Player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.images = {
            'Idle': (6, load_image('app/assets/player/Idle.png')),
            'Run_R': (10, load_image('app/assets/player/Run_R.png')),
            'Run_L': (10, load_image('app/assets/player/Run_L.png')),
        }
        self.status = 'Idle'
        self.image = self.images[self.status][1]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2
        self.vector = set()
        self.bullets = CNT_BULLETS
        self.cnt = 0
        self.frame_delay = 10
        self.frame_counter = 0
        self.bullet_image = load_image('app/assets/bullets/player_bullet.png')
        self.health = HEALTH
        
        
    def update(self, fon):
        if self.health <= 0:
            lose()
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.cnt += 1
            if self.cnt >= self.images[self.status][0]:
                self.cnt = 0
            self.frame_counter = 0

        if self.vector:
            if 'w' in self.vector and self.rect.y - PLAYER_SPEED >= fon.rect.y:
                self.rect.y -= PLAYER_SPEED
                if 'a' in self.vector:
                    self.status = 'Run_L'
                else:
                    self.status = 'Run_R'
            if 'a' in self.vector and self.rect.x - PLAYER_SPEED >= fon.rect.x:
                self.rect.x -= PLAYER_SPEED
                self.status = 'Run_L'
            if 's' in self.vector and self.rect.y + self.rect.height + PLAYER_SPEED <= fon.rect.y + fon.rect.height:
                self.rect.y += PLAYER_SPEED
                if 'a' in self.vector:
                    self.status = 'Run_L'
                else:
                    self.status = 'Run_R'
            if 'd' in self.vector and self.rect.x + self.rect.width + PLAYER_SPEED <= fon.rect.x + fon.rect.height:
                self.rect.x += PLAYER_SPEED
                self.status = 'Run_R'
        else:
            self.status = 'Idle'

        self._update_image()
                
    def take_bullet(self, bullet):
        if self.bullets < CNT_BULLETS:
            pygame.mixer.Sound(resource_path('app/assets/sfx/reload.mp3')).play()
            self.bullets += 1
            bullet.kill()
            
    def get_coordinate(self):
        return self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2
    
    def _update_image(self):
        frame_width = 128
        frame_height = 128
        sprite_sheet = self.images[self.status][1]
        frame_count = self.images[self.status][0]

        frame_x = (self.cnt % frame_count) * frame_width
        self.image = sprite_sheet.subsurface(pygame.Rect(frame_x, 0, frame_width, frame_height)).copy()

        self.rect.size = (frame_width, frame_height)