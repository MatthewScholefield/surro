import sys
from os.path import join
from threading import Timer

import numpy as np
from openal.audio import SoundSource

assets_root = getattr(sys, '_MEIPASS', '.')


def get_sfx(name):
    return join(assets_root, 'assets', name)


def new_pt(*values):
    return np.array(values or (0, 0, 0), dtype=float)


def vec_mag(vec: np.array):
    return np.sqrt(vec.dot(vec))


def vec_dist(a: np.array, b: np.array):
    return vec_mag(a - b)


class ContinuousSoundSource(SoundSource):
    def __init__(self, sound_generator):
        super().__init__()

        def play_sound():
            sound = sound_generator()
            self.queue(sound)
            self.__dict__['timer'] = timer = Timer(self.calc_length(sound), play_sound)
            timer.daemon = True
            timer.start()

        play_sound()

    @staticmethod
    def calc_length(sound):
        return sound.size / (sound.frequency * sound.bitrate / 8)
