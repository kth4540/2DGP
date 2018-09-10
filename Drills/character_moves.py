from pico2d import *
os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture03')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)



close_canvas()
