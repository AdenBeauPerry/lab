class Account:
    def __init__(self, name: str) -> None:
        '''
        Sets the default values for each object

        :param name: This is the name of the account
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Adds value to the account balance

        :param amount: The amount to be added to the balance
        :return: Returns the True if balance is altered
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Removes value from the account balance

        :param amount: The amount to be removed from the balance
        :return: Returns True if balance is altered
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Retrieves the account balance

        :return: Returns the balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Retrieves the name of the account

        :return: Returns the string name
        '''
        return self.__account_name
