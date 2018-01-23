import atexit

import pygame
from openal.audio import SoundSink
from pygame.surface import Surface

from surro.world import World


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Surro")
        atexit.register(pygame.quit)

        self.songs = []
        self.sink = SoundSink()
        self.sink.activate()
        self.screen = self.create_screen(640, 480)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(self.choose_font(), 70)
        self.has_evil = True
        self.world = None
        self.create_world()

    def create_world(self):
        if self.world:
            self.world.destroy()
        self.world = World(self.sink, self.songs, self.has_evil)

    @staticmethod
    def choose_font():
        fonts = sorted(pygame.font.get_fonts())
        for search_term in ['thin', 'light', 'roboto', 'dejavu', 'liberation', 'droidsans']:
            for font in fonts:
                if search_term in font:
                    print('Selected font:', font)
                    return font
        return ''

    @staticmethod
    def create_screen(width, height) -> Surface:
        params = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        return pygame.display.set_mode((width, height), params)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.VIDEORESIZE:
                print(event.w, event.h)
                self.screen = self.create_screen(event.w, event.h)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.has_evil = not self.has_evil
                    self.create_world()
                elif event.key == pygame.K_SPACE:
                    if not self.world.alive:
                        self.create_world()

    def run(self):
        while True:
            self.handle_events()

            self.world.update()
            self.world.render(self.font, self.screen)
            self.clock.tick(self.world.FPS)
