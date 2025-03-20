import pygame
import time
import math

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

clock_image = pygame.image.load("clock.png")
right_hand = pygame.image.load("rightarm.png")
left_hand = pygame.image.load("leftarm.png")

clock_image = pygame.transform.scale(clock_image, (width, height))


right_w, right_h = right_hand.get_size()
left_w, left_h = left_hand.get_size()


right_hand = pygame.transform.scale(right_hand, (right_w, right_h/(2.5))) 
left_hand = pygame.transform.scale(left_hand, (left_w, left_h/(2.5))) 

def rotate_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_image, (0, 0))
    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    second_angle = -seconds * 6
    minute_angle = -minutes * 6
    
    rotated_right, rect_right = rotate_center(right_hand, minute_angle, width//2, height//2)
    rotated_left, rect_left = rotate_center(left_hand, second_angle, width//2, height//2)
    
    screen.blit(rotated_right, rect_right.topleft)
    screen.blit(rotated_left, rect_left.topleft)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(1000)

pygame.quit()
