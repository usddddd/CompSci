from gasp import *

COMPUTER_WINS = 1
PLAYER_WINS = 0
QUIT = -1
# func to return bool if ball is within radius of paddle
def hit(bx, by, r, px, py, h):
    """
    >>> hit(760, 100, 10, 780, 100, 100)
    False
    >>> hit(770, 100, 10, 780, 100, 100)
    True
    >>> hit(770, 200, 10, 780, 100, 100)
    True
    >>> hit(770, 210, 10, 780, 100, 100)
    False
    """
    if px - r <= bx <= px + r and py <= by <= py + h:
        return True
    else:
        return False


def play_round():
    ball_x = 10
    ball_y = random_between(20, 280)
    ball = Circle((ball_x, ball_y), 10, filled=True)
    dx = 4
    dy = random_between(-5,5)
    
    height = 100
    radius = 20
    mitt_x = 780
    mitt_y = random_between(20,280)
    mitt = Box((mitt_x, mitt_y),10, height)

    while True:
        if ball_y >= 590 or ball_y <= 10:
            dy *= -1
        ball_x += dx
        ball_y += dy
        move_to(ball, (ball_x, ball_y))
        
        if key_pressed('k') and mitt_y <= 500:
            mitt_y += 5
        elif key_pressed('j') and mitt_y >= 0:
            mitt_y -= 5
        if key_pressed('e'):
            return QUIT

        move_to(mitt, (mitt_x, mitt_y))
        # check if ball hits paddle trajectory is reversed
        if hit(ball_x, ball_y, radius, mitt_x, mitt_y, height):
            dy *= -1
            dx *= -1
        elif ball_x >= 800 and not hit(ball_x, ball_y, radius,mitt_x, mitt_y, height): # else computer gets the point
            remove_from_screen(ball)
            remove_from_screen(mitt) 
            return COMPUTER_WINS
        if dx < 0 and ball_x <= 60:  # if traj is neg and < 60 we score!
            remove_from_screen(ball)
            remove_from_screen(mitt) 
            return PLAYER_WINS
        update_when('next_tick')
        
def play_game():
    player_score = 0
    comp_score = 0

    while True:
        pmsg = Text("Player: %d points" % player_score,(10,570), size=24)
        cmsg = Text("Computer: %d points" % comp_score,(640,570), size=24)
        sleep(3)
        remove_from_screen(pmsg)
        remove_from_screen(cmsg)

        result = play_round()

        if result == PLAYER_WINS:
            player_score += 1
        elif result == COMPUTER_WINS:
            comp_score += 1
        else:
            return QUIT

        if player_score == 5:
            return PLAYER_WINS
        elif comp_score == 5:
            return COMPUTER_WINS

begin_graphics(800, 600, title="Catch", background = color.YELLOW)
set_speed(120)

result = play_game()

if result == PLAYER_WINS:
    Text("Player Wins!",(340, 290), size = 32)
if result == COMPUTER_WINS:
    Text("Computer Wins!",(340, 290), size = 32)

sleep(4)

end_graphics()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
