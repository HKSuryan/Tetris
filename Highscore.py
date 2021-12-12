import pygame
from pygame.locals import*

pygame.init()

# playing measurements
display_width = 1000
display_height = 800

screen = pygame.display.set_mode((display_width,display_height))

white=(255, 255, 255)

def text(text,col,size,x,y):
    font=pygame.font.SysFont('algerian',size)
    tx=font.render(text,True,col)
    screen.blit(tx,(x,y))

def GameOver(score):
    while True:
        text("Game Over :(",white,48,400,300)
        text(f'Your score: {score}',white,48,400,500)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
