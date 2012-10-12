import sys
import pygame
from pygame.locals import *

import state
import game
import surface_manager

class Title(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/images/city.png")
        self.font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 64)
        self.help_font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 28)
        self.title_font_manager = pygame.font.Font("data/fonts/SEVEMFBR.TTF", 128)

        self.title = self.title_font_manager.render("RUN!", True, (255, 255, 255))
        self.title_rect = pygame.Rect((self.display.get_width()/2 - self.title.get_width()/2, self.display.get_height()/2 - self.title.get_height()*2),
            (self.title.get_width(), self.title.get_height()))
        self.title_color = "white"
        
        self.start_game = self.font_manager.render("START", True, (255, 255, 255))
        self.start_game_rect = pygame.Rect((self.display.get_width()/2 - self.start_game.get_width()/2, self.display.get_height()/2 - self.start_game.get_height()),
            (self.start_game.get_width(), self.start_game.get_height()))
        
        self.help = self.font_manager.render("HELP", True, (0, 0, 0))
        self.help_rect = pygame.Rect((self.display.get_width()/2 - self.help.get_width()/2, self.display.get_height()/2),
            (self.help.get_width(), self.help.get_height()))

        self.help_image = pygame.image.load("data/images/instructions.png").convert_alpha()
        self.help_image_rect = pygame.Rect((self.display.get_width()/2 - self.help_image.get_width()/2, self.display.get_height()/2 - self.help_image.get_height()/2), (self.help_image.get_width(), self.help_image.get_height()))

        self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
        self.exit_game_rect = pygame.Rect((self.display.get_width()/2 - self.exit_game.get_width()/2, self.display.get_height()/2 + self.exit_game.get_height()),
            (self.exit_game.get_width(), self.exit_game.get_height()))

        self.current_choice = 1
        
        self.show_help = False
            
        self.timer = pygame.time.Clock()

        self.music = pygame.mixer.Sound("data/sound/title_highscore.wav")
        self.music.play(loops=-1)

    def exit(self):
        self.music.stop()
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()

    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if self.show_help:
                        self.show_help = False
                    else:
                        if self.current_choice == 1:
                            return game.Game()
                        elif self.current_choice == 2:
                            self.show_help = True
                        elif self.current_choice == 3:
                            pygame.quit()
                            sys.exit()
                if event.key == K_DOWN:
                    self.next()
                if event.key == K_UP:
                    self.previous()

    def act(self):
        self.timer.tick(40)
        self.animate_title()

        self.display.blit(self.background, (0, 0))
        if self.show_help:
            self.display.blit(self.help_image, self.help_image_rect)
        else:
            self.display.blit(self.title, self.title_rect)
            self.display.blit(self.start_game, self.start_game_rect)
            self.display.blit(self.help, self.help_rect)
            self.display.blit(self.exit_game, self.exit_game_rect)

        pygame.display.update()

    def next(self):
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.help = self.font_manager.render("HELP", True, (255, 255, 255))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 2
        elif self.current_choice == 2:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.help = self.font_manager.render("HELP", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (255, 255, 255))
            self.current_choice = 3
        else:
            self.start_game = self.font_manager.render("START", True, (255, 255, 255))
            self.help = self.font_manager.render("HELP", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1

    def previous(self):
        if self.current_choice == 1:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.help = self.font_manager.render("HELP", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (255, 255, 255))
            self.current_choice = 3
        elif self.current_choice == 2:
            self.start_game = self.font_manager.render("START", True, (255, 255, 255))
            self.help = self.font_manager.render("HELP", True, (0, 0, 0))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 1
        else:
            self.start_game = self.font_manager.render("START", True, (0, 0, 0))
            self.help = self.font_manager.render("HELP", True, (255, 255, 255))
            self.exit_game = self.font_manager.render("EXIT", True, (0, 0, 0))
            self.current_choice = 2

    def animate_title(self):
        if self.title_color == "white":
            self.title = self.title_font_manager.render("RUN!", True, (0, 0, 0))
            self.title_color = "black"
        else:
            self.title = self.title_font_manager.render("RUN!", True, (255, 255, 255))
            self.title_color = "white"

        