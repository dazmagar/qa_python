my_set = {1, 3, 5}
my_dict = { 'name': 'Jose', 'age': 90, 'grades': [13, 45, 66, 90] }
another_dict = { 1:15, 2:75, 3:150}

lottery_players = [
    {
        'name': 'Rolf',
        'numbers': (13, 45, 66, 23, 22)
    },
    {
        'name': 'John',
        'numbers': (14, 56, 80, 23, 22)
    }
]

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    },
]

## 

# lottery_players[0].total() # AttributeError: 'dict' object has no attribute 'total'
# lottery_players.total() # AttributeError: 'list' object has no attribute 'total'


# new dict
statuses = {}
# list of functions
functions = ['Legal', 'Finance']
# some boolean variables
ca = True
cb = False
# add keys and values (as list) in dict
statuses[functions[0]] = statuses.get(functions[0],[]) + [ca,cb]
statuses[functions[1]] = statuses.get(functions[1],[]) + [ca,ca]
print(statuses)
# print dict
#{'Legal': [True, False], 'Finance': [True, True]}

# compare values from dict with list of expected results (iteration by key dict)
# Сравниваем список из словаря (для каждого ключа) со списком ожидаемых значений
# ключ словаря - Legal
# вывод: "Для функции Legal: ожидаемые значения [True, True], фактические [True, False]"
# ключ словаря - Finance
# вывод: "Для функции Finance: ожидаемые значения [True, True], фактические [True, True]"

# list of expected results
expect = [True, True]

for key, values in statuses.items():
    if values == expect:
        print("For function: {0} got: {1} expected: {2}".format(key,values,expect))
    else:
        print("For function: {0} got: {1} expected: {2}".format(key,values,expect))
