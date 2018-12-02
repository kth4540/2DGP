from pico2d import*
import game_framework
import math

import main_state
# 프레임
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#cadence event

RIGHT_ON, LEFT_ON, UP_ON, DOWN_ON,RIGHT_OFF,LEFT_OFF,UP_OFF,DOWN_OFF,SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_ON,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_ON,
    (SDL_KEYDOWN, SDLK_UP): UP_ON,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_ON,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_OFF,
    (SDL_KEYUP, SDLK_LEFT): LEFT_OFF,
    (SDL_KEYUP, SDLK_UP): UP_OFF,
    (SDL_KEYUP, SDLK_DOWN): DOWN_OFF,
    (SDL_KEYDOWN,SDLK_SPACE):SPACE
}

class IdleState:
    @staticmethod
    def enter(cadence,event):
        if event==RIGHT_ON and cadence.rhythm>=250:
            cadence.dir=1
        elif event==LEFT_ON and cadence.rhythm>=250:
            cadence.dir=-1
        elif event==UP_ON:
            pass
        elif event==DOWN_ON:
            pass
        elif event==RIGHT_OFF:
            pass
        elif event==LEFT_OFF:
            pass
        elif event == UP_OFF:
            pass
        elif event == DOWN_OFF:
            pass
        elif event==SPACE:
            pass

    @staticmethod
    def exit(cadence,event):
        if event==RIGHT_ON and cadence.act==False and cadence.rhythm>=250:
            for i in range(main_state.bat_num):
                if(cadence.weapon==0):
                    if (cadence.x + 24 == main_state.bat[i].x and cadence.y == main_state.bat[i].y):
                        main_state.bat[i].life -= 2
                        if(main_state.bat[i].life<=0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100
                        cadence.attack_dir=0
                        cadence.attack()
                        cadence.move_check=True
                elif(cadence.weapon==1):
                    if(cadence.x+24==main_state.bat[i].x and cadence.y>=main_state.bat[i].y-24 and cadence.y<= main_state.bat[i].y+24):
                        main_state.bat[i].life -= 1
                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100
                        cadence.attack_dir = 0
                        cadence.attack()
                        cadence.move_check = True
                elif(cadence.weapon==2):
                    if(cadence.x+24==main_state.bat[i].x or cadence.x+48==main_state.bat[i].x):
                        if(cadence.y==main_state.bat[i].y):
                            main_state.bat[i].life -= 1
                            if (main_state.bat[i].life <= 0):
                                main_state.bat[i].x = -100
                                main_state.bat[i].y = -100
                            cadence.attack_dir = 0
                            cadence.attack()
                            cadence.move_check = True
            for i in range(main_state.skel_num):
                if(cadence.weapon==0):
                    if (cadence.x + 24 == main_state.skeleton[i].x and cadence.y == main_state.skeleton[i].y):
                        main_state.skeleton[i].life -= 2
                        if(main_state.skeleton[i].life<=0):
                            main_state.skeleton[i].x = -100
                            main_state.skeleton[i].y = -100
                        cadence.attack_dir=0
                        cadence.attack()
                        cadence.move_check=True
                elif(cadence.weapon==1):
                    if(cadence.x+24==main_state.skeleton[i].x and cadence.y>=main_state.skeleton[i].y-24 and cadence.y<= main_state.skeleton[i].y+24):
                        main_state.skeleton[i].life -= 2
                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100
                            main_state.skeleton[i].y = -100
                        cadence.attack_dir = 0
                        cadence.attack()
                        cadence.move_check = True
                elif(cadence.weapon==2):
                    if(cadence.x+24==main_state.skeleton[i].x or cadence.x+48==main_state.skeleton[i].x):
                        if(cadence.y==main_state.skeleton[i].y):
                            main_state.skeleton[i].life -= 1
                            if (main_state.skeleton[i].life <= 0):
                                main_state.skeleton[i].x = -100
                                main_state.skeleton[i].y = -100
                            cadence.attack_dir = 0
                            cadence.attack()
                            cadence.move_check = True
            for i in range(main_state.dragon_num):
                if(cadence.weapon==0):
                    if (cadence.x + 24 == main_state.dragon[i].x and cadence.y == main_state.dragon[i].y):
                        main_state.dragon[i].life -= 2
                        if(main_state.dragon[i].life<=0):
                            main_state.dragon[i].x = -100
                            main_state.dragon[i].y = -100
                        cadence.attack_dir=0
                        cadence.attack()
                        cadence.move_check=True
                elif(cadence.weapon==1):
                    if(cadence.x+24==main_state.dragon[i].x and cadence.y>=main_state.dragon[i].y-24 and cadence.y<= main_state.dragon[i].y+24):
                        main_state.dragon[i].life -= 1
                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100
                            main_state.dragon[i].y = -100
                        cadence.attack_dir = 0
                        cadence.attack()
                        cadence.move_check = True
                elif(cadence.weapon==2):
                    if(cadence.x+24==main_state.dragon[i].x or cadence.x+48==main_state.dragon[i].x):
                        if(cadence.y==main_state.dragon[i].y):
                            main_state.dragon[i].life -= 1
                            if (main_state.dragon[i].life <= 0):
                                main_state.dragon[i].x = -100
                                main_state.dragon[i].y = -100
                            cadence.attack_dir = 0
                            cadence.attack()
                            cadence.move_check = True
            if cadence.move_check==False and cadence.x+24<80+(24*25):
                cadence.x+=24
            cadence.act = True

        elif event == LEFT_ON and cadence.act == False and cadence.rhythm >= 250:

            for i in range(main_state.bat_num):

                if (cadence.weapon == 0):

                    if (cadence.x - 24 == main_state.bat[i].x and cadence.y == main_state.bat[i].y):

                        main_state.bat[i].life -= 2

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100

                            main_state.bat[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.x - 24 == main_state.bat[i].x and cadence.y >= main_state.bat[i].y - 24 and
                           cadence.y<= main_state.bat[i].y + 24):

                        main_state.bat[i].life -= 1

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100

                            main_state.bat[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.x - 24 == main_state.bat[i].x or cadence.x - 48 == main_state.bat[i].x):

                        if (cadence.y == main_state.bat[i].y):

                            main_state.bat[i].life -= 1

                            if (main_state.bat[i].life <= 0):
                                main_state.bat[i].x = -100

                                main_state.bat[i].y = -100

                            cadence.attack_dir = 1

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.skel_num):

                if (cadence.weapon == 0):

                    if (cadence.x - 24 == main_state.skeleton[i].x and cadence.y == main_state.skeleton[i].y):

                        main_state.skeleton[i].life -= 2

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.x - 24 == main_state.skeleton[i].x and cadence.y >= main_state.skeleton[i].y - 24 and
                            cadence.y<=main_state.skeleton[i].y + 24):

                        main_state.skeleton[i].life -= 1

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.x - 24 == main_state.skeleton[i].x or cadence.x - 48 == main_state.skeleton[i].x):

                        if (cadence.y == main_state.skeleton[i].y):

                            main_state.skeleton[i].life -= 1

                            if (main_state.skeleton[i].life <= 0):
                                main_state.skeleton[i].x = -100

                                main_state.skeleton[i].y = -100

                            cadence.attack_dir = 1

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.dragon_num):

                if (cadence.weapon == 0):

                    if (cadence.x - 24 == main_state.dragon[i].x and cadence.y == main_state.dragon[i].y):

                        main_state.dragon[i].life -= 2

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.x - 24 == main_state.dragon[i].x and cadence.y >= main_state.dragon[i].y - 24 and
                            cadence.y<=main_state.dragon[i].y + 24):

                        main_state.dragon[i].life -= 1

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 1

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.x - 24 == main_state.dragon[i].x or cadence.x - 48 == main_state.dragon[i].x):

                        if (cadence.y == main_state.dragon[i].y):

                            main_state.dragon[i].life -= 1

                            if (main_state.dragon[i].life <= 0):
                                main_state.dragon[i].x = -100

                                main_state.dragon[i].y = -100

                            cadence.attack_dir = 1

                            cadence.attack()

                            cadence.move_check = True

            if cadence.move_check == False and cadence.x - 24 > 80 +24 :
                cadence.x -= 24

            cadence.act = True

        elif event == DOWN_ON and cadence.act == False and cadence.rhythm >= 250:

            for i in range(main_state.bat_num):

                if (cadence.weapon == 0):

                    if (cadence.y - 24 == main_state.bat[i].y and cadence.x == main_state.bat[i].x):

                        main_state.bat[i].life -= 2

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y - 24 == main_state.bat[i].y and cadence.x >= main_state.bat[i].x - 24 and
                            cadence.x<=main_state.bat[i].x + 24):

                        main_state.bat[i].life -= 1

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y - 24 == main_state.bat[i].y or cadence.y - 48 == main_state.bat[i].y):

                        if (cadence.x == main_state.bat[i].x):

                            main_state.bat[i].life -= 1

                            if (main_state.bat[i].life <= 0):
                                main_state.bat[i].x = -100

                                main_state.bat[i].y = -100

                            cadence.attack_dir = 2

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.skel_num):

                if (cadence.weapon == 0):

                    if (cadence.y - 24 == main_state.skeleton[i].y and cadence.x == main_state.skeleton[i].x):

                        main_state.skeleton[i].life -= 2

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y - 24 == main_state.skeleton[i].y and cadence.x >= main_state.skeleton[i].x - 24 and
                            cadence.x<=main_state.skeleton[i].x + 24):

                        main_state.skeleton[i].life -= 1

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y - 24 == main_state.skeleton[i].y or cadence.y - 48 == main_state.skeleton[i].y):

                        if (cadence.x == main_state.skeleton[i].x):

                            main_state.skeleton[i].life -= 1

                            if (main_state.skeleton[i].life <= 0):
                                main_state.skeleton[i].x = -100

                                main_state.skeleton[i].y = -100

                            cadence.attack_dir = 2

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.dragon_num):

                if (cadence.weapon == 0):

                    if (cadence.y - 24 == main_state.dragon[i].y and cadence.x == main_state.dragon[i].x):

                        main_state.dragon[i].life -= 2

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y - 24 == main_state.dragon[i].y and cadence.x >= main_state.dragon[i].x - 24 and
                            cadence.x<=main_state.dragon[i].x + 24):

                        main_state.dragon[i].life -= 1

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 2

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y - 24 == main_state.dragon[i].y or cadence.y - 48 == main_state.dragon[i].y):

                        if (cadence.x == main_state.dragon[i].x):

                            main_state.dragon[i].life -= 1

                            if (main_state.dragon[i].life <= 0):
                                main_state.dragon[i].x = -100

                                main_state.dragon[i].y = -100

                            cadence.attack_dir = 2

                            cadence.attack()

                            cadence.move_check = True

            if cadence.move_check == False and cadence.y - 24 > 510-(24*16) :
                cadence.y -= 24

            cadence.act = True



        elif event == UP_ON and cadence.act == False and cadence.rhythm >= 250:

            for i in range(main_state.bat_num):

                if (cadence.weapon == 0):

                    if (cadence.y + 24 == main_state.bat[i].y and cadence.x == main_state.bat[i].x):

                        main_state.bat[i].life -= 2

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y + 24 == main_state.bat[i].y and cadence.x >= main_state.bat[i].x - 24 and
                            cadence.x <= main_state.bat[i].x + 24):

                        main_state.bat[i].life -= 1

                        if (main_state.bat[i].life <= 0):
                            main_state.bat[i].x = -100
                            main_state.bat[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y + 24 == main_state.bat[i].y or cadence.y + 48 == main_state.bat[i].y):

                        if (cadence.x == main_state.bat[i].x):

                            main_state.bat[i].life -= 1

                            if (main_state.bat[i].life <= 0):
                                main_state.bat[i].x = -100

                                main_state.bat[i].y = -100

                            cadence.attack_dir = 3

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.skel_num):

                if (cadence.weapon == 0):

                    if (cadence.y + 24 == main_state.skeleton[i].y and cadence.x == main_state.skeleton[i].x):

                        main_state.skeleton[i].life -= 2

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y + 24 == main_state.skeleton[i].y and cadence.x >= main_state.skeleton[i].x - 24 and
                            cadence.x<=main_state.skeleton[i].x + 24):

                        main_state.skeleton[i].life -= 1

                        if (main_state.skeleton[i].life <= 0):
                            main_state.skeleton[i].x = -100

                            main_state.skeleton[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y + 24 == main_state.skeleton[i].y or cadence.y + 48 == main_state.skeleton[i].y):

                        if (cadence.x == main_state.skeleton[i].x):

                            main_state.skeleton[i].life -= 1

                            if (main_state.skeleton[i].life <= 0):
                                main_state.skeleton[i].x = -100

                                main_state.skeleton[i].y = -100

                            cadence.attack_dir = 3

                            cadence.attack()

                            cadence.move_check = True

            for i in range(main_state.dragon_num):

                if (cadence.weapon == 0):

                    if (cadence.y + 24 == main_state.dragon[i].y and cadence.x == main_state.dragon[i].x):

                        main_state.dragon[i].life -= 2

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 1):

                    if (cadence.y + 24 == main_state.dragon[i].y and cadence.x >= main_state.dragon[i].x - 24 and
                            cadence.x<=main_state.dragon[i].x + 24):

                        main_state.dragon[i].life -= 1

                        if (main_state.dragon[i].life <= 0):
                            main_state.dragon[i].x = -100

                            main_state.dragon[i].y = -100

                        cadence.attack_dir = 3

                        cadence.attack()

                        cadence.move_check = True

                elif (cadence.weapon == 2):

                    if (cadence.y + 24 == main_state.dragon[i].y or cadence.y + 48 == main_state.dragon[i].y):

                        if (cadence.x == main_state.dragon[i].x):

                            main_state.dragon[i].life -= 1

                            if (main_state.dragon[i].life <= 0):
                                main_state.dragon[i].x = -100

                                main_state.dragon[i].y = -100

                            cadence.attack_dir = 3

                            cadence.attack()

                            cadence.move_check = True

            if cadence.move_check == False and cadence.y + 24 < 510 - 24:
                cadence.y += 24

            cadence.act = True

        elif event == SPACE and cadence.act == False and cadence.rhythm >= 250:
            cadence.Bomb()


    @staticmethod
    def do(cadence):
        cadence.frame = (cadence.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if cadence.bomb_check==True:
            cadence.bomb_frame=(cadence.bomb_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if cadence.bomb_frame>5:
            cadence.bomb_frame=0
            cadence.bomb_check=False
        if cadence.attack_check==True:
            if(cadence.weapon==0):
                cadence.attack_frame=(cadence.attack_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            elif(cadence.weapon==1):
                cadence.sword_frame=(cadence.sword_frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%4
            elif(cadence.weapon==2):
                cadence.rapier_frame=(cadence.rapier_frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%4
        if(cadence.attack_frame>3):
            cadence.attack_frame=0
            cadence.attack_check=False
        if(cadence.sword_frame>3):
            cadence.sword_frame=0
            cadence.attack_check=False
        if(cadence.rapier_frame>3):
            cadence.rapier_frame=0
            cadence.attack_check=False

        cadence.rhythm+=400*130/60*game_framework.frame_time
        if cadence.rhythm>=400:
            cadence.act=False
            cadence.rhythm=0
            cadence.move_check=False

    @staticmethod
    def draw(cadence):
        if cadence.dir==1:
            cadence.image.clip_composite_draw(int(cadence.frame) * 24, 24, 24, 24,0,' ' ,cadence.x, cadence.y,24,24)

        else:
            cadence.image.clip_composite_draw(int(cadence.frame) * 24, 24, 24, 24, 0, 'h', cadence.x, cadence.y, 24, 24)

        if (cadence.attack_check == True and cadence.attack_dir == 0):
            if(cadence.weapon==0):
                cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, 0, ' ', cadence.x + 24,cadence.y, 24, 24)
            elif(cadence.weapon==1):
                cadence.sword_effect.clip_composite_draw(int(cadence.sword_frame)*24,0,24,72,0,' ',cadence.x+24,cadence.y,24,72)
            elif(cadence.weapon==2):
                cadence.rapier_effect.clip_composite_draw(int(cadence.rapier_frame)*48,0,48,24,0,' ',cadence.x+24,cadence.y,48,24)

        elif (cadence.attack_check == True and cadence.attack_dir==1):
            if (cadence.weapon == 0):
                cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, 0, 'h',cadence.x - 24, cadence.y, 24, 24)
            elif (cadence.weapon == 1):
                cadence.sword_effect.clip_composite_draw(int(cadence.sword_frame) * 24, 0, 24, 72, 0, 'h', cadence.x - 24, cadence.y, 24, 72)
            elif (cadence.weapon == 2):
                cadence.rapier_effect.clip_composite_draw(int(cadence.rapier_frame) * 48, 0, 48, 24, 0, 'h',cadence.x - 24, cadence.y, 48, 24)

        elif (cadence.attack_check == True and cadence.attack_dir == 2):
            if (cadence.weapon == 0):
                cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, math.radians(-90), ' ',
                                                          cadence.x, cadence.y-24, 24, 24)
            elif (cadence.weapon == 1):
                cadence.sword_effect.clip_composite_draw(int(cadence.sword_frame) * 24, 0, 24, 72, math.radians(-90), ' ',
                                                         cadence.x, cadence.y-24, 24, 72)
            elif (cadence.weapon == 2):
                cadence.rapier_effect.clip_composite_draw(int(cadence.rapier_frame) * 48, 0, 48, 24, math.radians(-90), ' ',
                                                          cadence.x, cadence.y-24, 48, 24)

        elif (cadence.attack_check == True and cadence.attack_dir == 3):
            if (cadence.weapon == 0):
                cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, math.radians(90),
                                                          ' ',
                                                          cadence.x, cadence.y + 24, 24, 24)
            elif (cadence.weapon == 1):
                cadence.sword_effect.clip_composite_draw(int(cadence.sword_frame) * 24, 0, 24, 72, math.radians(90),
                                                         ' ',
                                                         cadence.x, cadence.y + 24, 24, 72)
            elif (cadence.weapon == 2):
                cadence.rapier_effect.clip_composite_draw(int(cadence.rapier_frame) * 48, 0, 48, 24, math.radians(90),
                                                          ' ',
                                                          cadence.x, cadence.y + 24, 48, 24)

        if(cadence.bomb_check==True):
            for i in range (3):
                cadence.bomb.clip_composite_draw(int(cadence.bomb_frame+3)*74,0,74,74,0,' ',cadence.x+(24*(i-1)),cadence.y+24,24,24)
                cadence.bomb.clip_composite_draw(int(cadence.bomb_frame + 3) * 74, 0, 74, 74, 0, ' ',cadence.x + (24 * (i - 1)), cadence.y, 24, 24)
                cadence.bomb.clip_composite_draw(int(cadence.bomb_frame + 3) * 74, 0, 74, 74, 0, ' ',cadence.x + (24 * (i - 1)), cadence.y -24, 24, 24)

        for i in range(cadence.life):
            cadence.hp_image.draw(780-(24*i),550)

next_state_table={
    IdleState:{RIGHT_ON:IdleState,LEFT_ON:IdleState,UP_ON:IdleState,DOWN_ON:IdleState,
               RIGHT_OFF:IdleState, LEFT_OFF:IdleState, UP_OFF:IdleState,DOWN_OFF:IdleState, SPACE:IdleState}

}


class Cadence:
    def __init__(self):
        self.x, self.y = 104+24, 500-24
        self.life=10
        self.move_check=False
        self.frame = 0
        self.attack_frame=0
        self.sword_frame=0
        self.rapier_frame=0
        self.attack_check=False
        self.weapon=2
        self.image = load_image('clone.png')
        self.bomb=load_image('bomb.png')
        self.attack_sound=load_wav('attack.wav')
        self.attack_effect=load_image('attack_effect.png')
        self.sword_effect=load_image('attack_sword.png')
        self.rapier_effect=load_image('attack_rapier.png')
        self.hp_image=load_image('life.png')
        self.explode=load_wav('explode.wav')
        self.rhythm=0
        self.act=False
        self.dir=1
        self.attack_dir=0
        self.bomb_check=False
        self.bomb_frame=0
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def attack(self):
        self.attack_sound.set_volume(500)
        self.attack_sound.play()
        self.attack_check=True

    def Bomb(self):
        self.bomb_check=True
        for i in range(main_state.skel_num):
            if(main_state.skeleton[i].x<=self.x+24 and main_state.skeleton[i].x>=self.x-24
            and main_state.skeleton[i].y<=self.y+24 and main_state.skeleton[i].y>=self.y-24):
                main_state.skeleton[i].life=0
                main_state.skeleton[i].x=-100
                main_state.skeleton[i].y = -100

        for i in range(main_state.bat_num):
            if(main_state.bat[i].x<=self.x+24 and main_state.bat[i].x>=self.x-24
            and main_state.bat[i].y<=self.y+24 and main_state.bat[i].y>=self.y-24):
                main_state.bat[i].life=0
                main_state.bat[i].x = -100
                main_state.bat[i].y = -100

        for i in range(main_state.dragon_num):
            if (main_state.dragon[i].x <= self.x + 24 and main_state.dragon[i].x >= self.x - 24
                and main_state.dragon[i].y <= self.y + 24 and main_state.dragon[i].y >= self.y - 24):
                main_state.dragon[i].life = 0
                main_state.dragon[i].x = -100
                main_state.dragon[i].y = -100
        self.explode.play()

        self.life-=1



    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

