import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR_PALETTE = {
    pygame.K_1: BLACK,
    pygame.K_2: (255, 0, 0),
    pygame.K_3: (0, 255, 0),
    pygame.K_4: (0, 0, 255),
    pygame.K_5: (255, 255, 0),
}

# Clock for FPS control
clock = pygame.time.Clock()

# Initialize screen
screen.fill(WHITE)

# Variables for drawing
drawing = False
tool = "line"
color = BLACK
start_pos = (0, 0)

# Eraser size
ERASER_SIZE = 20

# Function to draw a square
def draw_square(start_pos, end_pos, color):
    side_length = abs(end_pos[0] - start_pos[0])
    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), side_length, side_length)
    pygame.draw.rect(screen, color, rect, 2)

# Function to draw a right triangle
def draw_right_triangle(start_pos, end_pos, color):
    p1 = start_pos
    p2 = (start_pos[0], end_pos[1])  # Bottom left corner
    p3 = (end_pos[0], end_pos[1])  # Bottom right corner
    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(start_pos, end_pos, color):
    side_length = abs(end_pos[0] - start_pos[0])
    height = (side_length * (3 ** 0.5)) / 2  # Height of an equilateral triangle
    p1 = start_pos
    p2 = (start_pos[0] + side_length, start_pos[1])  # Bottom-right corner
    p3 = ((start_pos[0] + p2[0]) / 2, start_pos[1] - height)  # Top corner
    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

# Function to draw a rhombus
def draw_rhombus(start_pos, end_pos, color):
    center_x = (start_pos[0] + end_pos[0]) // 2
    center_y = (start_pos[1] + end_pos[1]) // 2
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    
    # Calculate the points of the rhombus
    p1 = (center_x, start_pos[1])
    p2 = (start_pos[0], center_y)
    p3 = (center_x, end_pos[1])
    p4 = (end_pos[0], center_y)
    
    pygame.draw.polygon(screen, color, [p1, p2, p3, p4], 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start drawing
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                drawing = True
                if tool == "line":
                    pygame.draw.circle(screen, color, event.pos, 2)

        # Eraser and free line
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "line":
                    pygame.draw.line(screen, color, start_pos, event.pos, 3)
                    start_pos = event.pos
                elif tool == "eraser":
                    pygame.draw.rect(screen, WHITE,
                                     (event.pos[0] - ERASER_SIZE // 2,
                                      event.pos[1] - ERASER_SIZE // 2,
                                      ERASER_SIZE, ERASER_SIZE))

        # Draw shape only on release
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool == "rect":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]),
                                       abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, rect, 2)
                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 +
                                  (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, 2)
                elif tool == "square":
                    draw_square(start_pos, end_pos, color)  # Draw square
                elif tool == "triangle":
                    draw_right_triangle(start_pos, end_pos, color)  # Draw right triangle
                elif tool == "equilateral_triangle":
                    draw_equilateral_triangle(start_pos, end_pos, color)  # Draw equilateral triangle
                elif tool == "rhombus":
                    draw_rhombus(start_pos, end_pos, color)  # Draw rhombus
            drawing = False

        # Tool selection
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_l:
                tool = "line"
            elif event.key == pygame.K_s:
                tool = "square"  # Select square tool
            elif event.key == pygame.K_t:
                tool = "triangle"  # Select right triangle tool
            elif event.key == pygame.K_q:
                tool = "equilateral_triangle"  # Select equilateral triangle tool
            elif event.key == pygame.K_h:
                tool = "rhombus"  # Select rhombus tool
            elif event.key in COLOR_PALETTE:
                color = COLOR_PALETTE[event.key]

    pygame.display.update()
    clock.tick(60)
