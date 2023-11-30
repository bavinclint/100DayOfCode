# https://reeborg.ca/index_en.html
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
def jump():
    if wall_in_front():
        turn_left()
        turn_left()
        if wall_in_front():
            turn_left()
            move()
        else:
            move()
    else:
        move()

while not at_goal():
    if is_facing_north():
        turn_right()
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_right()
            jump()
    else:
        turn_left()