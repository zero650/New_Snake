import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food constants
SNAKE_SPEED = 15
Foods = []
snake_block = 20
game_over = False

# Initialize clock to manage game speed
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.SysFont(None, 74)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    font = pygame.font.SysFont(None, 64)
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH/6*5, HEIGHT/8])
    
def snakeLoop():
    global game_over
    while not game_over:
        # Check for termination
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_list[-1][0] != 20:
                    snake_move(snake_block, [-20, 0])
                elif event.key == pygame.K_RIGHT and snake_list[-1][0] != -20:
                    snake_move(snake_block, [20, 0])
                elif event.key == pygame.K_UP and snake_list[-1][1] != 20:
                    snake_move(snake_block, [0, -20])
                elif event.key == pygame.K_DOWN and snake_list[-1][1] != -20:
                    snake_move(snake_block, [0, 20])

        screen.fill(BLACK)
        
        # Generate food properly
        if len(Foods) < 1 or not (newFood := [random.randint(0, WIDTH//snake_block)*snake_block,
                                              random.randint(0, HEIGHT//snake_block)*snake_block]):
            while True:
                newFood = [random.randint(0, WIDTH//snake_block)*snake_block,
                          random.randint(0, HEIGHT//snake_block)*snake_block]
                if newFood not in snake_body:
                    break
            Foods.append(newFood)

        for food in foods:
            if food == snake_body[0]:
                snake_body.append(snake_block)
                score += 1
                font = pygame.font.SysFont(None, 64)
                mesg = font.render(f"Score: {score}", True, GREEN)
                screen.blit(mesg, [WIDTH//2 - 50, HEIGHT//8])

        if len(Foods) == 0:
            game_over = True
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        break

    pygame.quit()
    return

# Initializations
snake_body = []
direction = [0, 0]
snakeLoop()