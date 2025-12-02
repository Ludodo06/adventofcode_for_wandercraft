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
    An ID is invalid if it has AT LEAST TWO repeated sequence of digits (e.g., 11, 121212, 33333333)
    """

    id_ranges = parse_input(source)
    invalid_ids = set()
    total_sum = 0

    # Goal: go through all ID ranges and find invalid IDs by
    # seeing if the ID can be constructed by repeating a sequence of digits.
    for start, end in id_ranges:
        for test_id in range(start, end + 1):
            id_str = str(test_id)
            length = len(id_str)

            # 1. Find divisors of the length
            divisors = [d for d in range(1, length // 2 + 1) if length % d == 0]

            # 2. Check for each divisor if the ID can be constructed by repeating a sequence
            for d in divisors:                          # Example: d = 1,2,3 for 151515
                sequence = id_str[:d]                   # Example: sequence = "1","15","151"
                if sequence * (length // d) == id_str:  # Example: "1"*6="111111", "15"*3="151515" [HIT!], "151"*2="151515"
                    invalid_ids.add(test_id)            # Example: add 151515 to invalid IDs
                    break  # No need to check further divisors (e.g., we stop after finding d=2 for 151515)
    
    total_sum = sum(invalid_ids)
    return {"number_of_invalid_ids": len(invalid_ids), 
            "sum": total_sum}

if __name__ == "__main__":
    filename = "input.txt"
    print(track_invalid_ids(filename))
