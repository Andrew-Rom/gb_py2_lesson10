class Animal:

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.spec = None

    def __init__(self, name, age, spec):
        self.name = name
        self.age = age
        self.spec = spec

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        # super().__init__(name, age)
        super().__init__(name, age, spec)
        self.spec = spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        # super().__init__(name, age)
        super().__init__(name, age, spec)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        # super().__init__(name, age)
        super().__init__(name, age, spec)
        self.spec = spec


class AnimalShop:
    @classmethod
    def create(cls, animal_type, name, age, spec):
        match animal_type.lower:
            case 'dog':
                animal = Dog(name, age, spec)
            case 'cat':
                animal = Cat(name, age, spec)
            case 'bird':
                animal = Bird(name, age, spec)
            case _:
                # animal = Animal(name, age)
                animal = Animal(name, age, spec)
        return animal

if __name__ == '__main__':
    pet1 = AnimalShop.create('dog', 'Bob', 5, 'гавкает')
    pet2 = AnimalShop.create('cat', 'Felix', 2, 'мурлычет')
    pet3 = AnimalShop.create('bird', 'Aro', 1, 'поет')
    pet4 = AnimalShop.create('fish', 'Pinky', 1, 'плавает')
    pet5 = AnimalShop.create('pig', 'Boss', 1, 'орет')

    for pet in [pet1, pet2, pet3, pet4, pet5]:
        print(pet.name, pet.get_spec())
