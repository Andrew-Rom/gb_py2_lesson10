class Card():
    def __init__(self, balance):
        self.__balance = balance
        self.__operations = []
        self.__operation_counter = 0

    def get_balance(self):
        return self.__balance

    def get_operation_counter(self):
        return self.__operation_counter

    def set_operation_counter(self, counter:int):
        self.__operation_counter = counter

    def get_operations(self):
        return self.__operations


    def add_funds(self, money: int, operation:str = 'Add funds'):
        temp = self.__balance
        self.__balance += money
        self.__operations.append((operation, temp, money, self.__balance))
        self.__operation_counter += 1

    def withdraw_funds(self, money: int, operation:str = 'Withdraw funds'):
        temp = self.__balance
        if self.__balance >= money:
            self.__balance -= money
            self.__operations.append((operation, temp, money, self.__balance))
            self.__operation_counter += 1
        else:
            print('You do not have enough funds in your account to make the operation.')
