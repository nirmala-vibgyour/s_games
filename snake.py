import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
color = 'WHITE'
screen.fill(color)
def drawgrid():
    global color
    s=0
    while s<601:
        s1=0
        while s1<601:
            rect = pygame.Rect(s1,s,10,10)
            pygame.draw.rect(screen,'BLACK',rect,1)
            s1=s1+10
            pygame.display.update()   
        s=s+10
    pygame.display.update()
    if color == 'WHITE':
        color='RED'
        for row in range(600):
            rect = pygame.Rect(row,10,10,10)
            pygame.draw.rect(screen,color,rect)
        pygame.display.update()
running=True
while running:
    drawgrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        mouse_pos=[]
        if event.type == pygame.MOUSEMOTION:
            mouse_pos.append(pygame.mouse.get_pos(event))
        for mouse in mouse_pos:
            print(mouse)
pygame.quit()    


