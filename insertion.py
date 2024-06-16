import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen settings
# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Insertion Sort Visualization")

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # n = int(input("Enter number of elements to sort: "))
# n = 100

# # Array settings
# array = list(range(1, n+1))
# random.shuffle(array)
# bar_width = width // len(array)
# height_multiplier = 5  # Multiplier to increase height

# # Function to draw the array
# def draw_array(array, color_positions={}):
#     screen.fill(BLACK)
#     for i, value in enumerate(array):
#         color = color_positions.get(i, WHITE)
#         rect_height = value * height_multiplier  # Scale height by multiplier
#         pygame.draw.rect(screen, color, (i * bar_width, height - rect_height, bar_width, rect_height))
#     pygame.display.flip()

# Insertion Sort function with visualization
def insertion_sort_visualize(array, speed, draw_array):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            draw_array(array, {j: RED, j + 1: GREEN})
            pygame.time.wait(speed)
            j -= 1
        array[j + 1] = key
        draw_array(array, {i: GREEN})
        pygame.time.wait(speed)

# Main function
# def main():
#     running = True
#     sorting = False

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE and not sorting:
#                     sorting = True
#                     insertion_sort_visualize(array)
#                     draw_array(array, {i : GREEN for i in range(1, n+1)})
#                 if event.key == pygame.K_ESCAPE:  # Press Escape key to exit
#                     running = False
        
#         if not sorting:
#             draw_array(array)
        
#         pygame.display.flip()

#     pygame.quit()

# if __name__ == "__main__":
#     main()
