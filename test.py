import unittest
import Lib


class MyTestCase(unittest.TestCase):
    def test_factor(self):
        factor_number = Lib.Factor(630)
        self.assertEqual(factor_number.return_factor_list(), [2, 3, 5, 7])
        self.assertEqual(Lib.IsPalindrome("race car").check(), True)


if __name__ == '__main__':
    unittest.main()
