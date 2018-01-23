from copy import copy
from glob import glob
from os.path import basename, join
from random import shuffle

from openal.loaders import load_wav_file

from surro.util import ContinuousSoundSource, assets_root


class Orb:
    def __init__(self, world, songs=None):
        self.world = world
        self.pos_t = self.new_pos()
        self.pos = copy(self.pos_t)

        self.songs = songs or []

        def generate_song():
            if len(self.songs) == 0:
                self.songs.extend(glob(join('.', 'songs', '*.wav')))
                if len(self.songs) == 0:
                    self.songs.extend(glob(join(assets_root, 'songs', '*.wav')))
                if len(self.songs) == 0:
                    raise RuntimeError('No wav files found in songs/')
                shuffle(self.songs)
            song_file = self.songs.pop()
            print('Selected song:', basename(song_file).replace('.mp4', '').replace('.wav', ''))
            return load_wav_file(song_file)

        self.source = ContinuousSoundSource(generate_song)

    def new_pos(self):
        self.pos_t = self.world.random_point(0.6)
        return self.pos_t

    def update(self):
        if not self.world.alive:
            self.source.gain = max(0, self.source.gain - 0.01)
            return

        self.pos += 0.015 * (self.pos_t - self.pos)
        self.source.position = tuple(self.pos)
