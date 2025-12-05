from typing import List, Tuple

def parse_input(source: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    """
    Return two clean lists: 1st for the fresh ingredient ranges, 
    2nd for the wanted ingredients.
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    
    fresh_ingredient_ranges = []
    wanted_ingredients = []

    line_idx = 0

    while lines[line_idx].strip() != "":
        range_ids = lines[line_idx].strip().split("-")
        fresh_ingredient_ranges.append((int(range_ids[0]), int(range_ids[1])))
        line_idx += 1
    
    line_idx += 1  # skip the blank line

    while line_idx < len(lines):
        wanted_ingredients.append(int(lines[line_idx].strip()))
        line_idx += 1

    return fresh_ingredient_ranges, wanted_ingredients

def get_fresh_ingredients(
    source: str,
) -> int:
    """
    Return the number of ALL ingredients that are fresh.

    Putting everything in a set is too long to run for part 2,
    so we merge the ranges and sum the merged lengths (avoids double-counting).
    """

    fresh_ingredient_ranges, _ = parse_input(source)
    if not fresh_ingredient_ranges:
        return 0

    # Sort ranges by start (then end) and merge overlapping/adjacent intervals
    sorted_ranges = sorted(fresh_ingredient_ranges)

    merged_start, merged_end = sorted_ranges[0]
    total = 0

    for start, end in sorted_ranges[1:]:
        if start <= merged_end + 1:  # Overlapping or adjacent ranges
            # Extend the merged range (or not if next range is inside the current merged range)
            merged_end = max(merged_end, end) 
        else:
            # If no overlap, add the length of the merged range (previous) to total
            total += (merged_end - merged_start + 1)
            # And start a new merged range
            merged_start, merged_end = start, end

    # Add the last merged range
    total += (merged_end - merged_start + 1)
    
    return total

#### OTHER APPROACH (less efficient) ####

# def get_fresh_ingredients(
#     source: str,
# ) -> int:
#     """
#     Return the number of ALL ingredients that are fresh.

#     Putting everything in a set is too long to run for part 2,
#     so we just count the ranges directly (not forgetting to avoid double-counting).
#     """

#     fresh_ingredient_ranges, _ = parse_input(source)

#     nb_fresh_ingredients = 0

#     covered = []

#     for start, end in fresh_ingredient_ranges:
#         # remove overlaps with previous ranges
#         for (ov_start, ov_end) in covered:
#             if ov_start <= start <= ov_end:
#                 start = ov_end + 1
#             if ov_start <= end <= ov_end:
#                 end = ov_start - 1
#             if start <= ov_start and ov_end <= end:
#                 # current range fully covers previous one
#                 covered.remove((ov_start, ov_end))
#                 nb_fresh_ingredients -= (ov_end - ov_start + 1)
#         if start <= end:
#             nb_fresh_ingredients += (end - start + 1)
#             covered.append((start, end))
    
#     return nb_fresh_ingredients

if __name__ == "__main__":
    filename = "input.txt"
    print(get_fresh_ingredients(filename))
