import unittest
import calculator

class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.ADD(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calculator.Subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.Multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calculator.Divide(10, 5), 2.00)

    def test_divide_by_zero(self):
        self.assertEqual(calculator.Divide(10, 0), "error, cant divide by zero")



if __name__ == '__main__':
    unittest.main(verbosity=2)