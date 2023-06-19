# import random
# import time
#
# studentai = ["Rugile", "Egidijus", "Deividas", "Tomas", "Migle", "SauliusS", "SauliusA", "Ausrine", "Mantas", "Vaidas",
#              "Jurate", "Modestas"]
# random_student = random.choice(studentai)
# time.sleep(3)
# print("Atsitiktinai pasirinktas studentas: ", random_student)


"""--------------------------------------------------------------------------"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #gauna varda
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print("Amius negali buti neigiamas")

person = Person("Jonas", 50)

print("name", person.get_name())
print("age", person.get_age())

person.set_name("Petras")
person.set_age(-10)

print("new_name", person.get_name())
print("new_age", person.get_age())

"""-----------------------------------------------------------------------------------"""