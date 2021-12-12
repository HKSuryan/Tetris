import pygame

from pygame.locals import *
import time
pygame.init()
width=1000
height=600

# owner
own=pygame.image.load("owner.png")
xo=0
yo=0

def owner(xo,yo):
    screen.blit(own,(xo,yo))


# defining colors by using RGB
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,64)
black=(1,1,1)
yellow=(255,255,0)


# setting the pygame window
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("TETRIS")
pygame.display.set_icon(pygame.image.load("icon.jpg"))


#TEXT
def text(text,o,p,size,col):
    font=pygame.font.SysFont("algerian",size)
    tx=font.render(text,True,col)
    screen.blit(tx,(o,p))
    

# setting up the player
logoo = pygame.image.load("tetris1.jpg")
x=0
y=0
def logo(xchange,ychange):
    screen.blit(logoo,(xchange,ychange))
# presenter
def present():
    pygame.mixer.music.load('tetris12.mp3')
    pygame.mixer.music.play(-1,)
    
    run = True
    global xo
    j = False
    while run:
       
        if xo >= 1000:
            
            time.sleep(1)
            screen.fill(red)
            logo(x, y)
            pygame.draw.rect(screen, yellow, (0, 490, 415, 110))
            text('WELCOME!!',65,520,45,black)
            
            pygame.draw.rect(screen, yellow, (550, 50, 300, 50))
            text('START',665,55,25,black)
            pygame.draw.rect(screen, yellow, (550, 140, 300, 50))
            text('OPTIONS',665,145,25,black)
            pygame.draw.rect(screen, yellow, (550, 230, 300, 50))
            text('HIGH SCORES',640,235,25,black)
            pygame.draw.rect(screen, yellow, (550, 320, 300, 50))
            text('CREDITS',660,325,25,black)
            pygame.draw.rect(screen, yellow, (550, 410, 300, 50))
            text('CONTROLS',655,415,25,black)
            pygame.draw.rect(screen, yellow, (550, 500, 300, 50))
            text('EXIT',673,505,25,black)
            pygame.draw.rect(screen, yellow, (970, 570, 50, 50))
            text('♬',980,570,25,black)
            for events in pygame.event.get():
                mouse=pygame.mouse.get_pos()
                if events.type == pygame.QUIT: 
                    pygame.quit() 
                if events.type==pygame.MOUSEBUTTONDOWN:
                    if (mouse[0]>=550 and mouse[0]<=850) and (mouse[1]>=500 and mouse[1]<=550):
                        pygame.draw.rect(screen, white, (550, 500, 300, 50))
                        text('EXIT',673,505,25,blue)
                        pygame.display.update()
                        pygame.quit()
                        quit()
                        
                if events.type==pygame.MOUSEBUTTONDOWN:
                    if (mouse[0]>=550 and mouse[0]<=850) and (mouse[1]>=50 and mouse[1]<=100):
                        pygame.draw.rect(screen, white, (550, 50, 300, 50))
                        text('START',665,55,25,black)
                        pygame.display.update()
                        screen.fill(black)
                        screen.fill(blue)
                        text('GAME Starts in 3 .',20,400,65,yellow)
                        pygame.display.update()
                        time.sleep(1)
                        screen.fill(blue)
                        text('GAME Starts in 2 ..',20,400,65,yellow)
                        pygame.display.update()
                        time.sleep(1)
                        screen.fill(blue)
                        text('GAME Starts in 1 ...',20,400,65,yellow)
                        pygame.display.update()
                        time.sleep(1)
                        import Maingame1
                        r=Maingame1.mainwin()
                        time.sleep(100000000)
                        screen.fill(blue)
                        pygame.draw.rect(screen, yellow, (0, 0, 100, 40))
                        text('BACK', 5, 0, 25, black)
                        text('GAME IN MAINTAINANCE',20,400,65,white)
                        pygame.draw.rect(screen, yellow, (0, 0, 100, 40))
                        text('BACK',5,0,25,black)
                        pygame.display.update()
                        k=6
                    
                        pygame.display.update()
                        time.sleep(k)
                        
                        


                if events.type==pygame.MOUSEBUTTONDOWN:
                    if (mouse[0]>=550 and mouse[0]<=850) and (mouse[1]>=140 and mouse[1]<=190):
                        pygame.draw.rect(screen, white, (550, 140, 300, 50))
                        text('OPTIONS',665,145,25,black)
                        pygame.display.update()
                        time.sleep(0.5)
                        screen.fill(black)
                   
                        text('OPTIONS',350,0,65,white)
                       
            
                        pygame.display.update()
                        time.sleep(6)

                    
                if events.type==pygame.MOUSEBUTTONDOWN:
                        
                        if (mouse[0]>=970 and mouse[0]<=1000) and (mouse[1]>=570 and mouse[1]<=600):
                            if j is False:
                                pygame.draw.rect(screen, white, (970, 570, 50, 50))
                                text('♮',970,570,25,black)
                                    
                                pygame.display.update()
                               
                                pygame.mixer.music.pause()
                                j=True
                            else:
                                pygame.draw.rect(screen, white, (970, 570, 50, 50))
                                text('♮',970,570,25,black)
                               
                                pygame.mixer.music.unpause()
                                pygame.display.update()
                                j=False
                            break
                                
                       
                            




        else:
            screen.fill(blue)
            text("T E T R I S",300,300,120,white)
            owner(xo, yo)
            xo += 2.5

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                
        pygame.display.update()

present()

