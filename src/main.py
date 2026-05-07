import pygame # pyright: ignore[reportMissingImports]
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = width, height = 800, 600
screen = pygame.display.set_mode(screen)
#decide the color of the background/window
background_color = (0, 0, 0) #black
#need to fill the background with a color before drawing anything on it, otherwise it will be transparent and you won't see anything
screen.fill(background_color)
#drwaing a rectangle on the screen, the first two parameters are the x and y coordinates of the top left corner of the rectangle, and the last two parameters are the width and height of the rectangle
rect_color = (255, 0, 0) #red
rect_position = (100, 100, 200, 150) #x, y, width, height
pygame.draw.rect(screen, rect_color, rect_position)
# Game loop
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()

        #need to flip the display after drawing everything on it, otherwise you won't see the changes on the screen
        pygame.display.flip()