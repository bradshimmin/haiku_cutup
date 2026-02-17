#!/usr/bin/env python3
import argparse
import csv
import random
import sys
from pathlib import Path


def load_haiku_database(csv_path: str) -> tuple[list[str], list[str], list[str]]:
    """Load haiku lines from CSV, returning separate lists for 5-7-5 positions."""
    first_lines = []
    second_lines = []
    third_lines = []

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if len(row) >= 5:
                first = row[1].strip()
                second = row[2].strip()
                third = row[3].strip()
                if first:
                    first_lines.append(first)
                if second:
                    second_lines.append(second)
                if third:
                    third_lines.append(third)

    return first_lines, second_lines, third_lines


def get_first_line(
    lines: list[str], random_select: bool, index: int
) -> tuple[str, int]:
    if random_select:
        return random.choice(lines), index
    idx = index % len(lines)
    return lines[idx], index + 1


def get_second_line(
    lines: list[str], random_select: bool, index: int
) -> tuple[str, int]:
    if random_select:
        return random.choice(lines), index
    idx = index % len(lines)
    return lines[idx], index + 1


def get_third_line(
    lines: list[str], random_select: bool, index: int
) -> tuple[str, int]:
    if random_select:
        return random.choice(lines), index
    idx = index % len(lines)
    return lines[idx], index + 1


def wrap_text(text: str, width: int = 40) -> list[str]:
    """Simple word wrapping for the frog bubble."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = " ".join(current + [word])
        if len(test) <= width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines or [""]


def draw_frog(haiku_lines: list[str]) -> None:
    """Draw a thinking frog (Cowsay-style) with the haiku."""
    bubble_lines = [wrap_text(line, 36) for line in haiku_lines]
    bubble_flat = [word for line in bubble_lines for word in line]

    max_len = max(len(line) for line in bubble_flat)

    print("       _       ")
    print("      (o<      Thinking...")
    print("      (_)     ")
    print()

    border = "+" + "-" * (max_len + 2) + "+"
    print(border)
    for line in haiku_lines:
        wrapped = wrap_text(line, 36)
        for w in wrapped:
            print(f"| {w:<{max_len}} |")
    print(border)
    print()


def draw_haiku(haiku_lines: list[str], use_frog: bool) -> None:
    """Display the haiku, optionally with the thinking frog."""
    if use_frog:
        draw_frog(haiku_lines)
    else:
        for line in haiku_lines:
            print(line)


def main():
    parser = argparse.ArgumentParser(
        description="Display a random or sequential Haiku (5-7-5 format)", prog="haiku"
    )

    parser.add_argument(
        "--csv-path",
        default="./haiku_starter.csv",
        help="Path to haiku CSV file (default: ./haiku_starter.csv)",
    )

    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of haikus to generate (default: 1)",
    )

    parser.add_argument(
        "--random-first", action="store_true", default=True, dest="random_first"
    )
    parser.add_argument(
        "--no-random-first",
        action="store_false",
        dest="random_first",
        help="Use sequential selection for first line",
    )

    parser.add_argument(
        "--random-second", action="store_true", default=True, dest="random_second"
    )
    parser.add_argument(
        "--no-random-second",
        action="store_false",
        dest="random_second",
        help="Use sequential selection for second line",
    )

    parser.add_argument(
        "--random-third", action="store_true", default=True, dest="random_third"
    )
    parser.add_argument(
        "--no-random-third",
        action="store_false",
        dest="random_third",
        help="Use sequential selection for third line",
    )

    parser.add_argument(
        "--frog",
        action="store_true",
        default=False,
        dest="use_frog",
        help="Display with thinking frog (Cowsay-style)",
    )
    parser.add_argument(
        "--no-frog",
        action="store_false",
        dest="use_frog",
        help="Display without frog (default)",
    )

    args = parser.parse_args()

    csv_path = Path(args.csv_path)
    if not csv_path.exists():
        csv_path = Path(__file__).parent / args.csv_path

    if not csv_path.exists():
        print(f"Error: CSV file not found: {args.csv_path}", file=sys.stderr)
        sys.exit(1)

    first_lines, second_lines, third_lines = load_haiku_database(str(csv_path))

    if not first_lines or not second_lines or not third_lines:
        print("Error: No haiku lines found in CSV", file=sys.stderr)
        sys.exit(1)

    first_idx = 0
    second_idx = 0
    third_idx = 0

    for i in range(args.number):
        if i > 0:
            print()

        first_line, first_idx = get_first_line(
            first_lines, args.random_first, first_idx
        )
        second_line, second_idx = get_second_line(
            second_lines, args.random_second, second_idx
        )
        third_line, third_idx = get_third_line(
            third_lines, args.random_third, third_idx
        )

        draw_haiku([first_line, second_line, third_line], args.use_frog)


if __name__ == "__main__":
    main()
