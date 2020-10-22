import unittest
import fraction


class MyTestCase(unittest.TestCase):
    f1 = fraction.Fraction(1, 2)
    f2 = fraction.Fraction(3, 4)

    def get_f1(self):
        return self.f1

    def get_f2(self):
        return self.f2

    # Test the addition operator.
    def test_add(self):
        f3 = self.get_f1() + self.get_f2()
        f4 = fraction.Fraction(5, 4)
        self.assertEqual(f3, f4)

    # Test the radd operator.
    def test_radd(self):
        f3 = 4 + self.get_f1()
        f4 = fraction.Fraction(9, 2)
        self.assertEqual(f3, f4)

    # Test the get_num function.
    def test_get_num(self):
        self.assertEqual(self.get_f1().get_num(), 1)

    # Test the get_den function.
    def test_get_den(self):
        self.assertEqual(self.get_f1().get_den(), 2)

    # Test the iadd operator.
    def test_iadd(self):
        f3 = self.get_f1()
        f3 += self.get_f2()
        f4 = fraction.Fraction(5, 4)
        self.assertEqual(f3, f4)

    # Test the subtraction operator.
    def test_sub(self):
        f3 = self.get_f1() - self.get_f2()
        f4 = fraction.Fraction(-1, 4)
        self.assertEqual(f3, f4)

    # Test the subtraction operator.
    def test_divide(self):
        f3 = self.get_f1() / self.get_f2()
        f4 = fraction.Fraction(2, 3)
        self.assertEqual(f3, f4)

    # Test the subtraction operator.
    def test_mult(self):
        f3 = self.get_f1() * self.get_f2()
        f4 = fraction.Fraction(3, 8)
        self.assertEqual(f3, f4)

    # Test the >= operator.
    def test_ge(self):
        expression = self.get_f1() >= self.get_f2()
        self.assertFalse(expression)

    # Test the <= operator.
    def test_le(self):
        expression = self.get_f1() <= self.get_f2()
        self.assertTrue(expression)

    # Test the > operator.
    def test_gt(self):
        expression = self.get_f1() > self.get_f2()
        self.assertFalse(expression)

    # Test the < operator.
    def test_lt(self):
        expression = self.get_f1() < self.get_f2()
        self.assertTrue(expression)

    # Test the == operator.
    def test_eq(self):
        expression = self.get_f1() == self.get_f2()
        self.assertFalse(expression)

    # Test the != operator.
    def test_ne(self):
        expression = self.get_f1() != self.get_f2()
        self.assertTrue(expression)

    # Test the str operator.
    def test_str(self):
        self.assertEqual(str(self.f1), "1/2")

    # Test the repr operator.
    def test_repr(self):
        self.assertEqual(repr(self.f1), "1/2")


if __name__ == '__main__':
    unittest.main()
