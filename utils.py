import pygame
import cfgs
def getColorByNumber(number):
    number2Color_dict = {2: ['#8b00ff', '#000000'], 4: ['#6600ff', '#000000'], 8: ['#9400D3', '#000000'],
                         16: ['#8000FF', '#000000'], 32: ['#8A2BE2', '#000000'], 64: ['#8b00ff', '#000000'],
                         128: ['#9400D3', '#000000'], 256: ['#5b30a6', '#000000'], 512: ['#9400d3', '#000000'],
                         1024: ['#8A2BE2', '#000000'], 2048: ['#9400D3', '#000000'], 4096: ['#6600ff', '#000000'],
                         8192: ['#c1caca', '#000000'], 16384: ['#ffffff', '#000000'], 32768: ['#ffffff', '#000000'],
                         65536: ['#f67c5f', '#000000'], 'null': ['#0000cc', None]}
    return number2Color_dict[number]


# Нарисуйте игровой площадь
def drawGameMatrix(screen, game_matrix, cfgs):
    for i in range(len(game_matrix)):
        for j in range(len(game_matrix[i])):
            number = game_matrix[i][j]
            x = (j + 57) * cfgs.MARGIN_SIZE + j * cfgs.MATRIX_SIZE
            y = (i + 26) * cfgs.MARGIN_SIZE + i * cfgs.MATRIX_SIZE

            pygame.draw.rect(screen, pygame.Color(getColorByNumber(number)[0]),
                             (x, y, cfgs.MATRIX_SIZE, cfgs.MATRIX_SIZE))
            # print('game_matrix[{0}][{1}]={2}'.format(i, j, number))

            if number != 'null':
                font_color = pygame.Color(getColorByNumber(number)[1])
                font_size = cfgs.MATRIX_SIZE - cfgs.MARGIN_SIZE * len(str(number))
                font = pygame.font.Font(cfgs.FONTPATH, font_size)
                text = font.render(str(number), True, font_color)
                text_rect = text.get_rect()
                text_rect.centerx, text_rect.centery = x + cfgs.MATRIX_SIZE / 2.1, y + cfgs.MATRIX_SIZE / 1.5
                screen.blit(text, text_rect)


def drawScore(screen, score, max_score, cfgs):
    font_color = (255, 255, 255, 2)
    font_size = 55
    font = pygame.font.Font(cfgs.FONTPATH, font_size)
    text_score = font.render('Счёт сейчас:  ' + str(score), True, font_color)
    text_max_score = font.render('Лучший счёт:  ' + str(max_score), True, font_color)
    start_x = cfgs.GAME_MATRIX_SIZE[1] * cfgs.MATRIX_SIZE + (cfgs.GAME_MATRIX_SIZE[1] + 1) * cfgs.MARGIN_SIZE
    screen.blit(text_max_score, (start_x + 150, 175))
    screen.blit(text_score, (start_x + 255, 645 + text_score.get_height()))
    start_y = 40 + text_score.get_height() * 2

    return (start_x, start_y)


# Введение игры #draw
def drawGameIntro(screen, start_x, start_y, cfgs):
    start_y += 40
    font_color = (255, 255, 255)
    font_size_big = 50
    font_size_small = 50
    font_big = pygame.font.Font(cfgs.FONTPATH, font_size_big)
    font_small = pygame.font.Font(cfgs.FONTPATH, font_size_small)
    intros = ''
    for idx, intro in enumerate(intros):
        font = font_big if idx == 0 else font_small
        text = font.render(intro, True, font_color)
        screen.blit(text, (start_x + 15, start_y))
        start_y += font.get_height() + 10