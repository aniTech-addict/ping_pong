# import the pygame module
import pygame

# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *
# initialize pygame
pygame.init()

# setting game window
pygame.display.set_caption('Badminton Game')
img = pygame.image.load('logo.jpg')
pygame.display.set_icon(img)

# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))

# Game Variables
gameOn = True
SPEED = 5
player1_score = 0
player2_score = 0

# Our game loop
while gameOn:
	# for loop through the event queue
	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT:
			print(event)
			gameOn = not gameOn

	screen.fill((255, 255, 255))

	#border
	pygame.draw.rect(screen,"black", (0, 0, 800, 600),2)
	
	
	# Game Objects
	player1_pos = pygame.Vector2(30, screen.get_height()/2-50)
	player2_pos = pygame.Vector2(760, screen.get_height()/2-50)
	
	player1 = pygame.draw.rect(screen,"blue", (30, player1_pos.y, 10, 100),0)
	player2 = pygame.draw.rect(screen,"green", (760,  player2_pos.y, 10, 100),0)

	ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
	ball = pygame.draw.circle(screen,"red", (ball_pos.x, ball_pos.y), 10, 0)

	# Movement Controls

	keys = pygame.key.get_pressed()

	if keys[pygame.K_w]  : #Prevent movement in reverse direction
		player1_pos.y += SPEED

	if keys[pygame.K_s] : #Prevent movement in reverse direction
		player1_pos.y += -SPEED
        
        


	# Update the display using flip
	pygame.display.flip()
