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
    
    max_len = max(len(line) for line in lines)

    problems = []
    current_problem = []

    # To read vertically, we iterate over character positions
    # and pass to the next problem when we hit a blank column
    
    for char_idx in range(max_len):

        current_number_str = ""

        for line_idx in range(len(lines)-1):
            current_number_str += lines[line_idx][char_idx]

        if current_number_str.strip() == "":
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(int(current_number_str.strip()))

    opps = [op for op in lines[-1].split(" ") if op.strip() != ""]

    return problems, opps


def solve_math_problem(
    source: str,
) -> int:
    """
    Solve the math problem of the cephalopod's trash compactor (numbers are
    read vertically).

    e,g. for input:
    123 328  51 64 
     45 64  387 23 
      6 98  215 314
    *   +   *   +

    The result is: 

    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544

    Total: 1058 + 3253600 + 625 + 8544 = 3263827
    """

    numbers, opps = parse_input(source)

    total = 0

    for problem_nums, op in zip(numbers, opps):

        if op == "+":
            problem_sol = sum(problem_nums)

        elif op == "*":
            problem_sol = 1
            for n in problem_nums:
                problem_sol *= n

        else:
            raise ValueError(f"Unknown operation: {op}")
            
        total += problem_sol

    return total

if __name__ == "__main__":
    filename = "input.txt"
    print(solve_math_problem(filename))
