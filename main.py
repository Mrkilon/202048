import pygame
import sys
from sys import exit
from game2048 import *
from utils import *
import cfgs
from endInterface import *
import os
import subprocess


screen, game_2048 = 0, 0

class Config:
    # Параметры экрана
    SCREENSIZE = (1580, 930)

    # Параметры кнопок
    button_color = (128, 0, 255)
    button_text_color = (255, 255, 255)
    # Пути к изображениям фона и кнопок меню
    MENU_BACKGROUND_IMAGE_PATH = "resources/1.png"

    # Прямоугольники кнопок
    play_button_rect = pygame.Rect(700, 300, 200, 50)
    settings_button_rect = pygame.Rect(700, 400, 200, 50)
    quit_button_rect = pygame.Rect(700, 500, 200, 50)

    # Путь к музыке
    BGMPATH = "resources/shaonian.mp3"

def init(cfg):
    global screen, game_2048
    pygame.init()
    pygame.mixer.music.load(cfg.BGMPATH)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode(cfg.SCREENSIZE, 0, 32)
    pygame.display.set_caption("2048 game - Mrkilon")
    game_2048 = Game2048(matrix_size=cfgs.GAME_MATRIX_SIZE, max_score_filepath=cfgs.MAX_SCORE_FILEPATH)

    # Загрузка фонового изображения для меню
    cfg.menu_background_image = pygame.image.load(cfg.MENU_BACKGROUND_IMAGE_PATH)
    cfg.menu_background_image = pygame.transform.scale(cfg.menu_background_image, cfg.SCREENSIZE)

    # Загрузка шрифта для текста на кнопках
    cfg.button_font = pygame.font.Font(None, 36)

    # Создание текста для кнопок
    cfg.play_text = cfg.button_font.render("ИГРАТЬ", True, cfg.button_text_color)
    cfg.settings_text = cfg.button_font.render("НАСТРОЙКИ", True, cfg.button_text_color)
    cfg.quit_text = cfg.button_font.render("ВЫЙТИ", True, cfg.button_text_color)


def draw_menu(screen, cfg):
    # Отрисовываем фон
    screen.blit(cfg.menu_background_image, (0, 0))

    # Отрисовываем кнопки
    pygame.draw.rect(screen, cfg.button_color, cfg.play_button_rect)
    pygame.draw.rect(screen, cfg.button_color, cfg.settings_button_rect)
    pygame.draw.rect(screen, cfg.button_color, cfg.quit_button_rect)

    # Отрисовываем текст на кнопках
    screen.blit(cfg.play_text, cfg.play_button_rect)
    screen.blit(cfg.settings_text, cfg.settings_button_rect)
    screen.blit(cfg.quit_text, cfg.quit_button_rect)


    pygame.display.update()


def game_loop(cfg):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if cfg.quit_button_rect.collidepoint(mouse_pos):
                return False  # Завершаем выполнение программы
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                game_2048.setDirection({
                    pygame.K_UP: 'UP',
                    pygame.K_DOWN: 'DOWN',
                    pygame.K_LEFT: 'LEFT',
                    pygame.K_RIGHT: 'RIGHT'
                }[event.key])

    game_2048.update()
    return True

if __name__ == '__main__':


    cfg = Config()
    init(cfg)

    count=0
    run = True
    game = False
    while run:
        if not game:
            draw_menu(screen, cfg)

        mouse_pos = pygame.mouse.get_pos()
        if cfg.play_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            game = True
            game_2048.__init__()
        elif cfg.settings_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            # Открываем настройки
            pass

        if game:
            if not count:
                count+=1
                init(cfg)
            screen.blit(pygame.image.load(cfgs.BACKGROUND_IMAGE_PATH), (0, 0))

            drawGameMatrix(screen, game_2048.game_matrix, cfgs)
            (start_x, start_y) = drawScore(screen, game_2048.score, game_2048.max_score, cfgs)
            drawGameIntro(screen, start_x, start_y, cfgs)
            pygame.display.update()

        if not game_loop(cfg):
            break