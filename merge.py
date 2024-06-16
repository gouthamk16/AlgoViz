import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen settings
# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Merge Sort Visualization")

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

# Merge Sort function with visualization
def merge_sort_visualize(array, l, r, speed, draw_array):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_visualize(array, l, m, speed, draw_array)
        merge_sort_visualize(array, m + 1, r, speed, draw_array)
        merge(array, l, m, r, draw_array, speed)
        draw_array(array, {i: GREEN for i in range(l, r + 1)})
        pygame.time.wait(speed)

def merge(array, l, m, r, draw_array, speed):
    n1 = m - l + 1
    n2 = r - m

    L = array[l:m + 1]
    R = array[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        draw_array(array, {k: RED})
        pygame.time.wait(speed)
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        draw_array(array, {k: RED})
        pygame.time.wait(speed)
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        draw_array(array, {k: RED})
        pygame.time.wait(speed)
        k += 1

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
#                     merge_sort_visualize(array, 0, len(array) - 1)
        
#         if not sorting:
#             draw_array(array)
        
#         pygame.display.flip()

#     pygame.quit()

# if __name__ == "__main__":
#     main()
