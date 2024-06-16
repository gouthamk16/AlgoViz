import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen settings
# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Quick Sort Visualization")

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

RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Quick Sort function with visualization
def quick_sort_visualize(array, low, high, speed, draw_array):
    if low < high:
        pi = partition(array, low, high, speed, draw_array)
        draw_array(array, {pi: GREEN})
        pygame.time.wait(speed)
        quick_sort_visualize(array, low, pi - 1, speed, draw_array)
        quick_sort_visualize(array, pi + 1, high, speed, draw_array)

def partition(array, low, high, speed, draw_array):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            draw_array(array, {i: RED, j: GREEN})
            pygame.time.wait(speed)
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# # Main function
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
#                     quick_sort_visualize(array, 0, len(array) - 1)
#                     draw_array(array, {i: GREEN for i in range(1, n+1)})
        
#         if not sorting:
#             draw_array(array)
        
#         pygame.display.flip()

#     pygame.quit()

# if __name__ == "__main__":
#     main()
