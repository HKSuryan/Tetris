import time
import pygame
import random
import sys
from pygame.locals import*

pygame.init()

# playing measurements
display_width = 750
display_height = 800
play_width = 500
play_height = 800

# Setting the screen and caption
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TETRIIS')

# Creating an icon
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)


# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
pink = (254, 156, 127)
lblue = (135, 206, 250)
orany = (255, 51, 255)
purple = (204, 153, 255)

colors = [white, red, blue]


# defining global list of coordinates
global lc
lc = []
global shapedata
shapeData = {
    1: {
        0: {0, 25, 50},

        50: {0, 25, 50}
    },
    2: {
        0: {0, 25, 50, 75, 100},

        50: {0, 25, 50, 75, 100},

        100: {0, 25, 50, 75, 100}
    },
    3: {
        0: {0, 25, 50, 75, 100, 125, 150},

        50: {50, 75, 100, 125, 150},

        100: {0, 25, 50}
    },
    4: {
        0: {0, 25, 50, 75, 100},

        50: {0, 25, 50, 75, 100},

        100: {50, 75, 100},

        150: {50, 75, 100}
    },
    5: {
        0: {0, 25, 50, 75, 100},

        50: {0, 25, 50, 75, 100}
    },
    6: {
        0: {0, 25, 50},

        50: {0, 25, 50},

        100: {0, 25, 50}
    },
    7: {
        -50: {50, 75, 100},

        0: {0, 25, 50, 75, 100, 125, 150},

        50: {0, 25, 50, 75, 100, 125, 150},
    },
    8: {
        0: {0, 25, 50},
        50: {50, 75, 100},
        100: {50, 75, 100},
        150: {0, 25, 50}
    },
    9: {
        0: {0, 25, 50, 75, 100, 125, 150},

        50: {0, 25, 50, 75, 100, 125, 150},
        100: {50, 75, 100}
    },
    10: {
        0: {0, 25, 50},
        50: {-50, -25, 0, 25, 50},
        100: {-50, -25, 0, 25, 50},
        150: {0, 25, 50}
    },
    11: {
        0: {0, 25, 50, 75, 100, 125, 150, 175, 200},

        50: {0, 25, 50, 75, 100, 125, 150, 175, 200}
    },
    12: {
        0: {0, 25, 50},

        50: {0, 25, 50},

        100: {0, 25, 50},

        150: {0, 25, 50},

        200: {0, 25, 50}
    }
}
score = 0

usedGrid = {}


def scoree(scor):
    global score
    scor = 0
    score += scor

# defining class of shapes


class shapes:
    def __init__(self, x, y, current):
        self.x = x
        self.y = y
        self.current = current

    def singlepeice(self):
        pygame.draw.rect(screen, white, (self.x, self.y, 44, 44))
        pygame.display.flip()
        return 1

    def square(self):
        pygame.draw.rect(screen, green, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, green, (self.x, self.y+50, 44, 44))
        pygame.draw.rect(screen, green, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, green, (self.x+50, self.y+50, 44, 44))

        pygame.display.flip()
        return 2

    def tree(self):
        pygame.draw.rect(screen, yellow, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, yellow, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, yellow, (self.x, self.y+50, 44, 44))
        pygame.draw.rect(screen, yellow, (self.x+100, self.y, 44, 44))
        pygame.display.flip()

        return 3

    def antitree(self):
        pygame.draw.rect(screen, yellow, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, yellow, (self.x, self.y, 44, 44))

        pygame.draw.rect(screen, yellow, (self.x+50, self.y+100, 44, 44))
        pygame.draw.rect(screen, yellow, (self.x+50, self.y+50, 44, 44))
        pygame.display.flip()
        return 4

    def two(self):
        pygame.draw.rect(screen, lblue, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, lblue, (self.x+50, self.y, 44, 44))
        pygame.display.flip()
        return 5

    def antitwo(self):
        pygame.draw.rect(screen, lblue, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, lblue, (self.x, self.y+50, 44, 44))
        pygame.display.flip()
        return 6

    def trit(self):
        pygame.draw.rect(screen, orany, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+100, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+50, self.y-50, 44, 44))
        pygame.display.flip()
        return 7

    def anttrit1(self):
        pygame.draw.rect(screen, orany, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x, self.y+50, 44, 44))
        pygame.draw.rect(screen, orany, (self.x, self.y+100, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+50, self.y+50, 44, 44))
        pygame.display.flip()
        return 8

    def anttrit2(self):
        pygame.draw.rect(screen, orany, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+100, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x+50, self.y+50, 44, 44))
        pygame.display.flip()
        return 9

    def anttrit3(self):
        pygame.draw.rect(screen, orany, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, orany, (self.x, self.y+50, 44, 44))
        pygame.draw.rect(screen, orany, (self.x, self.y+100, 44, 44))
        pygame.draw.rect(screen, orany, (self.x-50, self.y+50, 44, 44))
        pygame.display.flip()
        return 10

    def bar(self):
        pygame.draw.rect(screen, purple, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, purple, (self.x+50, self.y, 44, 44))
        pygame.draw.rect(screen, purple, (self.x+100, self.y, 44, 44))
        pygame.draw.rect(screen, purple, (self.x+150, self.y, 44, 44))
        pygame.display.flip()
        return 11

    def antibar(self):
        pygame.draw.rect(screen, purple, (self.x, self.y, 44, 44))
        pygame.draw.rect(screen, purple, (self.x, self.y+50, 44, 44))
        pygame.draw.rect(screen, purple, (self.x, self.y+100, 44, 44))
        pygame.draw.rect(screen, purple, (self.x, self.y+150, 44, 44))
        pygame.display.flip()
        return 12

    def check(self):
        coords = shapeData[self.current]
        global usedX
        usedX = None
        y = self.y + list(coords.keys())[len(coords.keys())-1]
        if y == 800:
            return False
        else:
            for key in coords.keys():
                if key == 0:
                    continue
                x = set()

                for value in coords[key]:
                    x.add(self.x+value)

                if self.y+key in usedGrid.keys():
                    usedX = usedGrid[self.y+key]
                    global yt
                    yt = self.y+key
                    intersection = x.intersection(usedX)
                    if len(intersection) > 2:
                        return False

        return True

    def ycheck(self):

        coords = shapeData[self.current]
        y = self.y + list(coords.keys())[len(coords.keys())-1]
        if y == 800:
            return False
        else:
            for key in coords.keys():
                if key == 0:
                    continue
                x = set()

                for value in coords[key]:
                    x.add(self.x+value)

                if self.y+key in usedGrid.keys():
                    usedX = usedGrid[self.y+key]
                    global yt
                    yt = self.y+key

                    intersection = x.intersection(usedX)
                    if len(intersection) == 1:
                        return False

        return True

    def reset(self):
        self.x = 202  # Edited was 402
        self.y = -100


# Defining the player screen
def playscreen(play_width, play_height):
    pygame.draw.rect(screen, red, (0, 0, play_width, play_height), 5)
    pygame.display.update()

# drawing the grid for playing


def drawgrid():
    y = 45
    for i in range(16):
        pygame.draw.line(screen, red, (0, y), (500, y), 2)
        y += 50
        pygame.display.update()

    x = 0
    y = 0

    for i in range(10):
        pygame.draw.line(screen, red, (x, y), (x, 800), 2)
        x += 50

        pygame.display.update()


pygame.display.update()

clock = pygame.time.Clock()


def text(text, col, size, x, y):
    font = pygame.font.SysFont('algerian', size)
    tx = font.render(text, True, col)
    screen.blit(tx, (x, y))


def showscore(scor):
    text("Score", pink, 36, 575, 250)
    text(str(scor), pink, 36, 600, 300)
    pygame.display.update()

# a function to draw the next shape on the player screen


def drwanext(nextshape):
    text("NEXT SHAPE", pink, 36, 545, 500)

    getshapes = shapes(550, 600, current)
    if nextshape == 1:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.singlepeice()
        pygame.display.flip()

    elif nextshape == 2:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.square()
        pygame.display.flip()

    elif nextshape == 3:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.tree()
        pygame.display.flip()

    elif nextshape == 5:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.two()
        pygame.display.flip()

    elif nextshape == 7:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.trit()
        pygame.display.flip()

    elif nextshape == 11:
        pygame.display.flip()
        pygame.draw.rect(screen, black, (550, 550, 200, 200))
        getshapes.bar()
        pygame.display.flip()


def motion():
    y = -100
    x = 202  # changed was 402
    dip = True
    locked_pos = 1
    blockgap = 50
    xchange = 0
    ychange = 0
    e = 0

    current = 0
    getshape = shapes(x, y, current)
    # appending all shapes into a list and then taking a random shape
    global l, lc, s, nextshape
    l = [getshape.two(), getshape.trit(), getshape.bar(), getshape.singlepeice(), getshape.square(), getshape.tree()  # getshape.two(), getshape.trit(), getshape.bar(),getshape.singlepeice(), getshape.square(), getshape.tree()
         ]

    if nextshape == -1:
        current = random.choice(l)
        nextshape = random.choice(l)
    else:
        current = nextshape
        nextshape = random.choice(l)

    drwanext(nextshape)
    showscore(scor)

    while dip:
        h = 0
        l = []
        e = 0

        getshape = shapes(x, y, current)

        getshape = shapes(x, y, current)

# ----------------------------------------------------------------------------------------------------------------------------------
# the main window


def mainwin():
    run = True
    global lc, scor
    global current, nextshape, usedX, yt
    current = -1
    nextshape = -1
    scor = 0

    while run:

        if 0 not in usedGrid.keys():
            playscreen(play_width, play_height)
            drawgrid()
            motion()

            xc = {2, 27, 52, 77, 102, 127, 152, 177, 202, 227, 252, 277, 302, 327, 352, 377, 402,
                  427, 452, 477, 502}
            for k in usedGrid:
                xch = usedGrid[k]
                if k == 800:
                    pass

                else:
                    if len(xch) == len(xc):
                        for i in xc:
                            pygame.display.update()
                            pygame.draw.rect(screen, black, (i, k, 44, 44))
                            pygame.display.update()
                        usedGrid[k] = set()
                        scor += 10

            pygame.display.update()
            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()
                else:
                    continue

        else:
            from Highscore import GameOver
            GameOver(score)
