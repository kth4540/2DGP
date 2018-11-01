from pico2d import*
class Heart:
    def __init__(self):
        self.x,self.y=400,50
        self.frame=0
        self.image=load_image('heart.png')
        self.tmp=0

    def update(self):
        self.tmp=(self.tmp+1)%85
        if(self.tmp==75 or self.tmp==0):
            self.frame=(self.frame+1)%2

    def draw(self):
        self.image.clip_draw(self.frame * 41, 0, 41, 52, self.x, self.y)