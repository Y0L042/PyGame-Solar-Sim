import pygame

class PyShape:
    def __init__(self):
        pass
    
    def draw(self, win, delta):
        pass
    
    
    
class CircleSprite(PyShape):
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color
        
    def draw(self, win, delta):
        pygame.draw.circle(win, self.color, (self.center[0], self.center[1]), self.radius)
    
    
class PyRect(PyShape):
    def __init__(self):
        pass
    
    
    
class PyLine(PyShape):
    def __init__(self):
        pass
    
    
    
class PyPolygon(PyShape):
    def __init__(self):
        pass
    
    
    
class PyEllipse(PyShape):
    def __init__(self):
        pass
    
    
    
class PyArc(PyShape):
    def __init__(self):
        pass