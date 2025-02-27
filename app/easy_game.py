import pygame
from app.functions import terminate, load_image, resource_path
from app.config import *
from app.player import Player
from app.fon import Fon
from app.camera import Camera
from app.bullet import Bullet
from app.enemy import Enemy
from app.progressbar import ProgressBar


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Six Bullets')
icon = load_image("app/assets/favicon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
fon_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
progressBar_sprites = pygame.sprite.Group()
SPAWN_BULLET = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BULLET, 3000)
SPAWN_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_ENEMY, 5000)
font = pygame.font.Font(None, 128)
pygame.mixer.init()
pygame.mixer.music.load(resource_path('app/assets/sfx/fon.mp3'))
pygame.mixer.music.play(-1)
enemy_sound = pygame.mixer.Sound(resource_path('app/assets/sfx/enemy.mp3'))
reload_sound = pygame.mixer.Sound(resource_path('app/assets/sfx/reload.mp3'))


fon = Fon(fon_sprites, all_sprites)
player = Player(player_sprites, all_sprites)
player.rect.x = WIDTH // 2 - player.rect.width // 2
camera = Camera()
progressBar = ProgressBar(CNT_ENEMY, progressBar_sprites)


def easy_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.vector.add('w')
                if event.key == pygame.K_a:
                    player.vector.add('a')
                if event.key == pygame.K_s:
                    player.vector.add('s')
                if event.key == pygame.K_d:
                    player.vector.add('d')
                if event.key == pygame.K_UP:
                    Bullet(bullet_sprites, all_sprites, vector='w', unit=player)
                if event.key == pygame.K_DOWN:
                    Bullet(bullet_sprites, all_sprites, vector='s', unit=player)
                if event.key == pygame.K_LEFT:
                    Bullet(bullet_sprites, all_sprites, vector='a', unit=player)
                if event.key == pygame.K_RIGHT:
                    Bullet(bullet_sprites, all_sprites, vector='d', unit=player)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.vector.discard('w')
                if event.key == pygame.K_a:
                    player.vector.discard('a')
                if event.key == pygame.K_s:
                    player.vector.discard('s')
                if event.key == pygame.K_d:
                    player.vector.discard('d')
                    
            if event.type == SPAWN_BULLET:
                for _ in range(3):
                    Bullet(bullet_sprites, all_sprites, fon=fon)
                    
            if event.type == SPAWN_ENEMY:
                if progressBar.current_value > progressBar.max_value // 2:
                    for _ in range(3):
                        Enemy(enemy_sprites, all_sprites, level=2, fon=fon, target=player, progressBar = progressBar)
                else:
                    for _ in range(2):
                        Enemy(enemy_sprites, all_sprites, level=1, fon=fon, target=player, progressBar = progressBar)
            

        player.update(fon)
        for bullet in bullet_sprites:
            if bullet.vector is None and player.rect.colliderect(bullet.rect):
                player.take_bullet(bullet)
                
        
        
        camera.move(player, all_sprites)
        
        
        bullet_sprites.update(fon, enemy_sprites)
        enemy_sprites.update(enemy_sprites)
        
        screen.fill('black')
        fon_sprites.draw(screen)
        bullet_sprites.draw(screen)
        enemy_sprites.draw(screen)
        player_sprites.draw(screen)
        progressBar_sprites.draw(screen)
        screen.blit(font.render(f"{player.bullets}/{CNT_BULLETS}", True, (255, 201, 15)), (WIDTH - 150, HEIGHT - 100))
        
        
        pygame.display.flip()
        clock.tick(FPS)
        
        if progressBar.current_value == progressBar.max_value:
            return