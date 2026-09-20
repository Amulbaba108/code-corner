"""Runs every solution against its problem's cases.txt.

    python run.py               # everything
    python run.py prime         # one problem
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROBLEMS = Path(__file__).parent / "problems"

# extension -> (tool that must be installed, compile command or None, run command)
# {src} is the source file, {out} a temp directory for build output.
LANGUAGES = {
    ".py": ("python3", None, ["python3", "{src}"]),
    ".js": ("node", None, ["node", "{src}"]),
    ".c": ("cc", ["cc", "-O2", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".cpp": ("c++", ["c++", "-std=c++17", "-O2", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".java": ("javac", ["javac", "-d", "{out}", "{src}"], ["java", "-cp", "{out}", "Solution"]),
    ".go": ("go", ["go", "build", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".rs": ("rustc", ["rustc", "-O", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
}


def fill(cmd, src, out):
    return [part.format(src=src, out=out) for part in cmd]


def read_cases(problem):
    cases = []
    for line in (problem / "cases.txt").read_text().splitlines():
        if line.strip():
            given, expected = line.rsplit("|", 1)
            cases.append((given.strip(), expected.strip()))
    return cases


def run_solution(src, cases):
    """Returns a list of failure messages. Empty means every case passed."""
    tool, compile_cmd, run_cmd = LANGUAGES[src.suffix]
    if shutil.which(tool) is None:
        print(f"  skip  {src.name} ({tool} isn't installed)")
        return []
    with tempfile.TemporaryDirectory() as out:
        if compile_cmd:
            result = subprocess.run(fill(compile_cmd, src, out), capture_output=True, text=True)
            if result.returncode != 0:
                return [f"didn't compile:\n{result.stderr}"]
        failures = []
        for given, expected in cases:
            try:
                result = subprocess.run(fill(run_cmd, src, out), input=given + "\n", capture_output=True, text=True, timeout=10)
                got = result.stdout.strip()
            except subprocess.TimeoutExpired:
                got = "(took longer than 10 seconds)"
            if got != expected:
                failures.append(f"input {given!r}: expected {expected!r}, got {got!r}")
        return failures


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    failed = 0
    for problem in sorted(PROBLEMS.iterdir()):
        if only and problem.name != only:
            continue
        print(problem.name)
        cases = read_cases(problem)
        for src in sorted(problem.iterdir()):
            if src.suffix not in LANGUAGES:
                continue
            failures = run_solution(src, cases)
            if failures:
                failed += 1
                print(f"  FAIL  {src.name}")
                for f in failures:
                    print(f"        {f}")
            elif shutil.which(LANGUAGES[src.suffix][0]):
                print(f"  ok    {src.name}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
