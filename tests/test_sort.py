import pytest

from backend.logic import count_ones, sort_numbers_by_bitcount


def test_count_ones_basic():
    assert count_ones(0) == 0
    assert count_ones(1) == 1
    assert count_ones(7) == 3


def test_sort_numbers_by_bitcount_basic_order():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert sort_numbers_by_bitcount(arr) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
