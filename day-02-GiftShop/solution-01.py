from typing import List

def parse_input(source: str) -> List[List[int]]:
    """Return a clean list of ID range of the form [[start0, end0], [start1, end1], ...]."""
    if isinstance(source, str):
        with open(source, "r") as f:
            line = f.readline().strip()
    else:
        raise ValueError("Source must be a file path string.")

    ranges = line.split(",")
    return [[int(start), int(end)] for start, end in (r.split("-") for r in ranges)]

def track_invalid_ids(
    source: str,
) -> dict:
    """
    Tracks invalid gift shop item IDs based on provided ID ranges.
    An ID is invalid if it has two repeated sequence of digits (e.g., 11, 1010, 123123)
    """

    id_ranges = parse_input(source)
    invalid_ids = set()
    total_sum = 0

    # Goal: go through all ID ranges and find invalid IDs by
    # splitting each ID into two halves and checking if they are equal.
    for start, end in id_ranges:
        for test_id in range(start, end + 1):
            id_str = str(test_id)
            length = len(id_str)
            if length % 2 == 0:
                first_half = id_str[:length // 2]
                second_half = id_str[length // 2:]
                if first_half == second_half:
                    invalid_ids.add(test_id)
    
    total_sum = sum(invalid_ids)
    return {"number_of_invalid_ids": len(invalid_ids), 
            "sum": total_sum}

if __name__ == "__main__":
    filename = "input.txt"
    print(track_invalid_ids(filename))
