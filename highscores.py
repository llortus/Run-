import pygame
from pygame.locals import *

import state
import surface_manager
import title

class HighScores(state.State):
    high_scores = []
    def __init__(self, score):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/city.png")
        
        if score > 0:
            HighScores.high_scores.append(score)
        
        HighScores.high_scores.sort(reverse=True)
        
        if len(HighScores.high_scores) > 10:
            del HighScores.high_scores[10:]

        self.header_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 84)
        self.header = self.header_manager.render("YOUR SCORES:", True, (255, 255, 255))
        self.header_rect = pygame.Rect((self.display.get_width()/2 -self.header.get_width()/2, 0), (self.header.get_width(), self.header.get_height()))

        self.font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 28)
        self.music = pygame.mixer.Sound("data/sound/title_highscore.wav")
        self.music.play(loops=-1)

    def exit(self):
        self.music.stop()

    def reason(self):
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            return title.Title()

    def act(self):
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.header, self.header_rect)

        for y, score in enumerate(HighScores.high_scores):
            self.display.blit(self.font_manager.render("%d    %d" % (y+1, score), True, (255, 255, 255)), (self.display.get_width()/2 - 64, (self.header_rect.top + self.header.get_height()) + (32*(y+1))))

        pygame.display.update()
        pygame.event.clear()