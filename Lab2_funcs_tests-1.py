# Lab 2 Test Cases
# Name: Joanna Chou
# Section: 07
##############################################################
import unittest
import funcs

# 3 test cases for each function
class TestCases(unittest.TestCase):
    def test_do_math(self):
        self.assertAlmostEqual(funcs.do_math(4, 2), 0.380952380952)
        self.assertAlmostEqual(funcs.do_math(2, 3), -0.7727272727272726)
        self.assertAlmostEqual(funcs.do_math(3, 4), -1.076086956521739)

    def test_quadratic_formula1(self):
        self.assertAlmostEqual(funcs.quadratic_formula1(1, 6, 3), -0.5505102572168221)
        self.assertAlmostEqual(funcs.quadratic_formula1(2, 9, 2), -0.23443556292536272)
        self.assertAlmostEqual(funcs.quadratic_formula1(3, 11, 4), -0.4093327091137449)

    def test_quadratic_formula2(self):
        self.assertAlmostEqual(funcs.quadratic_formula2(1, 6, 3),-5.449489742783178)
        self.assertAlmostEqual(funcs.quadratic_formula2(2, 9, 2),-4.265564437074637)
        self.assertAlmostEqual(funcs.quadratic_formula2(3, 11, 4),-3.257333957552922)

    def test_distance(self):
        self.assertAlmostEqual(funcs.distance(2, 2, 1, 5), 4)
        self.assertAlmostEqual(funcs.distance(3, 5, 3, 10), 5)
        self.assertAlmostEqual(funcs.distance(0, 9, 21, 44), 56)

    def test_is_positive(self):
        self.assertTrue(funcs.is_positive(4))
        self.assertFalse(funcs.is_positive(-11))
        self.assertTrue(funcs.is_positive(0.222))

    def test_dividable_by_7(self):
        self.assertTrue(funcs.dividable_by_7(7))
        self.assertFalse(funcs.dividable_by_7(153))
        self.assertTrue(funcs.dividable_by_7(343))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
