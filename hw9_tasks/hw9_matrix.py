class Matrix():
    def __init__(self, data):
        self.data = data
        self.is_matrix(self.data)

    def is_matrix(self, value):
        if type(value) is list:
            for i in range(len(value)):
                if type(value) is not list:
                    raise ValueError('This is not a matrix.')
            else:
                if not all(len(value[i]) == len(value[i + 1]) for i in range(len(value) - 1)):
                    raise ValueError('This is not a matrix.')
        else:
            raise ValueError('This is not a matrix.')

    def transpose_matrix(self):
        self.data = [[self.data[row][col] for row in range(len(self.data))] for col in range(len(self.data[0]))]

    def show_matrix(self):
        print('\n'.join('\t'.join(map(str, row)) for row in self.data), '\n')


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix1.show_matrix()
    matrix1.transpose_matrix()
    matrix1.show_matrix()
