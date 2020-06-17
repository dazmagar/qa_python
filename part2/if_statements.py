# should_continue = True
# if should_continue:
#     print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You dont know {}!".format(person))

## Exercise

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",") # ["John", "Rolf", "Anna", "Greg"]

    people_without_spaces = [person.strip() for person in people_list]
    # for person in people_list:
    #     people_without_spaces.append(person.strip())
    return people_without_spaces

# print(people_without_spaces)

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {0}!".format(person))
    else:
        print("You dont know {}!".format(person))

ask_user()
