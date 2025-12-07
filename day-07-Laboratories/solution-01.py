from typing import List, Tuple

def parse_input(source: str) -> Tuple[List[List[int]], List[str]]:
    """
    Return a clean matrix of split positions
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    
    start_pos = lines[0].find("S")

    if start_pos == -1:
        raise ValueError("No starting position 'S' found in the input.")

    split_pos = []
    for line in lines:
        line_pos = []
        for idx, char in enumerate(line):
            if char == "^":
                line_pos.append(idx)
        split_pos.append(line_pos)


    return start_pos, split_pos


def find_nb_of_splits(
    source: str,
) -> int:
    """
    Find the number of time the beam splits on its way down.
    When it reaches a split position (^), it splits into two beams,
    one on the left and one on the right.
    """

    nb_of_splits = 0

    start_pos, split_pos = parse_input(source)

    beam_pos = set([start_pos])

    for i, row_splits in enumerate(split_pos):
        
        # If the beam position hits a split
        for beam in beam_pos.copy():
            if beam in row_splits:
                nb_of_splits += 1
                beam_pos.add(beam - 1)  # left beam
                beam_pos.add(beam + 1)  # right beam
                beam_pos.remove(beam)  # remove the original beam

    return nb_of_splits

if __name__ == "__main__":
    filename = "input.txt"
    print(find_nb_of_splits(filename))
