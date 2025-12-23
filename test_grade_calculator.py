from grade_calculator import calculate_average, assign_grade


def test_average_high_scores():
    marks = [90, 95, 85]
    assert calculate_average(marks) == 90


def test_average_medium_scores():
    marks = [70, 75, 65]
    assert calculate_average(marks) == 70


def test_average_low_scores():
    marks = [40, 45, 35]
    assert calculate_average(marks) == 40


def test_grade_S():
    assert assign_grade(95) == "S"


def test_grade_A():
    assert assign_grade(85) == "A"


def test_grade_B():
    assert assign_grade(70) == "B"


def test_grade_C():
    assert assign_grade(55) == "C"


def test_grade_D():
    assert assign_grade(45) == "D"


def test_grade_F():
    assert assign_grade(30) == "F"
