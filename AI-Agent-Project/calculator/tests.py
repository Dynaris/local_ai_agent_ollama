import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_addition(self) -> None:
        result: float | None = self.calc.evaluate("3 + 4")
        self.assertEqual(result, 7)

    def test_subtraction(self) -> None:
        result: float | None = self.calc.evaluate("10 - 5")
        self.assertEqual(result, 5)

    def test_multiplication(self) -> None:
        result: float | None = self.calc.evaluate("2 * 3")
        self.assertEqual(result, 6)

    def test_division(self) -> None:
        result: float | None = self.calc.evaluate("8 / 4")
        self.assertAlmostEqual(result, 2.0)

    def test_precedence(self) -> None:
        result: float | None = self.calc.evaluate("3 + 7 * 2")
        self.assertEqual(result, 17)

if __name__ == "__main__":
    unittest.main()