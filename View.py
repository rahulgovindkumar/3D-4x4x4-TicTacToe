import pygame

# Box Width
WI = 48

# Screen Width
SC = 800
SW = 900

# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (125, 200, 35)
RED = (255, 0, 0)
BLUE = (10, 100, 255)
GREY = (128, 128, 128)
CYAN = (5, 204, 171)
LIGHT_GREY = (51, 56, 63)
DARK_GREY = (33, 38, 40)
YELLOW = (255, 217, 0)
ORANGE = (253, 104, 35)
BOX_FRONT = (117, 219, 27)
BOX_BACK = (17, 119, 45)
T_BLUE=(21,106,132)
L_BLUE=(48,192,220)


# Defining View related functions
def drawO(i, j, k, screen):
    pygame.draw.circle(screen, ORANGE, [20 + WI * i + WI * 4 * k + WI / 2, 20 + WI * j + WI * 4 * k + WI / 2],
                       WI / 4, 5)


def drawX(i, j, k, screen):
    pygame.draw.line(screen, YELLOW, [20 + WI / 4 + WI * i + WI * 4 * k, 20 + WI / 4 + WI * j + WI * 4 * k],
                     [20 - WI / 4 + WI * (i + 1) + WI * 4 * k, 20 - WI / 4 + WI * (j + 1) + WI * 4 * k], 10)
    pygame.draw.line(screen, YELLOW, [20 - WI / 4 + WI * (i + 1) + WI * 4 * k, 20 + WI / 4 + WI * j + WI * 4 * k],
                     [20 + WI / 4 + WI * i + WI * 4 * k, 20 - WI / 4 + WI * (j + 1) + WI * 4 * k], 10)


def drawSelected(i, j, k, screen):
    pygame.draw.line(screen, RED, [20 + WI * i + WI * 4 * k, 20 + WI * j + WI * 4 * k],
                     [20 + WI * (i + 1) + WI * 4 * k, 20 + WI * j + WI * 4 * k], 2)
    pygame.draw.line(screen, RED, [20 + WI * i + WI * 4 * k, 20 + WI * j + WI * 4 * k],
                     [20 + WI * i + WI * 4 * k, 20 + WI * (j + 1) + WI * 4 * k], 2)
    pygame.draw.line(screen, RED, [20 + WI * (i + 1) + WI * 4 * k, 20 + WI * j + WI * 4 * k],
                     [20 + WI * (i + 1) + WI * 4 * k, 20 + WI * (j + 1) + WI * 4 * k], 4)
    pygame.draw.line(screen, RED, [20 + WI * i + WI * 4 * k, 20 + WI * (j + 1) + WI * 4 * k],
                     [20 + WI * (i + 1) + WI * 4 * k, 20 + WI * (j + 1) + WI * 4 * k], 4)


def renderBoard(screen, board):
    screen.fill(BLACK)
    for i in range(4):
        pygame.draw.line(screen, L_BLUE, [20 + 4 * WI * i, 20 + 4 * WI * i],
                         [20 + 4 * WI * i, 20 + 4 * WI * i + 4 * WI], 1)
        
        pygame.draw.line(screen, L_BLUE, [20 + 4 * WI * i, 20 + 4 * WI * i],
                         [20 + 4 * WI * i + 4 * WI, 20 + 4 * WI * i], 1)
        pygame.draw.line(screen, L_BLUE, [20 + 4 * WI * i + 4 * WI, 20 + 4 * WI * i + 4 * WI],
                         [20 + 4 * WI * i, 20 + 4 * WI * i + 4 * WI], 4)
        pygame.draw.line(screen, L_BLUE, [20 + 4 * WI * i + 4 * WI, 20 + 4 * WI * i + 4 * WI],
                         [20 + 4 * WI * i + 4 * WI, 20 + 4 * WI * i], 4)
        for j in range(4):
            pygame.draw.line(screen, T_BLUE, [20 + (j + 1) * WI + 4 * WI * i, 20 + 4 * WI * i],
                             [20 + (j + 1) * WI + 4 * WI * i, 20 + 4 * WI * i + 4 * WI], 5)
            pygame.draw.line(screen, T_BLUE, [20 + 4 * WI * i, 20 + (j + 1) * WI + 4 * WI * i],
                             [20 + 4 * WI * i + 4 * WI, 20 + (j + 1) * WI + 4 * WI * i], 5)




    pygame.draw.line(screen, RED, [18, 228], [595, 796], 2)
    pygame.draw.line(screen, RED, [228, 18], [796, 595], 2)
    # pygame.draw.line(screen, RED, [275, 275], [725, 725], 2)

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                if board.getPosition(i, j, k) == 1:
                    drawX(i, j, k, screen)
                elif board.getPosition(i, j, k) == 2:
                    drawO(i, j, k, screen)


def showMode(screen, mode, font, font2):
    tex = font2.render("press Key P to change Player", True, WHITE)
    texRect = tex.get_rect()
    texRect.center = (725, 140)
    screen.blit(tex, texRect)

    if mode == 1:
        screen.blit(font.render("X first", True, RED), (620, 85))
        screen.blit(font.render("O first", True, GREY), (740, 85))
    else:
        screen.blit(font.render("X first", True, GREY), (620, 85))
        screen.blit(font.render("O first", True, RED), (740, 85))

def showLevel(screen, level, font, font2):
    tex = font2.render("press L key to change Level", True, WHITE)
    texRect = tex.get_rect()
    texRect.center = (725, 370)
    screen.blit(tex, texRect)
    

    if level == 1:
        screen.blit(font.render("Easy", True, RED), (680, 200))
        screen.blit(font.render("Medium", True, GREY), (680, 250))
        screen.blit(font.render("Hard", True, GREY), (680, 300))
    elif level ==2:
        screen.blit(font.render("Easy", True, GREY), (680, 200))
        screen.blit(font.render("Medium", True, RED), (680, 250))
        screen.blit(font.render("Hard", True, GREY), (680, 300))

    else:
        screen.blit(font.render("Easy", True, GREY), (680, 200))
        screen.blit(font.render("Medium", True, GREY), (680, 250))
        screen.blit(font.render("Hard", True, RED), (680, 300))


# Function to get coordinated from mouse click
def getPoints(event):
    x = ((event.pos[0] - 50) // WI) % 4
    y = ((event.pos[1] - 50) // WI) % 4
    z = ((event.pos[0] - 50) // WI) // 4

    if int(int(int(event.pos[0] - 50) / WI) / 4) != int(int(int(event.pos[1] - 50) / WI) / 4):
        z = -1

    return x, y, z


# Function to parse time
def format_time(secs):
    secs = int(secs)
    sec = secs % 60
    minute = secs // 60

    s = str(sec)
    m = str(minute)

    if len(s) == 1:
        s = '0' + s

    if len(m) == 1:
        m = '0' + m

    mat = " " + m + ":" + s
    return mat
