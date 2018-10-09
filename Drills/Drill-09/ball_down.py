import random
from pico2d import *

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += random.randint(1,6)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class S_Ball:
    def __init__(self):
        self.x,self,y=random.randint(100,700), 600
        self.image=load_image('ball21x21.png')
    def update(self):
        self.y-= random.randint(1,6)

class B_Ball:
    def __init__(self):
        self.x,self.y=random.randint(100,700),600
        self.image=load_image('ball41x41.png')

    def update(self):
        self.y-=random.randint(1,6)
open_canvas()

big_count=random.randint(1,20+1)
small_count=20-big_count

team = [Boy() for i in range(11)]
Big_ball=[B_Ball() for i in range(big_count)]
Small_ball=[S_Ball() for i in range(small_count)]
grass = Grass()

running = True

