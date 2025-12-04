from typing import List

def parse_input(source: str) -> List[List[int]]:
    """Return a clean matrix of paper rolls from a file path."""
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    
    return [[1*(char == "@") for char in line.strip()] for line in lines if line.strip()]

def roll_is_accessible(
    grid: List[List[int]], 
    i: int, 
    j: int,
    nb_surrounding: int = 3
) -> bool:
    """Check if the paper roll at position (i, j) is accessible."""

    grid_height = len(grid)
    grid_width = len(grid[0]) if grid_height > 0 else 0

    surrounding_mat = [
        grid[x][y]
        for x in range(max(0, i-1), min(grid_height, i+2))
        for y in range(max(0, j-1), min(grid_width, j+2))
    ]

    return sum(surrounding_mat) <= nb_surrounding + 1  # including itself

def get_accessible_paper_rolls(
    source: str,
    nb_surrounding: int = 3
) -> int:
    """
    Returns the number of accessible paper rolls in the printing department.
    A paper roll is considered accessible if it's surrounded by max three rolls.
    """

    grid = parse_input(source)

    accessible_count = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell and roll_is_accessible(grid, i, j, nb_surrounding):
                accessible_count += 1

    return accessible_count


if __name__ == "__main__":
    filename = "input.txt"
    print(get_accessible_paper_rolls(filename))
