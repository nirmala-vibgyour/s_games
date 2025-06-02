import pygame
import random

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
        s=s+10
    pygame.display.update()

# Initialize snake and food
snake=[(30, 30)]
direction=(1,0)
food=(random.randint(0,59)*10, random.randint(0,59)*10)

clock=pygame.time.Clock()
running=True

while running:
    clock.tick(10) # control game speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction !=(0,1):
                direction=(0,-1)
            elif event.type == pygame.K_DOWN and direction !=(0,-1):
                direction=(0,1)
            elif event.type == pygame.K_LEFT and direction !=(1,0):
                direction=(-1,0)
            elif event.type == pygame.K_RIGHT and direction !=(-1,0):
                direction=(1,0)

    # Move the snake
    head_x, head_y = snake[-1]
    new_head=(head_x + direction[0]*10, head_y + direction[1]*10)
    snake.append(new_head)
    
    # Check if snake eats food
    if new_head == food:
        food = (random.randint(0, 59)*10, random.randint(0, 59)*10
    else:
        snake.pop()
    
    if (
        new_head in snake[:-1] or
        new_head[0] < 0 or new_head[0] >= 600 or
        new_head[1] < 0 or new_head[1] >= 600
    ):
        running = False
    
    # Draw the snake
    for segment in snake:
        rect = pygame.Rect(segment[0], segment[1], 10, 10)
        pygame.draw.rect(screen, 'GREEN', rect)
    
    rect = pygame.Rect(food[0], food[1], 10, 10)
    pygame.draw.rect(screen, 'RED', rect)
    
    pygame.display.update()
pygame.quit()    


