import random
import View
import pygame
import time
from Board import Board
from View import SC, SW

pygame.init()
pygame.mixer.music.load('resources/start.mp3')
pygame.mixer.music.play(0)
pygame.display.set_caption("3D 4x4x4 TicTacToe ~ by Team 1")
programIcon = pygame.image.load('resources/icon-1.png')
pygame.display.set_icon(programIcon)

size = (SW, SC)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("consolas", 18)
font_time = pygame.font.SysFont("comicsans", 20)

board = Board()
start = time.time()
me, you, turn = 0, 0, 1
x, y, z = (-1, -1, -1)
playing = True
MODE = 1
LEVEL = 1


def initBoard():
    global board, turn, x, y, z
    board = Board()
    turn = 1
    if MODE == 1:
        x, y, z = (-1, -1, -1)
    else:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        k = random.randint(0, 3)
        board.setPosition(i, j, k, 2)
        x, y, z = (-1, -1, -1)

    View.showMode(screen, MODE, font, font2)
    View.showLevel(screen, LEVEL, font, font2)


while playing:
    View.renderBoard(screen, board)
    play_time = int(round(time.time() - start))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.MOUSEMOTION:
            x, y, z = View.getPoints(event)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                MODE = MODE % 2 + 1
                #play music
                pygame.mixer.music.load('resources/player.mp3')
                pygame.mixer.music.play(0)
                initBoard()

            if event.key == pygame.K_l:
                LEVEL = LEVEL % 3 + 1
                print("LEVEL",LEVEL)
                #play music
                pygame.mixer.music.load('resources/level.mp3')
                pygame.mixer.music.play(0)
                initBoard()

      
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (0 <= x <= 3) & (0 <= y <= 3) & (0 <= z <= 3):
                    if board.getPosition(x, y, z) == 0 and turn == 1:
                        board.setPosition(x, y, z, 1)
                        #play music
                        
                        pygame.mixer.music.load('resources/play.mp3')
                        pygame.mixer.music.play(0)
                        if board.isWin(1):
                            you += 1
                        turn = 2
            elif event.button == 3:
                if (not board.isEmpty()) | board.isWin(1) | board.isWin(2):
                    initBoard()
        

    if (0 <= x <= 3) & (0 <= y <= 3) & (0 <= z <= 3):
        View.drawSelected(x, y, z, screen)

    if board.isWin(1):
        text = font.render(' You have won the game ! Right Click to Restart ', True, View.YELLOW, View.LIGHT_GREY)
        textRect = text.get_rect()
        textRect.center = (SW / 2, SC / 2)
        screen.blit(text, textRect)
        turn = 0

    elif turn == 2:
        screen.blit(font.render("Loading...", True, View.WHITE), (500, 100))
        pygame.display.flip()
        a, b, c = board.findMax(LEVEL)
        if (0 <= a <= 3) & (0 <= b <= 3) & (0 <= c <= 3):
            #check later
            board.setPosition(a, b, c, 2)
            if board.isWin(2):
                me += 1
        turn = 1

    elif not board.isEmpty():
        text = font.render(' Draw , Right Click to Restart', True, View.LIGHT_GREY, View.LIGHT_GREY)
        textRect = text.get_rect()
        textRect.center = (SW / 2, SC / 2)
        screen.blit(text, textRect)
        turn = 0

    if board.isWin(2):
        text = font.render(' Bot has won the game ! Right Click to Restart ', True, View.ORANGE, View.LIGHT_GREY)
        textRect = text.get_rect()
        textRect.center = (SW / 2, SC / 2)
        screen.blit(text, textRect)
        turn = 0

    View.showMode(screen, MODE, font, font2)
    View.showLevel(screen, LEVEL, font, font2)
    screen.blit(font_time.render(" Time: " + View.format_time(play_time),
                            True, View.GREY), (750, 20))

    screen.blit(font.render(" You: " + str(you) + "   Bot: " + str(me) + ' ',
                            True, View.GREY), (50, 740))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
