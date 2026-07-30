import pytest
from calculator import Calculator

calculator = Calculator()


@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (-6, -10, -16),
    (-6, 6, 0),
    (5.6, 6.3, 11.9),
    (4, 0, 4)
])
def test_sum_positive_nums(num1, num2, result):
    # Лучше использовать pytest.approx для float вместо '=='
    assert calculator.sum(num1, num2) == pytest.approx(result)

def test_sum_float_nums():
    res = calculator.sum(5.6, 6.3)
    # Идиоматичный способ сравнения float в pytest:
    assert res == pytest.approx(11.9)

def test_div_positive():
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    # Правильный синтаксис: с двоеточием и сдвигом тела блока
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


@pytest.mark.parametrize('nums, result', [
    ([], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 6.5)
])
def test_avg_list(nums, result):
    # 'nums' передается автоматически из декоратора
    res = calculator.avg(nums)

    # Сравниваем полученный результат с ожидаемым, используя approx для погрешности
    assert res == pytest.approx(result)
