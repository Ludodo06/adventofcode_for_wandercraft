from typing import Iterable, List, Union

def parse_commands(source: Union[str, Iterable[str]]) -> List[str]:
    """Return a clean list of commands from a file path or iterable."""
    if isinstance(source, str):
        with open(source, "r") as f:
            lines = f.readlines()
    else:
        lines = list(source)

    return [line.strip() for line in lines if line.strip()]

def count_dial_hits(
    source: Union[str, Iterable[str]],
    start: int = 50,
    modulo: int = 100,
    target: int = 0
) -> int:
    """
    Count how many times the dial reaches `target` after applying turn commands.
    Commands are of the form 'L<num>' or 'R<num>'.
    """
    
    dial = start
    target_count = 0

    for cmd in parse_commands(source):

        direction = cmd[0]
        clicks = int(cmd[1:])
        
        if direction not in ("L", "R"):
            raise ValueError(f"Invalid command: {cmd}")
        
        delta = clicks if direction == 'R' else -clicks
        dial = (dial + delta) % modulo

        # Check if dial is at target
        if dial == target:
            target_count += 1

    return target_count

if __name__ == "__main__":
    filename = "input.txt"
    print(count_dial_hits(filename))