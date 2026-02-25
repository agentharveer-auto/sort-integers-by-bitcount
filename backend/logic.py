from typing import List


def count_ones(n: int) -> int:
    """Count the number of 1 bits in the binary representation of n.

    Uses int.bit_count() when available (Python 3.8+), otherwise falls back to bin(n).
    Assumes non-negative integers as per problem constraints.
    """
    if n < 0:
        # For non-negative inputs only; mirror typical LeetCode constraints.
        n = abs(n)
    if hasattr(int, "bit_count"):
        return n.bit_count()
    return bin(n).count("1")


def sort_numbers_by_bitcount(arr: List[int]) -> List[int]:
    """Return a new list sorted by the number of 1s in binary representation, then by value.

    Sorting key: (count_ones(x), x)
    """
    return sorted(arr, key=lambda x: (count_ones(x), x))
