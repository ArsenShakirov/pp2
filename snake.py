import pygame
import random

pygame.init()

width = 400
height = 400
screen = pygame.display.set_mode((width, height))

score = 0
level = 1
fruit_eaten = False
fruit_counter = 0  # Counter to track the number of fruits eaten

# Food list to track fruits and their type and color
food_items = []

head_square = [100, 100]

squares = [
    [30, 100], [40, 100], [50, 100], [60, 100],
    [70, 100], [80, 100], [90, 100], [100, 100]
]

direction = "right"
next_dir = "right"
done = False

# Function to handle game over
def game_over(font, size, color):
    global done
    g_o_font = pygame.font.SysFont(font, size)
    g_o_surface = g_o_font.render("Game Over, your score: " + str(score), True, color)
    g_o_rect = g_o_surface.get_rect(center=(width // 2, height // 2))

    screen.fill((0, 0, 0))
    screen.blit(g_o_surface, g_o_rect)
    pygame.display.update()
    
    pygame.time.delay(3000)
    pygame.quit()
    exit()

# Set an initial delay time
delay_time = 100  # Default speed for level 1

# Function to generate a new food item with color and points
def generate_food():
    fr_x = random.randrange(1, width // 10) * 10
    fr_y = random.randrange(1, height // 10) * 10
    color_choice = random.choice(["red", "yellow", "green"])  # Random color for the food
    if color_choice == "red":
        points = 10
        color = (255, 0, 0)  # Red color
    elif color_choice == "yellow":
        points = 15
        color = (255, 255, 0)  # Yellow color
    else:
        points = 20
        color = (0, 255, 0)  # Green color
    timer = pygame.time.get_ticks()  # Get current time in milliseconds
    return {"position": [fr_x, fr_y], "points": points, "color": color, "timer": timer}

# Initial food item
food_items.append(generate_food())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                next_dir = "down"
            if event.key == pygame.K_UP:
                next_dir = "up"
            if event.key == pygame.K_LEFT:
                next_dir = "left"
            if event.key == pygame.K_RIGHT:
                next_dir = "right"

    # Check if snake collides with itself
    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over("times new roman", 45, (255, 0, 0))

    # Update direction
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"

    # Move snake
    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    # Check if snake hits the wall
    if head_square[0] < 0 or head_square[0] >= width or head_square[1] < 0 or head_square[1] >= height:
        game_over("times new roman", 45, (255, 0, 0))

    # Add new square to snake
    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    squares.pop(0)

    # Check for collision with food
    for food in food_items[:]:
        if head_square[0] == food["position"][0] and head_square[1] == food["position"][1]:
            fruit_eaten = True
            score += food["points"]  # Add points based on food color
            fruit_counter += 1
            food_items.remove(food)  # Remove the eaten food from the list

    # Generate new food if fruit is eaten or expired
    if fruit_eaten:
        food_items.append(generate_food())
        fruit_eaten = False

    # Level up after eating 3-4 fruits
    if fruit_counter >= 4:
        level += 1
        fruit_counter = 0  # Reset fruit counter
        
        if level <= 10:
            delay_time = max(100 - level * 5, 50)  # Minimum delay is 50ms
        else:
            delay_time = 50

    # Remove food that has expired (timer > 5 seconds) and generate new food immediately
    current_time = pygame.time.get_ticks()
    expired_foods = [food for food in food_items if current_time - food["timer"] > 5000]
    for expired_food in expired_foods:
        food_items.remove(expired_food)
        food_items.append(generate_food())  # Generate new food for the expired one

    # Clear screen
    screen.fill((0, 0, 0))

    # Display score
    score_font = pygame.font.SysFont("times new roman", 20)
    score_surface = score_font.render("Score: " + str(score), True, (128, 128, 128))
    score_rect = score_surface.get_rect(topleft=(10, 10))
    screen.blit(score_surface, score_rect)

    # Display level
    level_font = pygame.font.SysFont("times new roman", 20)
    level_surface = level_font.render("Level: " + str(level), True, (128, 128, 128))
    level_rect = level_surface.get_rect(topright=(width - 10, 10))
    screen.blit(level_surface, level_rect)

    pygame.draw.rect(screen, (255, 0, 0), (0, 0, width, height), 5)

    # Draw remaining food items with different colors
    for food in food_items:
        pygame.draw.circle(screen, food["color"], (food["position"][0] + 5, food["position"][1] + 5), 5)

    # Draw snake
    for el in squares:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))

    pygame.display.flip()
    pygame.time.delay(delay_time)  # Adjust the delay for speed

pygame.quit()
