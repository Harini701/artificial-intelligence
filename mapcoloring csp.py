class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors

    def is_assignment_valid(self, variable, color, assignment):
        for neighbor in self.neighbors[variable]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # All variables are assigned

        unassigned = [var for var in self.variables if var not in assignment]

        first_unassigned = unassigned[0]

        for color in self.domains[first_unassigned]:
            if self.is_assignment_valid(first_unassigned, color, assignment):
                assignment[first_unassigned] = color
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[first_unassigned]

        return None  # No valid assignment found

def main():
    # Define the variables, domains, and neighbors for the map coloring problem.
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains = {var: ["Red", "Green", "Blue"] for var in variables}
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": [],
    }

    csp = MapColoringCSP(variables, domains, neighbors)
    assignment = csp.backtracking_search()

    if assignment:
        print("Solution found:")
        for variable, color in assignment.items():
            print(f"{variable}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
