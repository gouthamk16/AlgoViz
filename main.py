import pygame
import random
import numpy as np

from bubble import bubble_sort_visualize
from selection import selection_sort_visualize
from insertion import insertion_sort_visualize
from quick import quick_sort_visualize
from merge import merge_sort_visualize

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

algo = input('Which algorithm would you like to visualize (merge, selection, insertion, quick, bubble): ')
n = int(input("Enter number of elements to sort: "))
speed = int(input("Enter delay (lower value -> faster) {1-50}: "))

# Screen settings
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bubble Sort Visualization")

# Array settings
array = list(range(1, n+1))
random.shuffle(array)
bar_width = max(1, width // len(array))
max_value = max(array)
height_multiplier = (height - 50) / max_value  # Adjusting height to fit within the screen

# Function to draw the array
def draw_array(array, color_positions={}):
    screen.fill(BLACK)
    for i, value in enumerate(array):
        color = color_positions.get(i, WHITE)
        rect_height = value * height_multiplier  # Scale height by multiplier
        pygame.draw.rect(screen, color, (i * bar_width, height - rect_height, bar_width, rect_height))
    pygame.display.flip()

def main():
    running = True
    sorting = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True

                    if (algo=="merge"):
                        merge_sort_visualize(array, 0, len(array)-1, speed, draw_array)
                    elif (algo=="quick"):
                        quick_sort_visualize(array, 0, len(array)-1, speed, draw_array)
                    elif (algo=="selection"):
                        selection_sort_visualize(array, speed, draw_array)
                    elif (algo=="insertion"):
                        insertion_sort_visualize(array, speed, draw_array)
                    elif (algo=="bubble"):
                        bubble_sort_visualize(array, speed, draw_array)

                    draw_array(array, {i: GREEN for i in range(0, n+1)})
        
        if not sorting:
            draw_array(array)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()