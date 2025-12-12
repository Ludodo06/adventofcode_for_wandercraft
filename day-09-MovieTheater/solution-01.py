from typing import List

def parse_input(source: str) -> List[List[int]]:
    """
    Return a clean list of tile pisition (x,y).
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    
    return [(int(x), int(y)) for line in lines for x, y in [line.strip().split(",")]]

def find_biggest_rect(
    source: str
) -> int:
    """
    Find biggest rectangle from oppposite tiles.
    """

    tuiles = parse_input(source)

    biggest_rect = 0

    for i, tuile_i in enumerate(tuiles):
        for j, tuile_j in enumerate(tuiles[i+1:], start=i+1):
            rect = (abs(tuile_i[0] - tuile_j[0]) + 1) * \
                   (abs(tuile_i[1] - tuile_j[1]) + 1)
            if rect > biggest_rect:
                biggest_rect = rect

    return biggest_rect


if __name__ == "__main__":
    filename = "input.txt"
    print(find_biggest_rect(filename))
