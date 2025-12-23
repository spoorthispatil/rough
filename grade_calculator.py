import sys


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def assign_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":

    script_name = sys.argv[0]

    if len(sys.argv) > 1:
        marks = list(map(float, sys.argv[1:]))
        print("User provided marks:")
    else:
        marks = [50, 60, 70, 80, 90]
        print("No input given - using default marks:")

    total = sum(marks)
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("Script Name:", script_name)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Maximum Marks:", max(marks))
    print("Minimum Marks:", min(marks))
    print("Grade:", grade)
