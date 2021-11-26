import pytest
import bonus


@pytest.mark.parametrize(
    "salary, performance_review, level, error, result",
    [
        (60000, 0.5, 7, ValueError, 0),
        (70000, 1, 7, None, 0),
        (100000, 2, 7, None, 26250.0),
        (750000, 2.5, 7, None, 393750),
        (800000, 3, 7, ValueError, 0),
        (800000, 3.5, 11, ValueError, 0),
        (750000, 5, 11, None, 1650000.0),
        (100000, 6, 11, ValueError, 0),
        (70000, 6, 14, ValueError, 0),
        (60000, 5, 14, ValueError, 0),
        (60000, 3.5, 17, ValueError, 0),
        (70000, 3, 11, None, 77000.0),
        (100000, 2.5, 14, None, 57500.0),
        (750000, 0.5, 14, ValueError, 0),
        (800000, 1, 14, ValueError, 0),
        (800000, 2, 17, ValueError, 0),
        (750000, 2, 19, ValueError, 0),
        (100000, 1, 17, None, 0),
        (70000, 3.5, 19, ValueError, 0),
        (60000, 2.5, 11, ValueError, 0),
        (60000, 3, 19, ValueError, 0),
        (70000, 0.5, 17, ValueError, 0),
        (100000, 5, 19, ValueError, 0),
        (750000, 6, 17, ValueError, 0),
        (800000, 6, 19, ValueError, 0),
        (800000, 5, 7, ValueError, 0),
        (750000, 3, 17, None, 900000.0),
        (100000, 3.5, 7, None, 157500.0),
        (70000, 2.5, 17, None, 42000.0),
        (60000, 2, 14, ValueError, 0),
        (60000, 1, 11, ValueError, 0),
        (70000, 2, 11, None, 19250.0),
        (100000, 0.5, 11, ValueError, 0),
        (750000, 1, 19, ValueError, 0),
        (800000, 0.5, 19, ValueError, 0),
        (800000, 2.5, 19, ValueError, 0),
        (750000, 3.5, 14, None, 1293750.0),
        (100000, 3, 14, None, 115000.0),
        (70000, 5, 17, None, 168000.0),
        (60000, 6, 7, ValueError, 0)
    ],
)
def test_calculation_bonus(salary, performance_review, level, error, result):
    res = 0
    if error is not None:
        with pytest.raises(error):
            res = bonus.calculation_bonus(salary, performance_review, level),
    else:
        res = bonus.calculation_bonus(salary, performance_review, level)
    assert res == result
