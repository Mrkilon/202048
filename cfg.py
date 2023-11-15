import os
import pygame

pygame.init()
pygame.quit()

SCREENSIZE = (1580, 930)
BACKGROUND_IMAGE_PATH = 'resources/5.jpg'

background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
background_image = pygame.transform.scale(background_image, SCREENSIZE)

BGMPATH = 'resources/shaonian.mp3'

FONTPATH = os.path.join(os.getcwd(), 'resources/gabriola.ttf')

GAME_MATRIX_SIZE = (4, 4)

MATRIX_SIZE = 100

MARGIN_SIZE = 10

MAX_SCORE_FILEPATH = 'score'

