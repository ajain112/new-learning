import  unittest
from calc import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        self.assertEqual(divide(-6, -3), 2)
    def test_divide_negative(self):
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(6, -3), -2) 
    def test_divide_float(self):
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
    def test_divide_large_numbers(self):
        self.assertEqual(divide(1000000, 1000), 1000)
        self.assertEqual(divide(1000000, 1), 1000000)
    def test_divide_small_numbers(self):
        self.assertAlmostEqual(divide(0.0001, 0.0001), 1.0)
        self.assertAlmostEqual(divide(0.0001, 0.001), 0.1)
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
        self.assertEqual(divide(0, 1), 0)
    def test_divide_negative_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(-1, 0)
        self.assertEqual(divide(0, -1), 0)
    def test_divide_by_negative(self):
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
    def test_divide_by_large_negative(self):
        self.assertEqual(divide(1000000, -1000), -1000)
        self.assertEqual(divide(-1000000, -1000), 1000)
    def test_divide_by_small_negative(self):
        self.assertAlmostEqual(divide(0.0001, -0.0001), -1.0)
        self.assertAlmostEqual(divide(-0.0001, -0.001), 0.1)
    def test_divide_by_float(self):
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide(1.0, 0.1), 10.0)
    def test_divide_by_zero_float(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            divide(1.0, 0.0)
    def test_divide_by_negative_float(self):
        self.assertAlmostEqual(divide(10.0, -2.0), -5.0)
        self.assertAlmostEqual(divide(-10.0, -2.0), 5.0)
        self.assertAlmostEqual(divide(10.0, -0.1), -100.0)
        self.assertAlmostEqual(divide(-10.0, -0.1), 100.0)
        self.assertAlmostEqual(divide(0.1, -0.1), -1.0)
        self.assertAlmostEqual(divide(-0.1, -0.1), 1.0)
        self.assertAlmostEqual(divide(0.1, 0.1), 1.0)
        self.assertAlmostEqual(divide(-0.1, 0.1), -1.0)
        with self.assertRaises(ZeroDivisionError):
            divide(0.1, 0.0)
        self.assertAlmostEqual(divide(0.0, 0.1), 0.0)
        self.assertAlmostEqual(divide(0.0, -0.1), 0.0)

if __name__ == '__main__':
    unittest.main()