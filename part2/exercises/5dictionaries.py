# Create a variable called student, with a dictionary
# The dictionary must contain three keys: 'name', 'school', and 'grades'
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.

student = {'name': 'Jose', 'school': 'Computing', 'grades': (97, 98, 99)}
students = [
    {
        'name': 'Rolf',
        'school': 'Math',
        'grades': (95, 96, 97, 98, 99)
    },
    {
        'name': 'John',
        'school': 'History',
        'grades': (95, 96, 97, 98, 99)
    }
]

# Assume the arguments, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades'] # Changer this!
    return sum(grades) / len(grades)

print(average_grade(student))

# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all grades of all students together
# You must also count how many grades there are in total in the entrire list
def average_grade_all_students(students_list):
    total = 0
    count = 0
    for student in students_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

print(average_grade_all_students(students))
