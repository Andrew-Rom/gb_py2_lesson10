class Triangle:

    def __init__(self, side_ab: int | float, side_bc: int | float = None, side_ac: int | float = None):
        self.side_ab = side_ab
        self.side_bc = side_bc if side_bc else side_ab
        self.side_ac = side_ac if side_ac else side_ab
        self.check_triangle(self.side_ab, self.side_bc, self.side_ac)

    def check_triangle(self, a, b, c):
        """Verifying the existence of a triangle"""
        if a > b + c or b > a + c or c > a + b:
            raise ValueError(f'A triangle with sides {a}, {b}, {c} does not exist')

    def type_triangle(self):
        """Returns type of a triangle"""
        if self.side_ab == self.side_bc == self.side_ac:
            return 'equilateral'
        elif self.side_ab == self.side_bc or self.side_ab == self.side_ac or self.side_bc == self.side_ac:
            return 'isosceles'
        else:
            return 'ordinary'


if __name__ == '__main__':
    triangle1 = Triangle(5)
    triangle2 = Triangle(3, 4, 3)
    triangle3 = Triangle(1, 2, 3)
    triangle4 = Triangle(1, 2)

    print(triangle1.type_triangle())
    print(triangle2.type_triangle())
    print(triangle3.type_triangle())
    print(triangle4.type_triangle())
