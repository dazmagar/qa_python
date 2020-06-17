# 1. Modify the method even_numbers() so that it only returns a list of even numbers (2, 4, 6, etc...)
# 2. Modify the method user_menu(choice) so that if choice is "q", it returns "Quit". Make sure that if is "a" it still returns "Add".

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 ==0:
            evens.append(number)
    return evens

# Modify the below method so that "Quit" is returned if the choice parameter is "q"
# Dont remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"

print(even_numbers())

choice = input("Enter your choice, should be 'a' or 'q': ")
print(user_menu(choice))
