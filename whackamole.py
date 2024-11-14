import pygame
import random

def draw_grid(screen, grid_width, grid_height, square_size):
    # Horizontal lines
    for y in range(0, grid_height * square_size, square_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (grid_width * square_size, y))

    # Vertical lines
    for x in range(0, grid_width * square_size, square_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, grid_height * square_size))

def random_square(grid_width, grid_height):
    # Return a random position within the grid
    return random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)

def main():
    try:
        pygame.init()
        # Mole image
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect()

        #Screen
        grid_width, grid_height = 20, 16
        square_size = 32
        screen = pygame.display.set_mode((grid_width * square_size, grid_height * square_size))
        clock = pygame.time.Clock()

        # Initial position
        mole_x, mole_y = 0, 0
        mole_rect.topleft = (mole_x * square_size, mole_y * square_size)

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get mouse click position
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_x // square_size
                    grid_y = mouse_y // square_size

                    # Check if mole was clicked
                    if grid_x == mole_x and grid_y == mole_y:
                        # Move mole to a random square
                        mole_x, mole_y = random_square(grid_width, grid_height)
                        mole_rect.topleft = (mole_x * square_size, mole_y * square_size)

            screen.fill("light green")
            draw_grid(screen, grid_width, grid_height, square_size)
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
