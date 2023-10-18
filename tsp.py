import itertools

# Define the cities and their coordinates
cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (9, 3),
}

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def total_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i + 1]])
    dist += distance(cities[route[-1]], cities[route[0]])
    return dist

def brute_force_tsp(cities):
    min_route = None
    min_distance = float('inf')
    city_permutations = itertools.permutations(cities)

    for route in city_permutations:
        route_distance = total_distance(route)
        if route_distance < min_distance:
            min_distance = route_distance
            min_route = route

    return min_route, min_distance

if __name__ == "__main__":
    optimal_route, min_distance = brute_force_tsp(cities.keys())
    
    print("Optimal Route:", optimal_route)
    print("Total Distance:", min_distance)
