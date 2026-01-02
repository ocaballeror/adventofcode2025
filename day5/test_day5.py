import pytest

from day5 import overlap_ranges


@pytest.mark.parametrize(
    "first, second, expect",
    [
        ((1, 3), (1, 3), [(1, 3)]),
        ((1, 3), (2, 3), [(1, 3)]),
        ((1, 3), (3, 3), [(1, 3)]),
        ((1, 3), (1, 4), [(1, 4)]),
        ((1, 3), (2, 4), [(1, 4)]),
        ((1, 3), (3, 4), [(1, 4)]),
        ((1, 3), (4, 4), [(1, 4)]),
        ((1, 3), (4, 5), [(1, 5)]),  # review
        ((1, 3), (5, 6), [(1, 3), (5, 6)]),
        ((1, 3), (0, 4), [(0, 4)]),
        ((1, 3), (0, 4), [(0, 4)]),
    ],
)
def test_overlap_ranges(first, second, expect):
    assert first[0] <= first[1]
    assert second[0] <= second[1]

    assert overlap_ranges([first, second]) == set(expect)
    assert overlap_ranges([second, first]) == set(expect)
