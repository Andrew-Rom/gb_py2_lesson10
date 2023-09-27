class Atm():

    def __init__(self):
        self.__BONUS = 3 / 100
        self.__BONUS_CONDITION = 3
        self.__TAX_RATE = 10 / 100
        self.__TAX_CONDITION = 5_000_000
        self.__ATM_INTERESTS = 1.5 / 100
        self.__ATM_INTERESTS_MIN = 30
        self.__ATM_INTERESTS_MAX = 600

    def main_menu(self, Card):
        while True:
            print('ATM main menu.\n'
                  'Balance of your card is', Card.get_balance(), '\n'
                                                                 'Select operation:\n'
                                                                 '1 - Add funds\n'
                                                                 '2 - Withdraw funds\n'
                                                                 '0 - Exit and return card')
            operation = input('> ')
            match operation:
                case '1':
                    cash = self.get_amount()
                    if cash == -1:
                        print('You entered incorrect amount')
                    else:
                        self.hold_tax(Card)
                        Card.add_funds(money=cash)
                        if Card.get_operation_counter() == self.__BONUS_CONDITION:
                            self.operation_bonus(Card)
                case '2':
                    cash = self.get_amount()
                    if cash == -1:
                        print('You entered incorrect amount')
                    elif cash > Card.get_balance():
                        print('Your card balance is less than the amount entered')
                    else:
                        self.hold_tax(Card)
                        cash += self.atm_fee(cash)
                        Card.withdraw_funds(money=cash)
                case '0':
                    print('Thank you for using our ATM.')
                    print(Card.get_operations())
                    exit()
                case _:
                    print('Incorrect selection. Please, try again \n')

    def get_amount(self):
        amount = input('Enter the amount > ')
        return int(amount) if amount.isdigit() and int(amount) % 50 == 0 else -1

    def atm_fee(self, money: int):
        atm_fee = money * self.__ATM_INTERESTS
        if atm_fee < self.__ATM_INTERESTS_MIN:
            atm_fee = self.__ATM_INTERESTS_MIN
        if atm_fee > self.__ATM_INTERESTS_MAX:
            atm_fee = self.__ATM_INTERESTS_MAX
        return atm_fee

    def operation_bonus(self, Card):
        money = Card.get_balance() * self.__BONUS
        Card.add_funds(money, operation='Got bonus')
        Card.set_operation_counter(0)

    def hold_tax(self, Card):
        if Card.get_balance() > self.__TAX_CONDITION:
            tax = Card.get_balance() * self.__TAX_RATE
            Card.withdraw_funds(tax, operation='Paid extra taxes')
