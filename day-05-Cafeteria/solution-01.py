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
    Return the number of wanted ingredients that are fresh.
    """

    fresh_ingredient_ranges, wanted_ingredients = parse_input(source)

    fresh_ingredients = set()

    for ingredient in wanted_ingredients:
        for (start, end) in fresh_ingredient_ranges:
            if start <= ingredient <= end:
                fresh_ingredients.add(ingredient)
                break
    
    return len(fresh_ingredients)


if __name__ == "__main__":
    filename = "input.txt"
    print(get_fresh_ingredients(filename))
