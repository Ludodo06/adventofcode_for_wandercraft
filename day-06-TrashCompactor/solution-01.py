from typing import List, Tuple

def parse_input(source: str) -> Tuple[List[List[int]], List[str]]:
    """
    Return two clean lists: 1st for the numbers to be processed,
    2nd for the operations to be performed.
    """
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        raise ValueError("Source must be a file path string.")
    

    numbers = [[int(num) for num in line.split(" ") if num.strip() != ""] for line in lines[:-1]]
    opps = [op for op in lines[-1].split(" ") if op.strip() != ""]

    if len(numbers[0]) != len(opps):
        raise ValueError("Number of operations must match number of number lines.")
        
    return numbers, opps


def solve_math_problem(
    source: str,
) -> int:
    """
    Solve the math problem of the cephalopod's trash compactor.

    e,g. for input:
    123 328  51 64 
     45 64  387 23 
      6 98  215 314
    *   +   *   +

    The result is: 
    
    123 * 45 * 6 = 33210
    328 + 64 + 98 = 490
    51 * 387 * 215 = 4243455
    64 + 23 + 314 = 401

    Total = 33210 + 490 + 4243455 + 401 = 4277556x
    """

    numbers, opps = parse_input(source)

    total = 0

    for idx, op in enumerate(opps):

        nums = [numbers[row][idx] for row in range(len(numbers))]
        problem_sol = 0

        if op == "+":
            problem_sol = sum(nums)

        elif op == "*":
            problem_sol = 1
            for n in nums:
                problem_sol *= n
                
        else:
            raise ValueError(f"Unknown operation: {op}")
        
        total += problem_sol

    return total

if __name__ == "__main__":
    filename = "input.txt"
    print(solve_math_problem(filename))
