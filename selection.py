import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen settings
# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Selection Sort Visualization")

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

# Selection Sort function with visualization
def selection_sort_visualize(array, speed, draw_array):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_array(array, {i: RED, j: GREEN, min_idx: GREEN})
            pygame.time.wait(speed)
            if array[j] < array[min_idx]:
                min_idx = j
            draw_array(array, {i: RED, j: GREEN, min_idx: RED})
            pygame.time.wait(speed)
        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(array, {i: GREEN, min_idx: GREEN})
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
#                     bubble_sort_visualize(array)
#                     draw_array(array, {i: GREEN for i in range(1, n+1)})
        
#         if not sorting:
#             draw_array(array)
        
#         pygame.display.flip()

#     pygame.quit()

# if __name__ == "__main__":
#     main()