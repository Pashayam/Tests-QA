from allpairspy import AllPairs


def get_level_coefficient(level: int):
    if level < 10:
        coefficient = 1.05
    elif 10 <= level < 13:
        coefficient = 1.1
    elif 13 <= level < 15:
        coefficient = 1.15
    else:
        coefficient = 1.2
    return coefficient


def get_performance_coefficient(performance_review):
    if performance_review < 2:
        coefficient = 0
    elif 2 <= performance_review < 2.5:
        coefficient = 0.25
    elif 2.5 <= performance_review < 3:
        coefficient = 0.5
    elif 3 <= performance_review < 3.5:
        coefficient = 1
    elif 3.5 <= performance_review < 4:
        coefficient = 1.5
    else:
        coefficient = 2
    return coefficient


def calculation_bonus(salary: int, performance_review, level: int):
    if not salary or not performance_review or not level:
        raise ValueError("Нет одного или нескольких параметорв")
    if type(salary) != int or type(level) != int:
        raise ValueError("Некорректное значение")
    if salary < 70000 or salary > 750000:
        raise ValueError("Неверна зарплата")
    if performance_review < 1 or performance_review > 5:
        raise ValueError("Неверный Performance Review")
    if level < 7 or level > 17:
        raise ValueError("Неверный уровень инженера")
    return round(salary * get_performance_coefficient(performance_review) * get_level_coefficient(level), 2)


if __name__ == "__main__":
    print(calculation_bonus(750000, 2.5, 7))
    parameters = [
        [60000, 70000, 100000, 750000, 800000],
        [0.5, 1, 2, 2.5, 3, 3.5, 5, 6],
        [7, 11, 14, 17, 19],
    ]
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{}".format(tuple(pairs)))
