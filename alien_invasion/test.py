import sys
import pygame
from settings import *
from object import Obj

class Ali:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        self.obj = Obj(self)
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.obj.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = Ali()
    ai.run_game()
