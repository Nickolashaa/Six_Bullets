import os
import sys
import pygame
from app.config import WIDTH, HEIGHT
import time


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path).replace('/', '\\')


def load_image(path):
    fullpath = resource_path(path)
    # если файл не существует, то выходим
    if not os.path.isfile(fullpath):
        input(f"Файл с изображением '{fullpath}' не найден")
        sys.exit()
    image = pygame.image.load(fullpath)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def lose():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill('black')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                time.sleep(1)
                terminate()
                
        screen.blit(load_image('app/assets/game_over.png'), (0, 0))
        pygame.display.update()
        
def start_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill('black')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                return
                
        screen.blit(load_image('app/assets/start_game.png'), (0, 0))
        pygame.display.update()
        
def end_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill('black')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                time.sleep(1)
                return
                
        screen.blit(load_image('app/assets/win_game.png'), (0, 0))
        pygame.display.update()