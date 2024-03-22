import random

def generate_sudoku():
    # Generate a solved Sudoku puzzle
    grid = [[(i*3 + i//3 + j) % 9 + 1 for j in range(9)] for i in range(9)]
    # Shuffle rows within each 3x3 box
    for box_row in range(3):
        random.shuffle(grid[box_row*3:box_row*3+3])
    # Transpose to shuffle columns within each 3x3 box
    grid = list(map(list, zip(*grid)))
    for box_col in range(3):
        random.shuffle(grid[box_col*3:box_col*3+3])
    # Remove numbers randomly to create the puzzle
    for _ in range(45):  # Adjust this number to control difficulty
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        grid[row][col] = 0
    return grid

def is_valid_move(grid, row, col, num):
    # Check if placing 'num' at position (row, col) is valid
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    # Solve the Sudoku puzzle using backtracking
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty_cell(grid):
    # Find the first empty cell in the Sudoku grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_sudoku(grid):
    # Print the Sudoku grid
    for row in grid:
        print(" ".join(map(str, row)))

def main():
    print("Welcome to Sudoku Solver!")
    print("Generating a new Sudoku puzzle...\n")
    sudoku_grid = generate_sudoku()
    print("Initial Sudoku Puzzle:")
    print_sudoku(sudoku_grid)
    print("\nSolving the Sudoku puzzle...\n")
    if solve_sudoku(sudoku_grid):
        show_solved = input("Do you want to see the solved Sudoku puzzle? (yes/no): ").lower()
        if show_solved in ["yes", "y"]:
            print("\nSolved Sudoku Puzzle:")
            print_sudoku(sudoku_grid)
        else:
            print("\nOkay, the solved Sudoku puzzle will not be displayed.")
    else:
        print("Error: Unable to solve Sudoku puzzle.")

if __name__ == "__main__":
    main()
