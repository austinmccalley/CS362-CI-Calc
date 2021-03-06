"""
Tests for calculator application
"""

import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_sub(self):
        assert 3 == calculator.sub(5, 2)

    def test_mult(self):
        assert 10 == calculator.multiply(5, 2)

    def test_div(self):
        assert 3 == calculator.div(6, 2)
