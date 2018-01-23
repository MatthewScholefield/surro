from copy import copy
from math import exp

from openal.loaders import load_wav_file

from surro.util import ContinuousSoundSource, get_sfx, vec_mag


class Enemy:
    def __init__(self, world):
        self.world = world  # type: World
        self.pos = world.random_point()
        self.pos_t = copy(self.pos)

        self.source = ContinuousSoundSource(lambda: load_wav_file(get_sfx('enemy.wav')))

    def update(self):
        if not self.world.alive:
            self.source.gain = max(0.4, self.source.gain - 0.01)
            return

        delta = self.world.player.pos_t - self.pos_t
        speed = 0.1 + 0.8 * (1 - exp(-self.world.game_time / 400.))
        self.pos_t += speed * self.world.SCALE * delta / vec_mag(delta)
        self.pos += 0.2 * (self.pos_t - self.pos)
        self.source.position = tuple(self.pos)
