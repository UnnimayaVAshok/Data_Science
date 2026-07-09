def student_grade(mark):

    if mark >= 90:

        grade = "A"

    elif mark >= 80 and mark < 90:

        grade = "B"

    elif mark >= 70 and mark < 80:

        grade = "C"

    else:

        grade = "D"

    print(grade)

student_grade(91) 