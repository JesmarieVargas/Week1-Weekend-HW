# Python List Transformation

# Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print("sorting in ascending (123) order")
grades.sort()
print(grades)

# Sort in descending order
grades.reverse()
print(grades)

# Task 2

# Calculate the average grade

print("Length of grades list:", len(grades))

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
mean = sum(grades) / len(grades)
print(mean)

# Task 3

# Replace any grade below 80 with 'Failed'

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

for temp in grades:
    if temp < 80:
        grades[grades.index(temp)] = "Failed"
print(grades)
    

# Advanced List Methods and Identity Operators

# Task 1 

# Find out which students both submitted their assignments and attended class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

twain_lists = []

for i in submitted:
    if i in attended:
        twain_lists.append(i)
print(twain_lists)

# Task 2

# Check if the two lists are identical in terms of their content regardless of order 

print(submitted is attended)

# Task 3

# Remove any students from attended list who did not submit assignment.

attended.remove("Eve")
attended.remove("Frank")
print(attended)

# Advanced Slicing Techniques

# Task 1

# Extract temperatures for second week (7 days) of the month.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print("Weather for the second week of July:", temperatures [7:14])

# Task 2

# Extract all temperatures above 100.

print("Hottest days:", temperatures[24:])

# Task 3

# Reverse list and extract temperatures from the 5th to the 10th day of reversed list.

temperatures.reverse()
print(temperatures)

print("Days", temperatures[4:10])

# Deep Dive into Python Lists

#Task 1

# Filter students with grades below 80.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

new_list = zip(students, grades, activities)

for student, grade, activity in new_list:
    if grade < 80:
       print(student, grade, activity, sep=', ')

# Task 2

new_list = ("John", "Doe", "Smith")
students_approved = new_list

# Task 3

print("students_approved =", students_approved)