import pygame
import math

from planet import Planet 
import py

# Set up the pygame window
pygame.init()
window_width = 2000
window_height = 2000
screen = pygame.display.set_mode((window_width, window_height))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Center Point
center_x = window_width // 2
center_y = window_height // 2

# Set up the sun
sun_x = center_x
sun_y = center_y
sun_radius = 50
sun = Planet(sun_x, sun_y, sun_radius, 0, 0)

# Set up the planets
mercury = Planet(center_x + 50, center_y, 10, 50, math.pi / 4)
venus = Planet(center_x + 75, center_y, 15, 75, math.pi / 3)
earth = Planet(center_x + 100, center_y, 20, 100, math.pi / 2)
mars = Planet(center_x + 125, center_y, 15, 125, 2 * math.pi / 3)
jupiter = Planet(center_x + 150, center_y, 30, 150, math.pi)
saturn = Planet(center_x + 200, center_y, 25, 200, 3 * math.pi / 2)
uranus = Planet(center_x + 250, center_y, 20, 250, 2 * math.pi)
neptune = Planet(center_x + center_y, center_y, 15, center_y, 5 * math.pi / 3)
pluto = Planet(center_x + 350, center_y, 10, 350, 3 * math.pi / 4)
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

# Set up the timer
clock = pygame.time.Clock()

# define zoom
zoom = 1

# Set up the loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS:
                zoom += .1
            elif event.key == pygame.K_MINUS:
                zoom -= .1
            elif event.key == pygame.K_q:
                done = True
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Update Sun
    # sun.x = 
    
    # Update the planets
    dt = clock.tick(60) / 1000
    for planet in planets:
        planet.update(dt, sun, zoom)
    
    # Draw the sun
    pygame.draw.circle(screen, WHITE, (sun.x, sun.y), sun.radius)
    
    # Draw the planets
    for planet in planets:
        pygame.draw.circle(screen, WHITE, (planet.x, planet.y), planet.radius)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
