import pygame
import math
pygame.init()

#region Display Config
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
#endregion Display Config



#region Loop
def main():
    run = True
    while run:
        # VVV Add your code here VVV
        process()
        # ^^^ Add your code here ^^^
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
#endregion Loop



#region Main Functions
def process():
    pass
#endregion Main Functions



#region Main()
main()
#endregion Main()