#!/usr/bin/env python3
"""
Run all solution scripts and fill the answers table in README.md.

Behavior:
- For each folder matching `day-??-*`, run `solution-01.py` and `solution-02.py` if present.
- Capture stdout; the answer is taken as the last non-empty line of stdout.
- Update `README.md` replacing the Day XX Part lines with the captured answers.

Run from repository root: `python run_all.py`
"""
from pathlib import Path
import subprocess
import re

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"

def run_solution(day_dir: Path, script_name: str):
    script_path = day_dir / script_name
    if not script_path.exists():
        return None
    try:
        proc = subprocess.run(["python", script_name], cwd=day_dir, capture_output=True, text=True, timeout=30)
    except Exception as e:
        return f"ERROR: {e}"

    if proc.returncode != 0:
        # include stderr to help debugging
        err = proc.stderr.strip()
        out = proc.stdout.strip()
        msg = err if err else out if out else f"EXIT {proc.returncode}"
        return f"ERROR: {msg}"

    # choose last non-empty line of stdout as the answer
    lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    return lines[-1] if lines else ""

def find_days(root: Path):
    days = sorted([p for p in root.iterdir() if p.is_dir() and p.name.startswith("day-")])
    return days

def update_readme(answers: dict):
    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()

    # find Answers section start and Notes section start
    start_idx = None
    end_idx = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("**Answers**"):
            start_idx = idx
        if line.strip().startswith("**Notes**"):
            end_idx = idx
            break

    # build new answers block as a Markdown table
    # answers mapping: daynum -> (name, part1, part2)
    def esc(s: str) -> str:
        if s is None:
            return ""
        s = str(s)
        s = s.replace("&", "&amp;")
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        s = s.replace('"', "&quot;")
        s = s.replace("\n", " ")
        return s

    answer_lines = [lines[start_idx]]
    answer_lines.append("")
    answer_lines.append("| Day | Name | Part 1 | Part 2 |")
    answer_lines.append("|---:|---|---:|---:|")

    for daynum in sorted(answers.keys()):
        name, p1, p2 = answers[daynum]
        name = name or ""
        # show a visually-hidden placeholder and put the real answer in the title tooltip
        def cell(val):
            if not val:
                return ""
            t = esc(val)
            return f'<span title="{t}">•••</span>'

        p1cell = cell(p1)
        p2cell = cell(p2)
        # format name: remove leading 'day-XX-' and replace remaining hyphens with spaces
        # e.g. 'day-01-SecretEntrance' -> 'SecretEntrance' or 'day-02-Gift-Shop' -> 'Gift Shop'
        display_name = re.sub(r'^day-\d{2}-', '', name).replace('-', ' ')
        answer_lines.append(f"| {int(daynum)} | {display_name} | {p1cell} | {p2cell} |")

    answer_lines.append("")

    # replace the block between start_idx and end_idx (exclusive of end_idx)
    new_lines = lines[:start_idx] + answer_lines + lines[end_idx:]

    new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
    README.write_text(new_text, encoding="utf-8")
    return len(answers)

def main():
    days = find_days(ROOT)
    answers = {}
    for d in days:
        m = re.match(r"day-(\d{2})", d.name)
        if not m:
            continue
        daynum = m.group(1)
        p1 = run_solution(d, "solution-01.py")
        p2 = run_solution(d, "solution-02.py")
        answers[daynum] = (d.name, p1 or "", p2 or "")
        print(f"Day {daynum} ({d.name}): Part1={p1!r} Part2={p2!r}")

    replaced = update_readme(answers)
    print(f"README updated: {replaced} day entries replaced")

if __name__ == "__main__":
    main()
