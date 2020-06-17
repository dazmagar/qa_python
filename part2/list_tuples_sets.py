my_variable = "hello"
grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable
set_grades = {77, 80, 90} # unique & unordered

grades.append(100)
print(grades)
print(grades[0])
grades[0] = 60
print(grades)

tuple_grades = tuple_grades + (100,)
print(tuple_grades)
print(tuple_grades[3])
print(tuple_grades)

# set_grades[0] = 60 # TypeError: 'set' object does not support item assignment
set_grades.add(60)
set_grades.add(60)
print(set_grades)

## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
wining_numbers = {11, 9, 7, 5, 3, 1}

print(your_lottery_numbers.intersection(wining_numbers))
print(your_lottery_numbers.union(wining_numbers))
print({1, 2, 3, 4}.difference({1, 2}))
