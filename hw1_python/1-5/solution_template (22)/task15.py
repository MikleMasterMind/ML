from typing import List


def hello(name: str = '') -> str:
    return("Hello," + ' ' + name + '!' if name else "Hello!")


def int_to_roman(num: int) -> str:
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman = ''
    for letter, value in roman_dict.items():
        while num >= value:
            roman += letter
            num -= value
    return roman


def longest_common_prefix(strs_input: List[str]) -> str:
    prefix = strs_input[0].strip() if len(strs_input) > 0 else ''
    for cur in strs_input:
        cur = cur.strip()
        new_prefix = ''
        for i in range(min(len(cur), len(prefix))):
            if prefix[i] == cur[i]:
                new_prefix += cur[i]
            else:
                break
        prefix = new_prefix
        if not prefix:
            break
    return prefix


class BankCard:
    
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit


    def __call__(self, sum_spent: int):
        if sum_spent <= self.total_sum:
            self.total_sum -= sum_spent
            print(f"You spent {sum_spent} dollars.")
        else:
            print("Not enough money to spend sum_spent dollars.")
            raise ValueError


    def __str__(self):
        return "To learn the balance call balance."


    def __add__(self, obj):
        return BankCard(self.total_sum + obj.total_sum, max(self.balance_limit, obj.balance_limit))


    def put(self, put_sum: int) -> None:
        self.total_sum += put_sum
        print(f"You put {put_sum} dollars.")


    @property
    def balance(self):
        if self.balance_limit < 0:
            return self.total_sum
        elif self.balance_limit == 0:
            print('Balance check limits exceeded.')
            raise ValueError
        else:
            self.balance_limit -= 1
            return self.total_sum
            


def primes() -> int:
    primary = 2
    while True:
        while len([d for d in range(1, primary + 1) if primary % d == 0]) != 2:
            primary += 1
        yield primary
        primary += 1


