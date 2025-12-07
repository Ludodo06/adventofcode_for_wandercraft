from typing import List, Tuple
from collections import defaultdict
import time


def parse_input(source: str) -> Tuple[int, List[List[int]]]:
    """Return starting column index and list of split positions per row.

    `start_pos` is the column index of the 'S' in the first line.
    `split_pos` is a list (per row) of column indices where '^' appears.
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")

    if not lines:
        raise ValueError("Empty input file")

    start_pos = lines[0].find("S")
    if start_pos == -1:
        raise ValueError("No starting position 'S' found in the input.")

    split_pos: List[List[int]] = []
    for line in lines:
        # ignore newline when computing indices
        row = line.rstrip("\n")
        row_pos = [idx for idx, ch in enumerate(row) if ch == "^"]
        split_pos.append(row_pos)

    return start_pos, split_pos


def find_nb_of_timelines(source: str) -> int:
    """Compute number of distinct timelines using counts per column.

    What we can do is to keep track, for each column, how many different
    timelines it holds. When we reach a split position, the number of timelines
    at col[i] is added to col[i-1] and col[i+1].
    """
    start_pos, split_pos = parse_input(source)

    timeline_counts = {start_pos: 1}
    
    for row_splits in split_pos:

        for col, count in timeline_counts.copy().items():
            if col in row_splits:
                # Split occurs here
                timeline_counts[col - 1] = timeline_counts.get(col - 1, 0) + count
                timeline_counts[col + 1] = timeline_counts.get(col + 1, 0) + count
                timeline_counts[col] = 0 

    total_timelines = sum(timeline_counts.values())
    return total_timelines


if __name__ == "__main__":
    filename = "input.txt"
    print(find_nb_of_timelines(filename))
