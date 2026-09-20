# code-corner

Small programming problems, each solved in a few different languages, plus a script that checks every solution against test cases.

## Running the checks

```
python3 run.py            # every problem
python3 run.py prime      # just one
```

It needs Python 3. On Windows the command is `python`. Solutions in languages you don't have installed are skipped. Codespaces has all of them: Python, Node, C, C++, Java, Go and Rust.

## Layout

```
problems/
  prime/
    README.md       what the program has to do
    cases.txt       one test per line: input | expected output
    solution.cpp
    solution.py
```

Every solution reads its input from stdin and prints the answer. Java files are named `Solution.java` with a `Solution` class.

## Contributing

- Add a solution in a language a problem doesn't have yet (`solution.rs`, `solution.c`, ...).
- Add test cases to a `cases.txt`, especially edge cases the README mentions but the cases don't cover yet.
- Add a new problem: a folder with a `README.md`, a `cases.txt` and at least one solution.
- If a solution gives the wrong answer for an input the README says it should handle, that's a bug. Open an issue with the input, the expected output and what you got, then fix it and add the input to `cases.txt`.

Run `python3 run.py` before opening a pull request. It also runs on every pull request.

Part of Source Start by CSI SPIT. MIT licensed.
