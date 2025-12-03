from typing import List

def parse_input(source: str) -> List[List[int]]:
    """Return a clean list of banks joltage from a file path."""
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")

    return [[int(joltage) for joltage in line.strip()] for line in lines if line.strip()]

def get_highest_joltages(
    source: str,
) -> int:
    """
    Returns the highest joltages from the provided banks.
    Each bank contains a list of battery joltages, and the highest joltage
    for a bank is calculated by selecting two digits (left to right) forming
    the highest possible number (e.g., for bank [17548], the highest joltage is 78).
    """

    banks = parse_input(source)
    total_joltage = 0

    for bank in banks:

        first_battery = max(bank[:-1])

        second_battery = max(bank[bank.index(first_battery) + 1:])

        bank_joltage = first_battery * 10 + second_battery

        total_joltage += bank_joltage

    return total_joltage


if __name__ == "__main__":
    filename = "input.txt"
    print(get_highest_joltages(filename))
