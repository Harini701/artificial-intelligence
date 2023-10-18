import random

# Define a grid with cells (0: Dirty, 1: Clean)
grid = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]

def display_grid():
    for row in grid:
        print(" ".join(["D" if cell == 0 else "C" for cell in row]))
    print()

def clean_cell(x, y):
    grid[x][y] = 1
    print(f"Cleaned cell ({x}, {y})")

def vacuum_cleaner():
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                clean_cell(row, col)

    print("Cleaning complete.")

if __name__ == "__main__":
    print("Initial Grid:")
    display_grid()
    vacuum_cleaner()
