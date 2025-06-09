# Input marks for 8 labs one by one
lab1 = float(input("Enter marks for lab 1: "))
lab2 = float(input("Enter marks for lab 2: "))
lab3 = float(input("Enter marks for lab 3: "))
lab4 = float(input("Enter marks for lab 4: "))
lab5 = float(input("Enter marks for lab 5: "))
lab6 = float(input("Enter marks for lab 6: "))
lab7 = float(input("Enter marks for lab 7: "))
lab8 = float(input("Enter marks for lab 8: "))

# Calculate average lab marks
average_lab = (lab1 + lab2 + lab3 + lab4 + lab5 + lab6 + lab7 + lab8) / 8

# Input midsemester and endsemester marks
midsemester = float(input("Enter midsemester marks: "))
endsemester = float(input("Enter endsemester marks: "))

# Calculate final grade
final_grade = (average_lab * 0.50) + (midsemester * 0.20) + (endsemester * 0.30)

# Determine letter grade
if final_grade >= 90:
    grade = "A"
elif final_grade >= 80:
    grade = "B"
elif final_grade >= 70:
    grade = "C"
elif final_grade >= 60:
    grade = "D"
elif final_grade >= 50:
    grade = "E"
else:
    grade = "Invalid"

print("Final grade for IST1025 is:", round(final_grade, 2))
print("Letter grade is:", grade)


