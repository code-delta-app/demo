#!/usr/bin/env python3
"""Summarise a buildproj metrics log into a one-page text report."""
import sys
from collections import Counter


def parse(lines):
    counts = Counter()
    totals = Counter()
    for line in lines:
        if not line.startswith("metric "):
            continue
        name, _, value = line[7:].partition("=")
        counts[name] += 1
        try:
            totals[name] += int(value)
        except ValueError:
            pass
    return counts, totals


def main():
    counts, totals = parse(sys.stdin)
    width = max(len(n) for n in counts) if counts else 0
    for name in sorted(counts):
        avg = totals[name] / counts[name]
        print(f"{name:<{width}}  n={counts[name]:<6} total={totals[name]:<10} avg={avg:.1f}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
