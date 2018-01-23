from random import randint

import pygame
from openal.audio import SoundSource
from openal.loaders import load_wav_file
from pygame.font import Font
from pygame.surface import Surface

from surro.enemy import Enemy
from surro.orb import Orb
from surro.player import Player
from surro.util import get_sfx, new_pt, vec_dist, ContinuousSoundSource


class World:
    FPS = 60
    SCALE = 0.05
    SIZE = 150 * SCALE

    def __init__(self, sink, songs=None, has_evil=True):
        self.sink = sink
        self.has_evil = has_evil

        self.points = self.points_t = 0
        self.game_time = 0.
        self.alive = True

        self.player = Player(self)
        self.enemy = Enemy(self) if has_evil else None
        self.orb = Orb(self, songs)

        self.sources = [self.player.damage_source, self.orb.source]
        if self.enemy:
            self.sources.append(self.enemy.source)
        self.sink.play(self.sources)

    def destroy(self):
        for i in self.sources:
            if isinstance(i, ContinuousSoundSource):
                i.timer.cancel()
        self.sink.stop(self.sources)

    def play_sfx(self, name, offset=(0., 0., 0.), volume=1.):
        source = SoundSource()
        source.queue(load_wav_file(get_sfx(name)))
        source.gain = volume
        source.position = tuple(new_pt(*self.sink.listener.position) + new_pt(*offset))
        self.sink.play(source)

    def random_point(self, ratio=1.):
        width = int(ratio * self.SIZE)
        return new_pt(randint(0, 2 * width) - width,
                      0, randint(0, 2 * width) - width)

    def score_points(self, points):
        self.play_sfx('point.wav')
        self.orb.new_pos()
        self.points_t += points

    def game_over(self):
        self.alive = False

    def update(self):
        self.player.update()
        if self.enemy:
            self.enemy.update()
        self.orb.update()
        self.sink.update()

        self.points += 0.1 * (self.points_t - self.points)
        self.game_time += 1. / self.FPS

    def calculate_bg_color(self):
        if not self.alive:
            return new_pt(0.7, 0.0, 0.0)

        def light_ratio(dist, damper=0.2):
            return 1. / max(1., dist / damper)

        enemy = light_ratio(vec_dist(self.player.pos, self.enemy.pos)) if self.enemy else 0.
        target = light_ratio(vec_dist(self.player.pos, self.orb.pos))
        wall = light_ratio(self.SIZE - max(abs(self.player.pos)))

        color = new_pt()
        for ratio, item_color in [
            (target, (1., 1., 1.)),
            (enemy, (1., 0., 0.)),
            (wall, (.2, .4, .9))
        ]:
            color += (1. - max(color)) * ratio * new_pt(*item_color)
        return color

    def render(self, font: Font, screen: Surface):
        def render_text(text, pos, color=(255, 255, 255)):
            surface = font.render(str(text), True, color)
            pos = (new_pt(pos[0] * screen.get_width(), pos[1] * screen.get_height()) -
                   new_pt(*surface.get_size()) / 2)
            screen.blit(surface, tuple(pos))

        screen.fill(tuple(255. * self.calculate_bg_color()))

        render_text(int(self.points + 0.5), (0.5, 0.5))
        render_text(round(self.player.health, 1), (0.1, 0.1), (255, 200, 200))
        if not self.alive:
            render_text('Game Over', (0.5, 0.2))
        pygame.display.flip()
