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

def overlaps(tuile_a1, tuile_a2, tuile_b1, tuile_b2) -> bool:
    """
    Check if two rectangles defined by opposite corners (tuile_a1, tuile_a2)
    and (tuile_b1, tuile_b2) overlap.
    """
    return not (
        min(tuile_a1[0], tuile_a2[0]) >= max(tuile_b1[0], tuile_b2[0]) or
        max(tuile_a1[0], tuile_a2[0]) <= min(tuile_b1[0], tuile_b2[0]) or
        min(tuile_a1[1], tuile_a2[1]) >= max(tuile_b1[1], tuile_b2[1]) or
        max(tuile_a1[1], tuile_a2[1]) <= min(tuile_b1[1], tuile_b2[1])
    )

class Pair:
    def __init__(self, tuile1, tuile2):
        self.tuile1 = tuile1
        self.tuile2 = tuile2
    
    def area(self) -> int:
        return (abs(self.tuile1[0] - self.tuile2[0]) + 1) * \
               (abs(self.tuile1[1] - self.tuile2[1]) + 1)


def find_biggest_rect(
    source: str
) -> int:
    """
    Find biggest rectangle from oppposite tiles.
    """

    tuiles = parse_input(source)

    paires = [Pair(tuiles[i], tuiles[j]) for i in range(len(tuiles)) for j in range(i+1, len(tuiles))]
    paires.sort(key=lambda p: p.area(), reverse=True)

    edges = [Pair(tuiles[i-1], tuiles[i]) for i in range(len(tuiles))]

    best_pair = next(p for p in paires if not any(overlaps(p.tuile1, p.tuile2, e.tuile1, e.tuile2) for e in edges))

    biggest_rect = best_pair.area() if best_pair else 0

    return biggest_rect


if __name__ == "__main__":
    filename = "input.txt"
    print(find_biggest_rect(filename))
