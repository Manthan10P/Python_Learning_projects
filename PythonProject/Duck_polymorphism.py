class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())  # This will call the speak() method of the object

# Create objects of different types
dog = Dog()
cat = Cat()

animal_speak(dog)   # Woof!
animal_speak(cat)   # Meow!
