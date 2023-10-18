from collections import deque

# Define the capacity of the two jugs
jug1_capacity = 4
jug2_capacity = 3

# Define the target volume to measure
target_volume = 2

# Function to represent the state of the jugs
class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __str__(self):
        return f"({self.jug1}, {self.jug2})"

# Function to check if the state is valid
def is_valid_state(state):
    return 0 <= state.jug1 <= jug1_capacity and 0 <= state.jug2 <= jug2_capacity

# Breadth-First Search to solve the Water Jug Problem
def solve_water_jug_problem():
    start_state = State(0, 0)
    visited = set()
    queue = deque([start_state])

    while queue:
        current_state = queue.popleft()

        if current_state.jug1 == target_volume or current_state.jug2 == target_volume:
            print("Solution found:", current_state)
            return

        # Fill Jug 1
        fill_jug1 = State(jug1_capacity, current_state.jug2)
        if is_valid_state(fill_jug1) and fill_jug1 not in visited:
            queue.append(fill_jug1)
            visited.add(fill_jug1)

        # Fill Jug 2
        fill_jug2 = State(current_state.jug1, jug2_capacity)
        if is_valid_state(fill_jug2) and fill_jug2 not in visited:
            queue.append(fill_jug2)
            visited.add(fill_jug2)

        # Empty Jug 1
        empty_jug1 = State(0, current_state.jug2)
        if is_valid_state(empty_jug1) and empty_jug1 not in visited:
            queue.append(empty_jug1)
            visited.add(empty_jug1)

        # Empty Jug 2
        empty_jug2 = State(current_state.jug1, 0)
        if is_valid_state(empty_jug2) and empty_jug2 not in visited:
            queue.append(empty_jug2)
            visited.add(empty_jug2)

        # Pour water from Jug 1 to Jug 2
        pour_jug1_to_jug2 = State(max(0, current_state.jug1 - (jug2_capacity - current_state.jug2)), min(jug2_capacity, current_state.jug2 + current_state.jug1))
        if is_valid_state(pour_jug1_to_jug2) and pour_jug1_to_jug2 not in visited:
            queue.append(pour_jug1_to_jug2)
            visited.add(pour_jug1_to_jug2)

        # Pour water from Jug 2 to Jug 1
        pour_jug2_to_jug1 = State(min(jug1_capacity, current_state.jug1 + current_state.jug2), max(0, current_state.jug2 - (jug1_capacity - current_state.jug1)))
        if is_valid_state(pour_jug2_to_jug1) and pour_jug2_to_jug1 not in visited:
            queue.append(pour_jug2_to_jug1)
            visited.add(pour_jug2_to_jug1)

    print("No solution found.")

if __name__ == "__main__":
    solve_water_jug_problem()
