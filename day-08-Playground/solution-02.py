from typing import List

def parse_input(source: str) -> List[List[int]]:
    """
    Return a clean list of boxes positions (x,y,z).
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    
    return [list(map(int, line.strip().split(","))) for line in lines]

class Circuit:
    def __init__(self, box):
        self.boxes = set(box)

    def total_junctions(self) -> int:
        return len(self.boxes)
    
    def union(self, other: 'Circuit') -> 'Circuit':
        new_circuit = Circuit(self.boxes.union(other.boxes))
        return new_circuit

def find_best_junctions(
    source: str,
    max_connections: int = 1000
) -> int:
    """
    Return the two X coordinates multiplied together of the last junction formed.
    """

    boxes = parse_input(source)

    # 1. Compute the straight-line distance dict
    distance_matrix = {}
    
    for i, box_a in enumerate(boxes):
        for j, box_b in enumerate(boxes[i+1:], start=i+1):
            if i != j:
                dist = sum((a - b) ** 2 for a, b in zip(box_a, box_b))
                distance_matrix[(i, j)] = dist
    
    # 2. Order distances
    sorted_distances = sorted(distance_matrix.items(), key=lambda item: item[1])

    # 3. Create circuits and find the best 3 junctions
    circuits = set(Circuit([i]) for i in range(len(boxes)))

    for (box_a, box_b), dist in sorted_distances:

        circuit_a = next(c for c in circuits if box_a in c.boxes)
        circuit_b = next(c for c in circuits if box_b in c.boxes)

        if circuit_a != circuit_b:
            
            if len(circuits) <= 2:
                return boxes[box_a][0] * boxes[box_b][0]

            new_circuit = circuit_a.union(circuit_b)
            circuits.remove(circuit_a)
            circuits.remove(circuit_b)
            circuits.add(new_circuit)

    return -1  # In case no junctions are formed

if __name__ == "__main__":
    filename = "input.txt"
    print(find_best_junctions(filename))
