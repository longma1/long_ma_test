import unittest
from question_a import line_overlap

class TestOverlap(unittest.TestCase):
    def test_overlap_l1_greater(self):
        self.assertEqual(line_overlap((2, 6), (1, 5)), True)
        self.assertEqual(line_overlap((0, 5.1), (-1, 1)), True)


    def test_overlap_l2_greater(self):
        self.assertEqual(line_overlap((1, 5), (2, 6)), True)
        self.assertEqual(line_overlap((1.4, 5.1), (2, 6)), True)
        self.assertEqual(line_overlap((-3, 5), (0, 6)), True)
        self.assertEqual(line_overlap((0, 1), (-3, 3)), True)

    def test_overlap_l1_contained(self):
        self.assertEqual(line_overlap((1.4, 5.1), (2.2, 4.7)), True)
        self.assertEqual(line_overlap((2.3, 5.1), (2.3, 2.4)), True)

    def test_overlap_l2_contained(self):
        self.assertEqual(line_overlap((-0, 0), (0, 6)), True)

    def test_not_overlap(self):
        self.assertEqual(line_overlap((0, 1), (2, 6)), False)
        self.assertEqual(line_overlap((1.4, 5.1), (5.6, 6)), False)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            line_overlap(('wow', 'nice'), ('asd', 'www'))
            line_overlap((2, 3, 1), (2,3))
            line_overlap(('5.1', 2), (1, 0.6))
            line_overlap((None, None), (1, 2))
            line_overlap([0.1, 5.1], (0, 0.2))