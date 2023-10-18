from collections import deque

initial_state = (3, 3, 1) 
final_state = (0, 0, 0)

def is_valid(state):
    missionaries_left, cannibals_left, boat_position = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    if (missionaries_left < 0 or missionaries_left > 3 or
        cannibals_left < 0 or cannibals_left > 3 or
        missionaries_right < 0 or missionaries_right > 3 or
        cannibals_right < 0 or cannibals_right > 3):
        return False

    if (missionaries_left < cannibals_left and missionaries_left > 0) or (missionaries_right < cannibals_right and missionaries_right > 0):
        return False

    return True

def solve_missionaries_and_cannibals():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == final_state:
            return path + [final_state]

        if current_state in visited:
            continue

        visited.add(current_state)

        missionaries, cannibals, boat_position = current_state
        new_boat_position = 1 - boat_position  # Switch the boat position

        # Generate all possible moves from the current state
        possible_moves = [(m, c) for m in range(3 + 1) for c in range(3 + 1) if 1 <= m + c <= 2]

        for move in possible_moves:
            m, c = move
            if boat_position == 1:
                new_state = (missionaries - m, cannibals - c, new_boat_position)
            else:
                new_state = (missionaries + m, cannibals + c, new_boat_position)

            if is_valid(new_state):
                new_path = path + [current_state]
                queue.append((new_state, new_path))

    return None

def print_solution(path):
    for state in path:
        missionaries, cannibals, boat_position = state
        missionaries_right = 3 - missionaries
        cannibals_right = 3 - cannibals
        if boat_position == 1:
            print(f"Left: {missionaries}M {cannibals}C | Right: {missionaries_right}M {cannibals_right}C | Boat: L->R")
        else:
            print(f"Left: {missionaries}M {cannibals}C | Right: {missionaries_right}M {cannibals_right}C | Boat: R->L")
    print("Goal reached!")

if __name__ == "__main__":
    path = solve_missionaries_and_cannibals()
    if path:
        print_solution(path)
    else:
        print("No solution found.") 
