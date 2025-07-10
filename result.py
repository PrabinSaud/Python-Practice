# Garden City University Result

print("GARDEN CITY UNIVERSITY  FINAL EXAMINATION RESULT")
print("Bachalur of Computer Application")
Reg_no = input ("Enter the Student Registaration No. : ")
name = input("Enter the Student Name : ")
semester = input ("Enter the Student Semester : ")

print("\n Enter the marks of subject out of 100 : ")

# Marks obtaion in each subject
subject1 = int(input("Enter marks for Python(T): "))
practical1 = int(input("Enter marks of Python(P) : "))

subject2 = int(input("Enter marks for Data Communication(T) : "))
practical2 = int(input("Enter marks of Data Comminication(P) : "))

subject3 = int(input("Enter marks for Software Engineerig(T): "))
practical3 = int(input("Enter marks of Software Engineering(P) : "))

subject4 = int(input("Enter marks for Java(T): "))
practical4 = int(input("Enter marks of Java(P) : "))

forgein = int(input("Enter marks of Forgein Language(Spainsh) : "))
mil = int(input("Enter marks of MIL(English) : "))
nss = int(input("Enter marks of NSS : "))

# Calculate total Marks
total_marks = subject1+practical1+subject2+practical2+subject3+practical3+subject4+practical4+forgein+mil+nss
percentage = (total_marks / 700) * 100

# Determine grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Display result
print("\n" + "="*50)
print("GARDEN CITY UNIVERSITY EXAMINATION RESULT")
print("Bachalur of Computer Application")
print("="*50)
print(f"Student Name: {Reg_no}")
print(f"Student Name: {name}")
print(f"Semester: {semester}")
print("-"*50)
print("Subject-wise Marks:")
print(f"Python(T): {subject1}")
print(f"Python(P): {practical1}")
print(f"Data Comminication(T): {subject2}")
print(f"Data Comminication(P): {practical2}")
print(f"Software Engineering(T): {subject3}")
print(f"Software Engineering(P): {practical3}")
print(f"Java(T): {subject4}")
print(f"Java(P): {practical4}")
print(f"Forgein Language(Spanish): {forgein}")
print(f"MIL(English): {mil}")
print(f"NSS: {nss}")

print("-"*50)
print("Total Marks ut of 700")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print(f"Grade: {calculate_grade(percentage)}")
print("="*50)





