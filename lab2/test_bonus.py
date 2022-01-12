import pytest
import bonus
from allpairspy import AllPairs

salaries = list(range(68000, 751001, 1000))
levels = list(range(6, 19))
perf_results = list(round(x * 1.0, 1) for x in range(1, 5))
parameters = [salaries, levels, perf_results]

for parameter in parameters:
    parameter.extend(["text", None])

pair_for_test = [pair for pair in AllPairs(parameters)]


@pytest.mark.parametrize(
    "salary, expected_error",
    [
        (50000, ValueError),
        (80000.5, TypeError),
        (800000, ValueError),
        ("text", TypeError),
        (None, TypeError)
    ]
)
def test_chek_salary_error(salary, expected_error):
    with pytest.raises(expected_error):
        bonus.chek_salary(salary)


@pytest.mark.parametrize(
    "salary, expected_result",
    [
        (75000, None),
        (500000, None),
        (750000, None),
    ]
)
def test_chek_salary(salary, expected_result):
    assert bonus.chek_salary(salary) == expected_result


@pytest.mark.parametrize(
    "performance_review, expected_result",
    [
        (1, 0),
        (2, 0.25),
        (2.5, 0.5),
        (3, 1),
        (3.5, 1.5),
        (5, 2),
    ]
)
def test_get_performance_coefficient(performance_review, expected_result):
    assert bonus.get_performance_coefficient(performance_review) == expected_result


@pytest.mark.parametrize(
    "performance_review, expected_error",
    [
        (0, ValueError),
        (6, ValueError),
        ("text", TypeError),
        (None, TypeError)
    ]
)
def test_get_performance_coefficient_error(performance_review, expected_error):
    with pytest.raises(expected_error):
        bonus.get_performance_coefficient(performance_review)


@pytest.mark.parametrize(
    "level, expected_result",
    [
        (7, 1.05),
        (10, 1.1),
        (13, 1.15),
        (17, 1.2)
    ]
)
def test_get_level_coefficient(level, expected_result):
    assert bonus.get_level_coefficient(level) == expected_result


@pytest.mark.parametrize(
    "level, expected_error",
    [
        (6, ValueError),
        (18, ValueError),
        ("text", TypeError),
        (None, TypeError)
    ]
)
def test_get_level_coefficient(level, expected_error):
    with pytest.raises(expected_error):
        bonus.get_level_coefficient(level)


@pytest.mark.parametrize(
    "salary, performance_review, level",
    pair_for_test,
)
def test_calculation_bonus(salary, performance_review, level):
    errors = (ValueError, TypeError)
    try:
        with pytest.raises(errors):
            bonus.calculation_bonus(salary, performance_review, level)
    except:
        assert bonus.calculation_bonus(salary, performance_review, level) not in errors