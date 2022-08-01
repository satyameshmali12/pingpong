import pygame

def displaytext(display,text,x,y,size,color,bold,italic):
    font = pygame.font.SysFont(None,size,bold,italic)
    text = font.render(text,True,color)
    display.blit(text,(x,y))

def playmusic(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()

def drawrect(display,color,x,y,sizex,sizey):
    pygame.draw.rect(display,color,(x,y,sizex,sizey))
