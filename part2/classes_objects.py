# lottery_player_dict = [
# {
#     'name': 'Rolf',
#     'numbers': (13, 45, 66, 23, 22)
# },
# {
#     'name': 'John',
#     'numbers': (14, 56, 80, 23, 22)
# }
# ]

# class LotteryPlayer:
#     def __init__(self, name):
#         self.name = name,
#         self.numbers = (5, 9, 12, 3, 1, 21)

#     def total(self):
#         return sum(self.numbers)

# player_one = LotteryPlayer("Rolf")
# player_one.numbers = (1, 2, 3, 6, 7, 8)
# player_two = LotteryPlayer("John")

# print("Compare classes: ", player_one == player_two)
# print("Compare player_one name {0} and player_two name {1}: ".format(player_one.name, player_two.name), player_one.name == player_two.name)
# print("Compare player_one numbers {0} and player_two numbers {1}: ".format(player_one.numbers, player_two.numbers), player_one.numbers == player_two.numbers)
# print("Compare player_one total num {0} and player_two total num {1}".format(player_one.total(), player_two.total()), player_one.total() == player_two.total())

## 

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}".format(self.school))

    @staticmethod
    def go_to_school_static():
        print("I'm going to school")

    @classmethod
    def go_to_school_cls(cls):
        print("I'm going to school")
        print("I'm a {}".format(cls))


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)

print(anna.marks)
print(anna.average())

anna.go_to_school()
Student.go_to_school_static()
Student.go_to_school_cls()
