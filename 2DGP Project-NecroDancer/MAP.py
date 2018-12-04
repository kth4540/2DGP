from pico2d import*
class Map:
    def __init__(self):
        self.image1=load_image('wall.png')
        self.image2=load_image('floor.png')
        self.background=load_image('background.png')
        self.music=load_music('zone1_2.mp3')  # BPM 115
        self.music.set_volume(50)
        self.music.repeat_play()


    def draw(self):
        self.background.clip_composite_draw(0, 0, 477, 322, 0, ' ', 400, 300, 800, 600)
        for i in range(1,25+1):
            self.image1.draw(80+24*i,500)
            self.image1.draw(80+24*i,114)
        for i in range(1,15+1):
            self.image1.clip_draw(0,22,24,24,680,510-24*i)
            self.image1.clip_draw(0,22,24,24,104,510-24*i)

        for i in range(1,23+1):
            for j in range(1,15+1):
                self.image2.clip_draw(0,26,24,24,104+24*i,500-24*j) # 좌측 상단 바닥 좌표 = (104+24,500-24)

