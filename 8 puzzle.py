import heapq

goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def heuristic(board):
    h = 0
    for i in range(9):
        if board[i] == 0:
            continue
        gx, gy = divmod(goal_state.index(board[i]), 3)
        x, y = divmod(i, 3)
        h += abs(gx - x) + abs(gy - y)
    return h

def solve_puzzle(initial_state):
    open_set = [(heuristic(initial_state), 0, initial_state)]
    closed_set = set()
    parent = {}
    
    while open_set:
        _, g, current_state = heapq.heappop(open_set)
        if current_state == goal_state:
            path = []
            while current_state in parent:
                path.append(current_state)
                current_state = parent[current_state]
            path.append(initial_state)
            path.reverse()
            return path
        closed_set.add(current_state)
        x, y = divmod(current_state.index(0), 3)
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = list(current_state)
                new_index = new_x * 3 + new_y
                new_state[x * 3 + y], new_state[new_index] = new_state[new_index], new_state[x * 3 + y]
                new_state = tuple(new_state)
                if new_state not in closed_set:
                    g_new = g + 1
                    h_new = heuristic(new_state)
                    f_new = g_new + h_new
                    if (h_new, g_new, new_state) not in open_set:
                        heapq.heappush(open_set, (f_new, g_new, new_state))
                        parent[new_state] = current_state
    return None

if __name__ == '__main__':
    initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # Change this to your initial state
    if sum(initial_state) % 2 != sum(goal_state) % 2:
        print("No solution exists")
    else:
        solution = solve_puzzle(initial_state)
        if solution:
            for step, state in enumerate(solution):
                print(f"Step {step + 1}:")
                print_board(state)
                print()
        else:
            print("No solution found.")
