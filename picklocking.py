import os

lines = open("initial.txt", "r").readlines();
if len(lines) != 1:
    print("Invalid input in input.txt. The number of lines should be exactly 1.")
    exit(0)

if len(lines[0].strip()) == 0:
    print("Invalid input in input.txt. The line should not be empty.")
    exit(0)

initial = tuple()
for c in lines[0].strip():
    if c < '1' or c > '7':
        print("Invalid input in input.txt. Each character should be a digit between 1 and 7.")
        exit(0)
    
    initial = initial + (int(c),)

lines = open("max_depth.txt", "r").readlines();
if len(lines) != 1:
    print("Invalid input in max_depth.txt. The number of lines should be exactly 1.")
    exit(0)

try:
    MAX_DEPTH = int(lines[0].strip())
except ValueError:
    print('Invalid input in max_depth.txt. The line should be an integer.')
    exit(0)

if MAX_DEPTH < 1:
    print('Invalid input in max_depth.txt. The integer should be a positive integer.')
    exit(0)

print(MAX_DEPTH)
# Initial positions
SECTIONS=len(initial)

lines = open("moves.txt", "r").readlines();
if len(lines) != SECTIONS:
    print("Invalid input in moves.txt. The number of lines should be exactly " + str(SECTIONS) + ".")
    exit(0)

coupling = []
for line in lines:
    if len(line.strip()) != SECTIONS:
        print("Invalid input in moves.txt. Each line should have exactly " + str(SECTIONS) + " characters.")
        exit(0)

    move = []
    for c in line.strip():
        if c not in ['F', 'R', 'N']:
            print("Invalid input in moves.txt. Each character should be either 'F', 'R' or 'N'.")
        if c == 'F':
            move.append(1)
        elif c == 'R':
            move.append(-1)
        else:
            move.append(0)
    
    coupling.append(move)

print(coupling)
# Coupling matrix
coupling = [
    [ 1,  1,  0,  0,  0, 1],
    [ 0,  1,  1,  0,  0, -1],
    [ 0,  0,  1,  1,  0,  0],
    [ 0,  0,  0,  1,  0,  0],
    [ 0,  0,  1,  0,  1,  1],
    [ 0,  0,  0,  0,  0,  1],
]

exit()
# SECTIONS=2
# # Initial positions
# initial = (5, 3)
# # Coupling matrix
# coupling = [
#     [ 1,  -1],
#     [ 1,  1],
# ]
goal = tuple([4] * SECTIONS)

# reversed is "1" or "-1" depending on whether the move is reversed or not
def apply_move(state, move, reversed):
    new_state = list(state)
    for i in range(SECTIONS):
        new_state[i] +=coupling[move][i] * reversed
    return tuple(new_state)

def is_valid(state):
    for i in range(SECTIONS):
        if state[i] < 1 or state[i] > 7:
            return False
    return True


combinations = dict({initial: []})
def push_reached_combination(cur_state, next_state, move, reversed):
    if combinations.get(next_state) is not None:
        return

    cur_combination = combinations.get(cur_state).copy()
    cur_combination.append((move, reversed))
    combinations[next_state] = cur_combination.copy()

    return True


current_combinations = set([initial])
next_combinations = set()
depth = 0
goal_found = False
while not goal_found and depth < MAX_DEPTH:
    depth += 1

    for combination in current_combinations:
        for move in range(SECTIONS):
            for reversed in [1, -1]:
                new_combination = apply_move(combination, move, reversed)
                if is_valid(new_combination):
                    next_combinations.add(new_combination)
                    push_reached_combination(combination, new_combination, move, reversed)


    current_combinations = next_combinations
    next_combinations = set()

    for combination in current_combinations:
        if goal == combination:
            print("Goal reached: ", combination)
            goal_found = True
            break


def calculate_key_sequence(combination):
    curr_segment = 0
    keys = []
    for move, reversed in combination:
        diff = curr_segment - move
        for i in range(-diff):
            keys.append("W")
        for i in range(diff):
            keys.append("S")

        curr_segment = move

        if reversed == 1:
            keys.append("D")
        else:
            keys.append("A")

    return keys

if goal_found:
    print("Goal found at depth: ", depth)
    winning_combination = combinations.get(goal)
    winning_combination2 = winning_combination.copy()
    print("Winning combination: ", winning_combination)
    combination = initial
    while goal != combination:
        print("Current combination: ", combination)
        move, reversed = winning_combination.pop(0)
        combination = apply_move(combination, move, reversed)

    print("key sequence:" , calculate_key_sequence(winning_combination2))
else:
    print("Goal not found within depth limit.")
    
# print(current_combinations)
# print(combinations)
    
