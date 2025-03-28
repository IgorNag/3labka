import pytest
from geometry import calculate_area

def test_calculate_area():
    assert calculate_area(5, 3) == 15
    assert calculate_area(7, 2) == 14

    try:
        calculate_area(-1, 5)
    except ValueError:
        pass
    else:
        assert False, "Ожидалась ошибка ValueError"

    try:
        calculate_area(3, -4)
    except ValueError:
        pass
    else:
        assert False, "Ожидалась ошибка ValueError"