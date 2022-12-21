import math

class Planet:
    def __init__(self, x, y, radius, orbit_radius, orbit_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.angle = 0
    
    def update(self, dt, center, zoom=1):
        self.angle += self.orbit_speed * dt
        self.x = math.cos(self.angle) * (self.orbit_radius * zoom) + center.x
        self.y = math.sin(self.angle) * (self.orbit_radius * zoom) + center.y


