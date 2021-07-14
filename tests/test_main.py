#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator
import pytest

def test_add_two_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950

def test_sub_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.sub(10,3)
    assert result == 7

def test_mul_two_numbers():
    numbers = range(1,10)
    calculator = SimpleCalculator()
    result = calculator.mul(*numbers)
    assert result == 362880

def test_div_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.div(6,3)
    assert result == 2

def test_div_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.div(6,0)
    assert result == float('inf')

def test_mul_by_zero_raises_execption():
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        calculator.mul(3,0)

def test_avg():
    calculator = SimpleCalculator()
    result = calculator.avg([2, 5, 14])
    assert result == 7

def test_avg_removes_upper_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([2, 5, 14, 98], ut=90)
    assert result == 7

def test_avg_removes_lower_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([2, 5, 12, 98], lt=10)
    assert result == pytest.approx(55)

def test_avg_includes_upper_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([2, 5, 12, 98], ut=98)
    assert result == 29.25

def test_avg_includes_lower_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([2, 5, 12, 98], lt=2)
    assert result == 29.25

def test_avg_empty_list():
    calculator = SimpleCalculator()
    result = calculator.avg([])
    assert result == 0

def test_avg_empty_list():
    calculator = SimpleCalculator()
    result = calculator.avg([], lt=90, ut=2)
    assert result == 0

def test_avg_empty_list_after_outliers_removed():
    calculator = SimpleCalculator()
    result = calculator.avg([12,99], lt=15, ut=90)
    assert result == 0

def test_avg_manages_zero_value_lower_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([-1,0,1], lt=0)
    assert result == 0.5

def test_avg_manages_zero_value_upper_outliers():
    calculator = SimpleCalculator()
    result = calculator.avg([-1,0,1], ut=0)
    assert result == -0.5
