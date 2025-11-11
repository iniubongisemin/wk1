# class Dog:
#     def bark(self):
#         print("whoof whoof")

# dog_one = Dog()
# dog_one.bark()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Whoof Whoof")

dog_two = Dog("Freya", "German Shepherd")
dog_two.bark()
print(dog_two.name)

class Cat:
    pass
