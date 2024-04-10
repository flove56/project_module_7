# Set the parameters for the different ears positions
ears_low = 10
ears_mid = 40
ears_high = 80

# Set the parameters for the different eyes stages
eyes_reg = 1
eyes_big = 2
eyes_small = 3
eyes_closed = 4
eyes_angle_nor = 10
eyes_angle_not = 0

# Set the parameters for the different tail movements
tail_width_normal = 1
tail_width_sad = 3
tail_movement_slow = 0.01
tail_movement_fast = 0.07
tail_movement_not = 0
tail_max_scale_reg = 1
tail_max_scale_big = 2
tail_end_nor = 'high'
tail_end_low = 'low'

# Set the parameters for the different mouth stage
mouth_normal = 3.14
mouth_sad = 1


def stage(phase):
    """

    :param phase: give a string of the different phases with the three first letters
    :return: a list in the order: 0:ears_angle, 1:eyes_scale, 2:eyes_angle, 3:tail_movement, 4: tail_max_scale
    5:tail_width, 6: tail_end, 7:mouth_pos
    """
    move_list = []

    # All variables are set to the default setting (reg)
    ears_angle = ears_mid
    eyes_scale = eyes_reg
    eyes_angle = eyes_angle_nor
    tail_movement = tail_movement_slow
    tail_width = tail_width_normal
    tail_max_scale = tail_max_scale_reg
    tail_end = tail_end_nor
    mouth_pos = mouth_normal

    # The variables are changed if they are different then the default
    if phase == 'pet':
        tail_movement = tail_movement_fast
        tail_max_scale = tail_max_scale_big
    if phase == 'scr':
        ears_angle = ears_high
        eyes_scale = eyes_big
        tail_movement = tail_movement_fast
        tail_max_scale = tail_max_scale_big
        tail_end = tail_end_low
    if phase == 'pok':
        ears_angle = ears_low
        eyes_scale = eyes_closed
        eyes_angle = eyes_angle_not
        tail_movement = tail_movement_fast
        tail_max_scale = tail_max_scale_big
    if phase == 'com':
        ears_angle = ears_high
        eyes_scale = eyes_closed
        tail_end = tail_end_low
    if phase == 'hit':
        ears_angle = [ears_high, ears_low]
        eyes_scale = [eyes_big, eyes_small]
        tail_movement = tail_movement_not
        tail_width = tail_width_sad
        mouth_pos = mouth_sad
    move_list.append(ears_angle)
    move_list.append(eyes_scale)
    move_list.append(eyes_angle)
    move_list.append(tail_movement)
    move_list.append(tail_width)
    move_list.append(tail_max_scale)
    move_list.append(tail_end)
    move_list.append(mouth_pos)
    return move_list
