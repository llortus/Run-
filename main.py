import pygame

import state
import title
import game

pygame.init()
display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Run! Space to Jump - 1 to Throw")

class RBR():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = RBR()
    game.start()