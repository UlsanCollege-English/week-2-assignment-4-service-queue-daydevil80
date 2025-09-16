"""Service Queue — Starter

Simulate a simple customer queue with pure functions.
Implement without mutating inputs.
"""
from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if not queue:
        return (None, [])
    next_name = queue[0]
    remaining = queue[1:]
    return (next_name, remaining)


def move_to_back(queue: List[str], name: str) -> List[str]:
    new_queue = queue[:]  # copy
    if name in new_queue:
        idx = new_queue.index(name)
        # remove and add to the back
        moved = new_queue.pop(idx)
        new_queue.append(moved)
    return new_queue


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    i, j = 0, 0
    # interleave until one list ends
    while i < len(q1) and j < len(q2):
        result.append(q1[i])
        result.append(q2[j])
        i += 1
        j += 1
    # add leftover
    result.extend(q1[i:])
    result.extend(q2[j:])
    return result
