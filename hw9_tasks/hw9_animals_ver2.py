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


class AnimalShop(Dog, Cat, Bird, Animal):

    def __init__(self, animal_type, name, age, spec):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.spec = spec
        self.animal = None


    def create(self):
        match self.animal_type.lower:
            case 'dog':
                self.animal = Dog(self.name, self.age, self.spec)
            case 'cat':
                self.animal = Cat(self.name, self.age, self.spec)
            case 'bird':
                self.animal = Bird(self.name, self.age, self.spec)
            case _:
                self.animal = Animal(self.name, self.age)
        return self.animal


if __name__ == '__main__':
    pet1 = AnimalShop('Dog', 'Bob', 5, 'гавкает').create()
    pet2 = AnimalShop('Cat', 'Felix', 2, 'мурлычет').create()
    pet3 = AnimalShop('Bird', 'Aro', 1, 'поет').create()
    pet4 = AnimalShop('Fish', 'Pinky', 1, 'плавает').create()
    pet5 = AnimalShop('pig', 'Boss', 1, 'орет').create()

    for pet in [pet1, pet2, pet3, pet4, pet5]:
        print(pet.name, pet.get_spec())
