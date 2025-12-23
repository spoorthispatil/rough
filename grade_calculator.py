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


def get_student_result(marks):
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    return avg, grade


if __name__ == "__main__":
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        marks.append(int(input(f"Enter marks for subject {i+1}: ")))

    avg, grade = get_student_result(marks)

    print("\n====== Student Result ======")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average Marks:", avg)
    print("Grade:", grade)
    print("============================")
