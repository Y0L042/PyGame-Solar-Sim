class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11

    SCALE = 250 / AU  # 1AU = 100px
    TIMESTEP = 3600*24

    def __init__(self, posX, posY, radius, mass, color):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.mass = mass
        self.color = color

        self.velX = 0
        self.velY = 0

        self.orbitTail= []

    def draw(self, win):
        x = self.posX * self.SCALE + WIDTH / 2
        y = self.posY * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)