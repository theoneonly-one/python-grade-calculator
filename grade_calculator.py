python_marks = int(input("Enter Python marks: "))
sql_marks = int(input("Enter SQL marks: "))
math_marks = int(input("Enter Mathematics marks: "))

total = python_marks + sql_marks + math_marks
average = total / 3

print("Total marks:", total)
print("Maximum possible marks: 300")
print("Average marks:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")