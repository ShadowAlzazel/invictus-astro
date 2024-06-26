import pygame

class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func # A function to run
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        # Runs function if active
        if current_time - self.start_time >= self.duration and self.active:
            self.deactivate()
            if self.func:
                self.func()