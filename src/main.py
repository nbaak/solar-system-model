import pygame
import math

from planet import Planet

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
sun = Planet(sun_x, sun_y, sun_radius, 0, 0, WHITE)

# Set up the planets
mercury_color = (178, 178, 178)  # gray
venus_color = (255, 153, 51)  # orange
earth_color = (51, 153, 255)  # blue
mars_color = (255, 51, 51)  # red
jupiter_color = (255, 255, 153)  # yellow
saturn_color = (255, 153, 153)  # pink
uranus_color = (153, 153, 255)  # light blue
neptune_color = (51, 102, 255)  # dark blue
pluto_color = (178, 102, 255)  # purple

mercury = Planet(center_x + 50, center_y, 10, 50, math.pi / 4, mercury_color)
venus = Planet(center_x + 75, center_y, 15, 75, math.pi / 3, venus_color)
earth = Planet(center_x + 100, center_y, 20, 100, math.pi / 2, earth_color)
mars = Planet(center_x + 125, center_y, 15, 125, 2 * math.pi / 3, mars_color)
jupiter = Planet(center_x + 150, center_y, 30, 150, math.pi, jupiter_color)
saturn = Planet(center_x + 200, center_y, 25, 200, 3 * math.pi / 2, saturn_color)
uranus = Planet(center_x + 250, center_y, 20, 250, 2 * math.pi, uranus_color)
neptune = Planet(center_x + center_y, center_y, 15, center_y, 5 * math.pi / 3, neptune_color)
pluto = Planet(center_x + 350, center_y, 10, 350, 3 * math.pi / 4, pluto_color)

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
        
    # Update the planets
    dt = clock.tick(60) / 1000
    for planet in planets:
        planet.update(dt, sun, zoom)
    
    # Draw the sun
    pygame.draw.circle(screen, WHITE, (sun.x, sun.y), sun.radius * zoom)
    
    # Draw the planets
    for planet in planets:
        pygame.draw.circle(screen, planet.color, (planet.x, planet.y), planet.radius * zoom)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
