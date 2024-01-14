"""definitions.py
An example showing different function definitions with example calls.
"""
import unittest

from definitions import meow, get_cat_meow, calculate_center


# Required to define a set of unit tests
class ExampleTests(unittest.TestCase):

    # All function definitions indented within the class are separate unit tests

    # Test for 'meow()' function
    def test_meow(self):
        self.assertEqual('Meow', meow())

    # Test for 'meow()' function in a separate format
    def test_meow_alternative_example(self):
        expected = 'Meow'
        actual = meow()
        self.assertEqual(expected, actual)

    # A test for 'get_cat_meow()'
    def test_get_cat_meow(self):
        self.assertEqual('Mochi: Meow', get_cat_meow('Mochi'))

    # Another test for 'get_cat_meow()'
    def test_get_cat_meow_alternative_example(self):
        expected = 'Pearl: Meow'
        actual = get_cat_meow('Pearl')
        self.assertEqual(expected, actual)

    # A test for 'calculate_center'
    def test_calculate_center(self):
        expected = calculate_center(0.0, 10.0)
        actual = 5.0
        self.assertAlmostEqual(expected, actual)  # Used due to floating point output

    # A failing test for 'calculate_center'
    def test_calculate_center_rounding(self):
        expected = calculate_center(0.00000001, 0.00000003)
        actual = 0.0
        self.assertAlmostEqual(expected, actual)  # Question: Why does this pass?

    # A failing test for 'calculate_center'
    def test_calculate_center_failure(self):
        expected = calculate_center(0.00000001, 0.00000003)
        actual = 0.0
        self.assertAlmostEqual(expected, actual, 8)


# A main guard
if __name__ == '__main__':
    unittest.main()
