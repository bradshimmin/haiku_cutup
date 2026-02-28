# Haiku Cutup

A simple Python CLI tool that displays random Haiku poems (575 format) using a database of 1st, 2nd, and 3rd lines from a CSV file. It supports random/sequential selection per line position and an optional "thinking frog" display (Cowsay-style).

## Quick Start

```bash
# Install dependencies (if needed)
pip install -r requirements.txt

# Run the CLI
python haiku_cutup.py
```

## Features

- **Random Haiku Generation**: Creates poems by randomly combining first, second, and third lines
- **Thinking Frog Display**: Optional ASCII art frog that "thinks" about the haiku
- **Flexible Selection**: Choose between random or sequential line selection
- **Multiple Output**: Generate multiple haikus at once

## Usage

### Basic Usage

```bash
python haiku_cutup.py
```

### With Thinking Frog

```bash
python haiku_cutup.py --frog
```

### Generate Multiple Haikus

```bash
python haiku_cutup.py -n 3
```

### Sequential Line Selection

```bash
# Sequential first line, random others
python haiku_cutup.py --no-random-first

# Fully sequential
python haiku_cutup.py --no-random-first --no-random-second --no-random-third
```

### Help

```bash
python haiku_cutup.py -h
```

## Installation

No installation required! The tool runs directly from the source files:

```bash
# Clone the repository
git clone https://github.com/yourusername/haiku_cutup.git
cd haiku_cutup

# Run the tool
python haiku_cutup.py
```

## File Structure

```
haiku_cutup/
├── haiku_cutup.py       # Main CLI application
├── haiku_starter.csv    # Haiku line database
├── README.md           # This file
└── AGENTS.md           # Development guidelines
```

## Data Source

The haiku line database (`haiku_starter.csv`) is derived from the following dataset:

- **Source**: [Haiku Dataset on Kaggle](https://www.kaggle.com/datasets/hjhalani30/haiku-dataset)
- **Author**: hjhalani30

## Development

### Running Tests

No formal test framework is currently set up. To run manual tests:

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
```

### Linting and Type Checking

```bash
# Install linting tools
pip install ruff mypy

# Run ruff linter
ruff check haiku_cutup.py

# Run ruff with auto-fix
ruff check --fix haiku_cutup.py

# Run mypy type checker
mypy haiku_cutup.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

MIT License - see LICENSE file for details.