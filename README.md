# Python untuk Pemula

Practice repository for the **"Praktikum Python untuk Pemula"** assignment. It covers the basics of Python, from the first `print()` to classes, plus pip, virtual environments, and IDE configuration.

All chapter examples are written in a single file, `main.py`. Each chapter is committed separately, together with a screenshot of its output in the `screenshots/` folder.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Chapters](#chapters)
- [Dependencies](#dependencies)
- [Commit Convention](#commit-convention)
- [Author](#author)

## Project Structure

```text
python-untuk-pemula/
├── .vscode/
│   └── settings.json      # VS Code workspace settings
├── screenshots/           # Execution proof for each chapter
├── venv/                  # Virtual environment (ignored by Git)
├── .gitignore
├── main.py                # All chapter examples in one file
├── README.md
└── requirements.txt       # Project dependencies
```

## Requirements

- Python 3 (developed with Python 3.15.2)
- Git
- Visual Studio Code (recommended)
- Windows PowerShell (the commands below are written for it)

## Getting Started

1. Clone the repository:

   ```powershell
   git clone https://github.com/bainalhkim/python-untuk-pemula.git
   cd python-untuk-pemula
   ```

2. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

3. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks the script, run this once in the same window and activate again:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

4. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Run the program:

   ```powershell
   python main.py
   ```

Running `main.py` prints the output of every chapter in order. The last section uses `colorama`, so the virtual environment must be active, otherwise Python raises `ModuleNotFoundError`.

## Chapters

| No | Chapter | Topics | Screenshot |
|----|---------|--------|------------|
| 1 | Introduction and Installation | First program with `print()` | `screenshots/ch01-introduction.png` |
| 2 | Variables and Data Types | Integer, float, string, multiline string, boolean | `screenshots/ch02-variables.png` |
| 3 | Operators | Arithmetic, comparison, logical (`and`, `or`, `not`) | `screenshots/ch03-operators.png` |
| 4 | Conditionals | `if`, `elif`, `else`, indentation | `screenshots/ch04-conditionals.png` |
| 5 | Loops | `for`, `while`, `range()`, `break`, `continue` | `screenshots/ch05-loops.png` |
| 6 | Lists and Dictionaries | Indexing, `append`, `insert`, `remove`, `pop`, `clear`, `extend`; keys, values, `get`, `update` | `screenshots/ch06-lists.png`, `screenshots/ch07-dictionaries.png` |
| 7 | Functions | Arguments, `*args`, keyword arguments, `**kwargs`, default values | `screenshots/ch08-functions.png` |
| 8 | Classes and Objects | Class, object, constructor (`__init__`), methods, `self` | `screenshots/ch09-classes.png` |
| 9 | PIP and Virtual Environments | `venv`, `pip install`, `pip list`, `colorama` | `screenshots/ch09-pip-venv.png` |
| 10 | Environment and IDE Configuration | VS Code interpreter and workspace settings | `screenshots/ch10-ide-config.png` |
| 11 | README and Requirements | Project documentation and `requirements.txt` | `screenshots/ch11-readme-requirements.png` |

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| colorama | 0.4.6 | Colored terminal output in chapter 9 |

The full list is stored in `requirements.txt`. To regenerate it after installing new packages:

```powershell
python -m pip freeze | Set-Content -Encoding ascii requirements.txt
```

## Commit Convention

This repository follows [Conventional Commits](https://www.conventionalcommits.org/):

```text
type(scope): short subject

- detail of the change
- another detail

Refs: chapter-XX
```

Types used in this project:

| Type | Usage |
|------|-------|
| `feat` | New chapter or example added to `main.py` |
| `build` | Dependency and package management changes |
| `chore` | Tooling and configuration (`.gitignore`, IDE settings) |
| `docs` | Documentation such as `README.md` |

Each chapter has its own commit, containing both the code and its execution screenshot.

## Author

GitHub: [@bainalhkim](https://github.com/bainalhkim)
