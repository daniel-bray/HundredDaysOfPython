# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def descend_hurdle():
    turn_right()
    while front_is_clear():
        move()
    if at_goal():
        return ()
    turn_left()


def check_right():
    turn_right()
    if not wall_in_front():
        move()
        descend_hurdle()


def jump_hurdle():
    turn_left()
    move()
    check_right()
    while front_is_clear():
        if at_goal():
            return ()
        else:
            move()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_hurdle()
    # if wall_in_front():
    # jump_hurdle()
