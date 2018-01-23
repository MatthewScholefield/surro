import pygame
from openal.loaders import load_wav_file

from surro.util import new_pt, ContinuousSoundSource, get_sfx, vec_dist


class Player:
    MAX_HEALTH = 4

    def __init__(self, world):
        self.world = world
        self.step_size = world.SCALE
        self.pos = new_pt()
        self.pos_t = new_pt()
        self.since_last_point = 0.
        self.was_on_wall = False
        self.health = self.MAX_HEALTH

        self.listener = world.sink.listener
        self.damage_source = ContinuousSoundSource(lambda: load_wav_file(get_sfx('damage.wav')))

    def update_controls(self):
        keys = pygame.key.get_pressed()
        for key, index, sign in [
            (pygame.K_LEFT, 0, -1),
            (pygame.K_RIGHT, 0, +1),
            (pygame.K_UP, 2, -1),
            (pygame.K_DOWN, 2, +1)
        ]:
            if keys[key]:
                self.world.player.pos_t[index] += sign * self.step_size

    def update(self):
        if not self.world.alive:
            self.damage_source.gain = max(0, self.damage_source.gain - 0.01)
            return

        self.update_controls()

        on_wall = False
        for i in 0, 1, 2:
            if self.pos_t[i] > self.world.SIZE:
                self.pos_t[i] = self.world.SIZE
                sign = +1
            elif self.pos_t[i] < -self.world.SIZE:
                self.pos_t[i] = -self.world.SIZE
                sign = -1
            else:
                continue
            on_wall = True
            if not self.was_on_wall:
                offset = new_pt()
                offset[i] = sign
                self.world.play_sfx('wall.wav', offset=offset)
        self.was_on_wall = on_wall

        self.pos += 0.2 * (self.pos_t - self.pos)

        if self.world.enemy:
            enemy_dist = vec_dist(self.pos, self.world.enemy.pos)
            if enemy_dist < 8 * self.step_size:
                self.damage_source.gain = 1.
                self.health -= 2. / self.world.FPS
            else:
                self.damage_source.gain = 0.
        else:
            self.health -= 0.05 / self.world.FPS
            self.damage_source.gain = 0.

        if self.health < 0.:
            self.health = 0.
            self.world.game_over()

        sound_dist = vec_dist(self.pos, self.world.orb.pos_t)
        if sound_dist < 8 * self.step_size:
            self.world.score_points(10 + 1000 / max(1., self.since_last_point))
            self.health = min(self.health + 0.1, self.MAX_HEALTH)
            self.since_last_point = 0.

        self.since_last_point += 1. / self.world.FPS
        self.listener.position = tuple(self.pos)
        self.damage_source.position = tuple(self.pos)
