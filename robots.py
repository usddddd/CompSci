#!/usr/bin/env python
#
#robots.py
#
from gasp import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_WIDTH = SCREEN_WIDTH/10 - 1
GRID_HEIGHT = SCREEN_HEIGHT/10 - 1

def place_player():
    x = random.randint(0, GRID_WIDTH)
    y = random.randint(0, GRID_HEIGHT)
    return {'shape': Circle((10*x+5, 10*y+5), 5, filled=True), 'x':x, 'y':y}
    
def place_robot(x, y, junk=False):
    return {'shape': Box((10*x,10*y), 10, 10, filled=junk), 'x': x, 'y':y, 'junk': junk}
    
    
def place_robots(numbots):
    robots = []
    for i in range(numbots):
        x = random.randint(0, GRID_WIDTH)
        y = random.randint(0, GRID_HEIGHT)
        robots.append(place_robot(x, y))
    return robots

junk = []

def move_player(player):
    update_when('key_pressed')
    if key_pressed('escape'):
        return True
    elif key_pressed('4'):
        if player['x'] > 0: player['x'] -= 1
    elif key_pressed('7'):
        if player['x'] > 0: player['x'] -= 1
        if player['y'] < GRID_HEIGHT: player['y'] += 1
    elif key_pressed('8'):
        if player['y'] < GRID_HEIGHT: player['y'] += 1
    elif key_pressed('9'):
        if player['x'] < GRID_WIDTH: player['x'] += 1
        if player['y'] < GRID_HEIGHT: player['y'] += 1
    elif key_pressed('6'):
        if player['x'] < GRID_WIDTH: player['x'] += 1
    elif key_pressed('3'):
        if player['x'] < GRID_WIDTH: player['x'] += 1
        if player['y'] > 0: player['y'] -= 1
    elif key_pressed('2'):
        if player['y'] > 0: player['y'] -= 1
    elif key_pressed('1'):
        if player['x'] > 0: player['x'] -= 1
        if player['y'] > 0: player['y'] -= 1
    elif key_pressed('t'):
        teleport(player)
    else:
        return False
    
    move_to(player['shape'], (10*player['x']+5, 10*player['y']+5))

    return False


def teleport(player):
    player['x'] = random.randint(0, GRID_WIDTH)
    player['y'] = random.randint(0, GRID_HEIGHT)
    move_to(player['shape'],(10*player['x']+5, 10*player['y']+5))

def collided(thing1, thing2):
    return thing1['x'] == thing2['x'] and thing1['y'] == thing2['y']
    
    
def check_collisions(robots, junk,  player):
    # Check whether player has collided with anything
    for thing in robots + junk:
        if collided(thing, player):
            return "robots_win"
    # remove robots that have collided with a junk pile
    for robot in reversed(robots):
        for pile in junk:
            if collided(robot, pile):
                robots.remove(robot)
    # remove robots that collide and leave a pile of junk
    for index, robot1 in enumerate(robots):
        for robot2 in reversed(robots[index+1:]):
            if collided(robot1, robot2):
                robot1['junk'] = True
                junk.append(place_robot(robot1['x'], robot1['y'],True))
                remove_from_screen(robot2['shape'])
                robots.remove(robot2)
    
    for robot in reversed(robots):
        if robot['junk']:
            remove_from_screen(robot['shape'])
            robots.remove(robot)
    
    if not robots:
        return "player_wins"

    return ""

def move_robot(robot, player):
        if robot['x'] < player['x']: robot['x'] += 1
        elif robot['x'] > player['x']: robot['x'] -= 1
        
        if robot['y'] < player['y']: robot['y'] += 1
        elif robot['y'] > player['y']: robot['y'] -= 1
        
        move_to(robot['shape'], (10*robot['x'], 10*robot['y']))
        
def move_robots(robots, player):
    for robot in robots:
        move_robot(robot, player)
        
    
def play_game():
    begin_graphics(SCREEN_WIDTH, SCREEN_HEIGHT, title="Robots")
    player = place_player()
    robot = place_robots(random.randint(2, 10))
    defeated = False
    while not defeated:
        quit = move_player(player)
        if quit:
            break
        move_robots(robot, player)
        defeated = check_collisions(robot, junk,  player)
        if defeated == "robots_win":
            remove_from_screen(player['shape'])
            for thing in robot + junk:
                remove_from_screen(thing['shape'])
            Text("They got you!!!", (240, 240), size = 32)
            sleep(3)
        elif defeated == "player_wins":
            remove_from_screen(player['shape'])
            for thing in robot + junk:
                remove_from_screen(thing['shape'])
            Text(("You Win!!"), (240, 240), size = 34)
            sleep(3)
            
    end_graphics()


if __name__ == '__main__':
    play_game()   
