import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(graph, start, goal):
    open_set = [Node(start, None, 0, heuristic(start, goal))]
    closed_set = set()
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.state == goal:
            return reconstruct_path(current)
        
        closed_set.add(current.state)
        
        for neighbor, cost in graph[current.state]:
            if neighbor in closed_set:
                continue
            
            tentative_cost = current.cost + cost
            neighbor_node = Node(neighbor, current, tentative_cost, heuristic(neighbor, goal))
            
            if not node_in_list(open_set, neighbor_node) or tentative_cost < get_node_cost(open_set, neighbor_node):
                heapq.heappush(open_set, neighbor_node)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

def heuristic(node, goal):
    return 0

def node_in_list(node_list, target_node):
    return any(node.state == target_node.state for node in node_list)

def get_node_cost(node_list, target_node):
    for node in node_list:
        if node.state == target_node.state:
            return node.cost
    return float('inf')

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    goal_node = 'D'

    path = astar(graph, start_node, goal_node)

    if path:
        print("Shortest path:", path)
        print("Total cost:", sum(graph[node1][node2] for node1, node2 in zip(path, path[1:])))
    else:
        print("No path found.")
