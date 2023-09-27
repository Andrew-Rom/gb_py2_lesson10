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

    def __init__(self, animal, name, age, spec):
        self.name = name
        self.age = age
        self.spec = spec
        match animal.lower:
            case 'dog':
                self.animal = Dog(self.name, self.age, self.spec)
            case 'cat':
                self.animal = Cat(self.name, self.age, self.spec)
            case 'bird':
                self.animal = Bird(self.name, self.age, self.spec)
            case _:
                self.animal = Animal(self.name, self.age)


if __name__ == '__main__':
    pet1 = CreateAnimal('Dog', 'Bob', 5, 'гавкает')
    pet2 = CreateAnimal('Cat', 'Felix', 2, 'мурлычет')
    pet3 = CreateAnimal('Bird', 'Aro', 1, 'поет')
    pet4 = CreateAnimal('Fish', 'Pinky', 1, 'плавает')
    pet5 = CreateAnimal('pig', 'Boss', 1, 'орет')

    for pet in [pet1, pet2, pet3, pet4, pet5]:
        print(pet.name, pet.get_spec())
