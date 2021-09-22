from interpreter import interpret

def train():
    running = True
    while running:
        # choose action
        if config_in_training() or explore_action():
            action = act(state)
            done, reward, state = step(action)
            score += reward


def config_in_training():
    return True


def explore_action():
    return True


def step(action):
    reward = 1
    done = 0

    # add character to program
    # if action ...
    program = "++[.-]"

    # run program (interpret)
    printed, memory, memory_pointer = interpret(program)

    # get state
    state = [printed, memory, memory_pointer]

    return reward, state, done


def calculate_reward(actual_print, target_print):
    return (character_count_reward(actual_print, target_print)
            + correct_character_reward(actual_print, target_print)
            + character_position_reward(actual_print, target_print))


# points for the correct amount of characters, 0 points if too many
def character_count_reward(actual_print, target_print):
    actual_len = len(actual_print)
    target_len = len(target_print)
    return actual_len if target_len >= actual_len else 0


# 1 point per correct character (not influenced by position)
def correct_character_reward(actual_print, target_print):
    # build mapping of characters in target
    character_map = {}
    for char in target_print:
        if char in character_map:
            character_map[char] += 1
        else:
            character_map[char] = 1

    # count the correct amount of characters
    correct_characters = 0
    for char in actual_print:
        if char in character_map and character_map[char] > 0:
            character_map[char] -= 1
            correct_characters += 1
        else:
            character_map[char] = 1

    return correct_characters


# 1 point per correct character on the correct position
def character_position_reward(actual_print, target_print):
    comparison_list = zip(actual_print, target_print)
    only_equals = filter(lambda tup: tup[0] == tup[1], comparison_list)
    return len(only_equals)
