import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account("Aden")
        self.a2 = Account("Beau")

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == "Aden"
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == "Beau"
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(-40) is False
        assert self.a1.get_balance() == 30

        with pytest.raises(TypeError):
            self.a1.deposit("Hello")
        assert self.a1.get_balance() == 30

    def test_withdraw(self):
        self.a1.deposit(30)
        assert self.a1.withdraw(15) is True
        assert self.a1.get_balance() == 15

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 15

        assert self.a1.withdraw(-40) is False
        assert self.a1.get_balance() == 15

        with pytest.raises(TypeError):
            self.a1.withdraw("Hello")
        assert self.a1.get_balance() == 15