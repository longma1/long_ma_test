import unittest
import random
from question_b import Solution, InvalidVersionStringError

class TestVersionCompare(unittest.TestCase):
    def test_valid_inputs_v1_greater(self):
        sol = Solution()
        self.assertEqual(sol.version_compare('1.1', '1.2'), '"1.2" is greater than "1.1"')
        self.assertEqual(sol.version_compare('2.1', '1.1'), '"2.1" is greater than "1.1"')
        self.assertEqual(sol.version_compare('2.2', '1.1'), '"2.2" is greater than "1.1"')
        self.assertEqual(sol.version_compare('2.0', '1.9999999999999999999999999'),
                         '"2.0" is greater than "1.9999999999999999999999999"')
        self.assertEqual(sol.version_compare('1.1.1.1.5', '1.1.1.1.4'), '"1.1.1.1.5" is greater than "1.1.1.1.4"')

    def test_valid_inputs_v2_greater(self):
        sol = Solution()
        self.assertEqual(sol.version_compare('1.1.123', '1.2.155'), '"1.2.155" is greater than "1.1.123"')
        self.assertEqual(sol.version_compare('1.1', '2.2'), '"2.2" is greater than "1.1"')
        self.assertEqual(sol.version_compare('1.1', '2.1'), '"2.1" is greater than "1.1"')

    def test_equal(self):
        sol = Solution()
        self.assertEqual(sol.version_compare('1.1', '1.1'), 'The two version strings are equal')
        for i in range(100):
            v1 = random.randint(0, 100)
            v2 = random.randint(0, 100)

            s = str(v1) + "." + str(v2)

            self.assertEqual(sol.version_compare(s, s), 'The two version strings are equal')

    def test_valid_random_inputs(self):
        sol = Solution()
        for i in range(20):
            i1 = random.randint(0, 100)
            i2 = random.randint(0, 100)
            i3 = random.randint(0, 100)
            i4 = random.randint(0, 100)

            s1 = str(i1) + "." + str(i3)
            s2 = str(i2) + "." + str(i4)

            if i1 > i2:
                self.assertEqual(sol.version_compare(s1, s2), '"{}" is greater than "{}"'.format(s1, s2))

            elif i2 > i1:

                self.assertEqual(sol.version_compare(s1, s2), '"{}" is greater than "{}"'.format(s2, s1))

            else:
                if i3 > i4:
                    self.assertEqual(sol.version_compare(s1, s2), '"{}" is greater than "{}"'.format(s1, s2))

                elif i3 < i4:
                    self.assertEqual(sol.version_compare(s1, s2), '"{}" is greater than "{}"'.format(s2, s1))

                else:
                    self.assertEqual(sol.sol.version_compare(s1, s2), 'The two version strings are equal')

    def test_invalid(self):
        sol = Solution()
        with self.assertRaises(InvalidVersionStringError):
            sol.version_compare('1.1.1', '1.2')
            sol.version_compare('version : 1.1', 'version : 1.2')
            sol.version_compare('1.1', '1.')
            sol.version_compare('1,1', '1.2')
            sol.version_compare('1.1', '1;2')
