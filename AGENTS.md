# Agent Guidelines for haiku_cutup

## Project Overview

This is a simple Python CLI tool that displays random Haiku poems (575 format) using a database of 1st, 2nd, and 3rd lines from a CSV file. It supports random/sequential selection per line position and an optional "thinking frog" display (Cowsay-style).

## Repository Structure

```
haiku_cutup/
├── haiku_cutup.py       # Main CLI application
├── haiku_starter.csv    # Haiku line database
└── AGENTS.md           # This file
```

## Build, Lint, and Test Commands

### Running the CLI

```bash
# Basic usage (random haiku)
python haiku_cutup.py

# With thinking frog
python haiku_cutup.py --frog

# Generate multiple haikus
python haiku_cutup.py -n 3

# Sequential first line, random others
python haiku_cutup.py --no-random-first

# Fully sequential
python haiku_cutup.py --no-random-first --no-random-second --no-random-third
```

### Linting and Type Checking

This project uses standard Python tools. Install recommended tools:

```bash
# Install linting and type checking tools
pip install ruff mypy

# Run ruff linter
ruff check haiku_cutup.py

# Run ruff with auto-fix
ruff check --fix haiku_cutup.py

# Run mypy type checker
mypy haiku_cutup.py
```

### Testing

No formal test framework is currently set up. To run a single test manually:

```bash
# Create a test CSV and run Python inline tests
python -c "
import csv
import tempfile
import os

# Create test CSV
with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
    f.write('idx,first,second,third\n')
    f.write('0,test first,test second,test third\n')
    f.write('1,first two,second two,third two\n')
    temp_path = f.name

# Test the module
import haiku_cutup
first, second, third = haiku_cutup.load_haiku_database(temp_path)
assert 'test first' in first
assert 'test second' in second
assert 'test third' in third
os.unlink(temp_path)
print('All tests passed!')
"

# Run a single function test
python -c "
import haiku_cutup
result = haiku_cutup.wrap_text('hello world test string', width=10)
print('wrap_text result:', result)
"
```

## Code Style Guidelines

### Imports

- Use standard library imports first, then third-party
- Group imports: stdlib, third-party, local
- Use explicit imports (no `from x import *`)
- Sort imports alphabetically within groups

```python
# Correct
import argparse
import csv
import random
import sys
from pathlib import Path
```

### Formatting

- Use Black-compatible formatting (max line length: 88)
- Use 4 spaces for indentation (no tabs)
- Use double quotes for strings unless specifically avoiding escaping
- Add trailing commas in multi-line collections
- Use vertical whitespace between top-level definitions

### Type Hints

- Use type hints for all function parameters and return values
- Use built-in types (not typing module when possible)
- Use `tuple[...]` for fixed-length tuples, `list[...]` for lists

```python
# Good
def load_haiku_database(csv_path: str) -> tuple[list[str], list[str], list[str]]:
    ...

def draw_haiku(haiku_lines: list[str], use_frog: bool) -> None:
    ...
```

### Naming Conventions

- `snake_case` for functions, variables, and file names
- `PascalCase` for classes (if any)
- `UPPER_SNAKE_CASE` for constants
- Use descriptive names (minimum 2 words for non-obvious variables)
- Avoid single-letter variables except in loops or comprehensions

### Functions

- Keep functions small and focused (single responsibility)
- Use docstrings for all public functions
- Use type hints for all parameters and return values
- Prefer early returns over deeply nested conditionals

```python
def get_first_line(
    lines: list[str], random_select: bool, index: int
) -> tuple[str, int]:
    """Get a first line from the database.
    
    Args:
        lines: List of available first lines.
        random_select: If True, choose randomly; otherwise use sequential index.
        index: Current position for sequential selection.
    
    Returns:
        Tuple of (selected line, updated index).
    """
    if random_select:
        return random.choice(lines), index
    idx = index % len(lines)
    return lines[idx], index + 1
```

### Error Handling

- Use `sys.exit(1)` for fatal errors with user-friendly messages
- Print errors to stderr, not stdout
- Provide helpful error messages that explain what went wrong
- Handle file-not-found gracefully with informative messages

```python
# Good
if not csv_path.exists():
    print(f"Error: CSV file not found: {args.csv_path}", file=sys.stderr)
    sys.exit(1)
```

### CLI Design

- Use `argparse` for CLI argument parsing
- Support both `--flag` and `--no-flag` patterns for booleans
- Provide sensible defaults (random selection by default)
- Add helpful help text for all arguments
- Use `-h` / `--help` for help (built into argparse)

### General Best Practices

- Add shebang `#!/usr/bin/env python3` for executable scripts
- Use `if __name__ == "__main__":` guard for main entry point
- Keep lines under 100 characters when reasonable
- Use list comprehensions over explicit loops where appropriate
- Avoid unnecessary complexity - this is a simple CLI tool
