import os
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
sun = Planet("Sun", sun_x, sun_y, sun_radius, 0, 0, WHITE)

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

mercury = Planet("Mercury", center_x + 50, center_y, 10, 50, math.pi / 4, mercury_color)
venus = Planet("Venus", center_x + 75, center_y, 15, 75, math.pi / 3, venus_color)
earth = Planet("Earth", center_x + 100, center_y, 20, 100, math.pi / 2, earth_color)
mars = Planet("Mars", center_x + 125, center_y, 15, 125, 2 * math.pi / 3, mars_color)
jupiter = Planet("Jupiter", center_x + 150, center_y, 30, 150, math.pi, jupiter_color)
saturn = Planet("Saturn", center_x + 200, center_y, 25, 200, 3 * math.pi / 2, saturn_color)
uranus = Planet("Uranus", center_x + 250, center_y, 20, 250, 2 * math.pi, uranus_color)
neptune = Planet("Neptune", center_x + center_y, center_y, 15, center_y, 5 * math.pi / 3, neptune_color)
pluto = Planet("Pluto", center_x + 350, center_y, 10, 350, 3 * math.pi / 4, pluto_color)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

# Set up the timer
clock = pygame.time.Clock()

# Screenshots for animation
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
screenshot_number = 0
recording = False

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
            elif event.key == pygame.K_r:
                recording = not recording
    
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
        # Draw the name label
        font = pygame.font.Font(None, 36)
        text = font.render(planet.name, 1, WHITE)
        text_x = planet.x - text.get_width() // 2
        text_y = planet.y - planet.radius * zoom - text.get_height()
        screen.blit(text, (text_x, text_y))
    
    
    # Take Screenshot
    if recording:
        pygame.image.save(screen,f"{screenshot_folder}/{screenshot_number:010}.jpg")
        screenshot_number += 1
        pygame.draw.circle(screen, (255,0,0), (20,20), 5)
        
    # Update the display
    pygame.display.flip()
    


# Quit pygame
pygame.quit()
