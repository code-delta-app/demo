"""Ordinary code with no AI usage at all — the control. Agent Scan should rate
this NORMAL and not flag it, demonstrating that the scan doesn't fire on
everything (low false-positive on plain code)."""

def add(a, b):
    return a + b

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        return self._items.pop()
