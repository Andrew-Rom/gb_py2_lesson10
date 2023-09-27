class Matrix():
    def __init__(self, data):
        self.data = data

    def isMatrix(self):
        if type(self.data) is list:
            for i in range(len(self.data)):
                if type(self.data[i]) is not list:
                    return False
            else:
                return all(len(self.data[i]) == len(self.data[i + 1]) for i in range(len(self.data) - 1))
        else:
            return False

    def transpose_matrix(self):
        if self.isMatrix():
            self.data = [[self.data[row][col] for row in range(len(self.data))] for col in range(len(self.data[0]))]

    def show_matrix(self):
        if self.isMatrix():
            print('\n'.join('\t'.join(map(str, row)) for row in self.data))
            print()
        else:
            print('This is not matrix.')

if __name__ == '__main__':
    my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    my_matrix.show_matrix()
    my_matrix.transpose_matrix()
    my_matrix.show_matrix()
