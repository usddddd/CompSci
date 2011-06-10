from gasp import *

begin_graphics(800, 600, title ="Catch", background=color.YELLOW)
set_speed(120)

ball_x = 10
ball_y = 300
ball = Circle((ball_x, ball_y), 10, filled = True)
dx = 4
dy = random_between(-4,4) 

while ball_x < 810:
    if ball_y >= 590 or ball_y <= 10:
        dy *= -1
    ball_x += dx
    ball_y += dy
    move_to(ball, (ball_x, ball_y))
    update_when('next_tick')

end_graphics()


