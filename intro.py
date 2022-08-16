import random
import pgzrun

alien = Actor('alien')
alien.pos = 100,56
speed = 3

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 15, 233))
    alien.draw()

def update():

    alien.left += speed
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos,button):
    global speed
    if alien.collidepoint(pos):
        set_alien_hurt()
        clock.schedule_unique(set_alien_normal, 1.0)

        # if button == mouse.LEFT:
        #     speed += 1
        # elif speed == 0:
        #     if button == mouse.LEFT:
        #         speed = 3
        #     else:
        #         speed = 5
        # else:
        #     speed = 0
    if button == mouse.RIGHT:
        alien.pos = pos


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()

def set_alien_normal():
    alien.image = 'alien'

def random_position():
    x = random.randint(0,WIDTH)
    y = random.randint(0,WIDTH)
    alien.pos = x,y
    clock.schedule_unique(random_position, 3.0)


random_position()
pgzrun.go()