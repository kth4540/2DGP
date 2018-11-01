from pico2d import*
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Cadence:
    def __init__(self):
        self.x, self.y = 104+24, 500-24
        self.frame = 0
        self.image = load_image('clone.png')
        self.attack_sound=load_wav('attack.wav')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def attack(self):
        self.attack_sound.set_volume(500)
        self.attack_sound.play()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 24, 24, 24, 24, self.x, self.y)