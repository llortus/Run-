import pygame

surface_list = pygame.sprite.RenderUpdates()

def add(surface):
    global surface_list
    surface_list.add(surface)

def remove(surface):
    global surface_list
    surface_list.remove(surface)
    
def update():
    global surface_list
    surface_list.update()

def draw(display):
    global surface_list
    dirty_rects = surface_list.draw(display)
    return dirty_rects

def clear(display, background):
    global surface_list
    surface_list.clear(display, background)

def has(surface):
    if surface_list.has(surface):
        return True
    else:
        return False

def empty():
    global surface_list
    surface_list.empty()