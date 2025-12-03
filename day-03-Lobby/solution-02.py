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
    for a bank is calculated by selecting TWELVE digits (left to right) forming
    the highest possible number :

    e.g., in 234234234234278, the largest joltage can be found by turning on everything
    except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    """

    banks = parse_input(source)
    total_joltage = 0

    for bank in banks:

        bank_joltage = ''
        last_battery_index = -1

        for i in range(12, 0, -1):

            # Limit the search of each battery to the right of the last selected battery
            # e.g., step 1: [2342]34234234278, step 2: 234[23]4234234278, etc.
            idx_range_min = last_battery_index + 1

            if idx_range_min + i == len(bank):
                # If we have exactly enough batteries left to fill the remaining slots,
                # we have to take them all.
                bank_joltage += ''.join(str(b) for b in bank[idx_range_min:])
                break
            
            # Limit the search to ensure enough batteries remain to fill the remaining slots
            idx_range_max = -i + 1 if i != 1 else None

            # Find the max battery in the allowed range
            battery = max(bank[idx_range_min:idx_range_max])

            # Update the last selected battery index
            last_battery_index = bank.index(battery, idx_range_min)

            # Update the bank joltage by adding the selected battery
            bank_joltage += str(battery)

        total_joltage += int(bank_joltage)

    return total_joltage


if __name__ == "__main__":
    filename = "input.txt"
    print(get_highest_joltages(filename))
