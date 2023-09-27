class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class CreateAnimal(Dog, Cat, Bird, Animal):

    def __init__(self, animal_type, animal_name, animal_age, animal_spec):
        self.animal = animal_type
        self.name = animal_name
        self.age = animal_age
        self.spec = animal_spec
        self.create_animal (self.animal, self.name, self.age, self.spec)

    def create_animal(self, animal, name, age, spec):
        animals = [Dog, Cat, Bird]
        if animal in animals:
            return animal(name, age, spec)
        else:
            return Animal(name, age)


pet1 = CreateAnimal(Dog, 'Bob', 5, 'гавкает')
pet2 = CreateAnimal(Cat, 'Felix', 2, 'мурлычет')
pet3 = CreateAnimal(Bird, 'Aro', 1, 'поет')
# pet4 = CreateAnimal(Fish, 'Pinky', 1, 'плавает')

for pet in [pet1, pet2, pet3]:
     print(pet.name, pet.get_spec())
