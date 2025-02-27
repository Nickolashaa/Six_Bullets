import pygame
from app.config import CAMERA_WIDTH, CAMERA_HEIGHT, WIDTH, HEIGHT, CAMERA_SPEED

class Camera():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, CAMERA_WIDTH, CAMERA_HEIGHT)
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2

    def move(self, player, group):
        moves = list()

        if player.rect.x + player.rect.width > self.rect.x + self.rect.width:
            moves.append('right')
        if player.rect.x < self.rect.x:
            moves.append('left')
        if player.rect.y < self.rect.y:
            moves.append('up') 
        if player.rect.y + player.rect.height > self.rect.y + self.rect.height:
            moves.append('down')

        for move in moves:
            for sprite in group:
                if move == 'right':
                    sprite.rect.x -= CAMERA_SPEED
                if move == 'left':
                    sprite.rect.x += CAMERA_SPEED
                if move == 'up':
                    sprite.rect.y += CAMERA_SPEED
                if move == 'down':
                    sprite.rect.y -= CAMERA_SPEED
        
