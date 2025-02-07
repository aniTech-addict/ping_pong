# import the pygame module
import pygame

# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *
# initialize pygame
pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))

# Game Variables
gameOn = True

# Our game loop
while gameOn:
	# for loop through the event queue
	for event in pygame.event.get():
		print(event)



	# Update the display using flip
	pygame.display.flip()
