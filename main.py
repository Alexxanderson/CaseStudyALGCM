import pygame


def main():
    # read txt file and print 2d maze grid
    print("Yo")
    # Initialize Pygame
    pygame.init()

    # Define the dimensions of the window
    window_width = 800
    window_height = 600

    # Create the window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("1-Way 1-Stack Deterministic Pushdown Automata")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    circles = []

    # Flag for "adding mode"
    adding_mode = False

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add a circle's position when the mouse is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                circles.append((mouse_x, mouse_y))


        # Fill the window with a color (white in this case)
        window.fill(WHITE)

        # Draw all circles on the window
        for circle_pos in circles:
            pygame.draw.circle(window, BLACK, circle_pos, 20)  # Draw a circle with radius 20

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
