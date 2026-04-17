def student_marks():
    marks_dict = {}
    while True:
        student_name = input("enter student name or type 'done' to finish ")
        if student_name == "done":
            return marks_dict
        marks = input(f"enter marks for {student_name}:")
        try:
            marks_dict[student_name] = float(marks)
        except ValueError:
            print("Invalid input. Enter marks as a number")

print(student_marks())
