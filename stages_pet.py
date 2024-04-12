# Set the parameters for the different ears positions
ears_low = 10
ears_mid = 15
ears_high = 35
ears_pos_reg = 'reg'
ears_pos_high = 'high'
ears_pos_low = 'low'

# Set the parameters for the different eyes stages
eyes_reg = 3.8
eyes_big = 3
eyes_small = 3

# Set the parameters for the different tail movements
tail_width_normal = 3
tail_width_sad = 5
tail_speed_slow = 0.02
tail_speed_fast = 0.06
tail_speed_not = 0
tail_max_scale_reg = 0.5
tail_max_scale_big = 0.8
tail_end_nor = 'high'
tail_end_low = 'low'

# Set the parameters for the different mouth stage
mouth_normal = 3.14
mouth_sad = 1

changed_stated = False

def stage(phase, last_phase):
    """
    :param phase: give a string of the different phases with the three first letters
    :return: a list of dictionaries in the order: 0:ears_list, 1:eyes_list, 2:tail_list, 3:mouth_pos
    """
    if last_phase is not phase:
        changed_state = True
    else:
        changed_state = False
    move_list = []
    ears_dict = {}
    eyes_dict = {}
    tail_dict = {}

    # All variables are set to the default setting (reg)
    ears_angle = ears_mid
    ears_pos = ears_pos_reg
    eyes_scale = eyes_reg
    eyes_big_bool = False
    eyes_open = True
    eyes_awake_closed = True
    tail_speed = tail_speed_slow
    tail_width = tail_width_normal
    tail_max_scale = tail_max_scale_reg
    tail_end = tail_end_nor
    mouth_pos = mouth_normal

    # The variables are changed if they are different then the default
    if phase == 'pet':
        ears_angle = ears_low
        ears_pos = ears_pos_high
        tail_speed = tail_speed_fast
        tail_max_scale = tail_max_scale_big
    if phase == 'scr':
        ears_angle = ears_high
        ears_pos = ears_pos_low
        eyes_scale = eyes_big
        eyes_big_bool = True
        tail_speed = tail_speed_fast
        tail_max_scale = tail_max_scale_big
        tail_end = tail_end_low
    if phase == 'pok':
        ears_angle = ears_low
        ears_pos = ears_pos_high
        eyes_open = False
        tail_speed = tail_speed_fast
        tail_max_scale = tail_max_scale_big
    if phase == 'com':
        ears_angle = ears_high
        ears_pos = ears_pos_low
        eyes_open = False
        eyes_awake_closed = False
        tail_end = tail_end_low
    if phase == 'hit':
        ears_angle = [ears_high, ears_low]
        ears_pos = [ears_pos_low, ears_pos_high]
        eyes_scale = [eyes_big, eyes_small]
        tail_speed = tail_speed_not
        tail_width = tail_width_sad
        mouth_pos = mouth_sad
    ears_dict['angle'] = ears_angle
    ears_dict['position'] = ears_pos

    eyes_dict['scale'] = eyes_scale
    eyes_dict['big_bool'] = eyes_big_bool
    eyes_dict['open_bool'] = eyes_open
    eyes_dict['closed_bool_awake'] = eyes_awake_closed

    tail_dict['speed'] = tail_speed
    tail_dict['width'] = tail_width
    tail_dict['max_scale'] = tail_max_scale
    tail_dict['end_point'] = tail_end

    move_list.append(ears_dict)
    move_list.append(eyes_dict)
    move_list.append(tail_dict)
    move_list.append(mouth_pos)
    move_list.append(changed_state)
    return move_list
