import typing as tp
import unittest

from compute_dna import compute_dna
from longest_password import longest_password
from longest_positive import Solution


class ExampleTasksTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.longest_password_test_cases: tp.Sequence[tp.Sequence[str, int]] = (
            ("test 5 a0A pass007     ?xy1", 7),
            ("1aa" * 100, -1),
            ("test 5 a0A pass007©©©©© ?xy1", 3),
        )
        self.longest_positive_test_cases: tp.Sequence[tp.Sequence[tp.List[int], int]] = (
            ([-1, 0, 1], 3),
            ([-1, 0, 1, 0], 4),
            ([-1, 0, 1, 0, 1], 5),
            ([1, 1, -1, -1, -1, -1, -1, 1, 1], 4),
            ([-1, -1, 1, -1, 1, 0, 1, -1, -1], 7),
        )

    def test_compute_dna(self) -> None:
        self.assertEqual(compute_dna("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_longest_password(self) -> None:
        for test_case in self.longest_password_test_cases:
            with self.subTest():
                self.assertEqual(longest_password(test_case[0]), test_case[1])

    def test_longest_positive(self) -> None:
        for test_case in self.longest_positive_test_cases:
            with self.subTest():
                self.assertEqual(Solution.longest_positive(test_case[0]), test_case[1])
