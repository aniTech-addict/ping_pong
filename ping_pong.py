# import the pygame module
import pygame
import random

# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *
# initialize pygame
pygame.init()

# setting game window
pygame.display.set_caption('Badminton Game')
img = pygame.image.load('logo.jpg')
pygame.display.set_icon(img)
font = pygame.font.SysFont(None, 50)
border = (800,600)
# Define the dimensions of screen object
screen = pygame.display.set_mode((border))

# Game Variables
gameOn = True
gameOver = False
SPEED = 0.5
player1_score = 0
player2_score = 0
player1_pos = pygame.Vector2(30, screen.get_height()/2-50)
player2_pos = pygame.Vector2(760, screen.get_height()/2-50)
ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

# Ball movement variables
ball_velocity = pygame.Vector2(random.choice([-1, 1]), random.choice([-1, 1]))  # Random initial direction
ball_velocity.scale_to_length(3)  # Set speed of the ball

# Function
def text_screen(text, color, x, y):
    screen_print = font.render(text, True, color)
    screen.blit(screen_print, (x, y))

# Our game loop
while gameOn:
	# for loop through the event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print(event)
			gameOn = not gameOn

		if (ball_pos.x > screen.get_width() or ball_pos.x < 0) :
			gameOn = not True
			print("game over")
			while not exit_game:
				screen.fill("black")
				text_screen("Game Over", "red", screen.get_width() / 2, screen.get_height() / 2)
				text_screen("Player 1 : "+str(player1_score),"red",screen.get_width()/2,screen.get_height()/2+50)
				text_screen("Player 2 : "+str(player2_score),"red",screen.get_width()/2,screen.get_height()/2+50)
				pygame.display.update()
				pygame.time.delay(5000)
				exit_game = True

	screen.fill((255, 255, 255))

	# Border
	pygame.draw.rect(screen,"black", (0, 0, 800, 600),2)
	
	player1_rect = [30, player1_pos.y, 10, 100]
	player2_rect = [760,  player2_pos.y, 10, 100]
	# Game Objects
	pygame.draw.rect(screen,"blue", player1_rect,0)
	pygame.draw.rect(screen,"green", player2_rect,0)

	ball = pygame.draw.circle(screen,"red", (ball_pos.x, ball_pos.y), 10, 0)

	# Movement Controls
	keys = pygame.key.get_pressed()

	if keys[pygame.K_w] and player1_pos.y > 0:
		player1_pos.y -= SPEED

	if keys[pygame.K_s] and player1_pos.y < screen.get_height() - 100:
		player1_pos.y += SPEED

	if keys[pygame.K_UP] and player2_pos.y > 0:
		player2_pos.y -= SPEED

	if keys[pygame.K_DOWN] and player2_pos.y < screen.get_height() - 100:
		player2_pos.y += SPEED

	# Update ball position
	ball_pos += ball_velocity

	# Check for ball collision with top and bottom borders
	if ball_pos.y <= 0 or ball_pos.y >= screen.get_height():
		ball_velocity.y *= -1  # Reverse Y direction

	pygame.display.update()

	# Update the display using flip
