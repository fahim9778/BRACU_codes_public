# Create a program that will find the minimum number of coins needed to make a change using dynamic programming.

# Input: 1. The amount of money to be changed
#        2. The number of different coins
#        3. The value of each coin
# Output: The minimum number of coins needed to make the change

class CoinChange:
    def __init__(self, amount, coins):
        self.amount = amount
        self.coins = coins
        self.table = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]

    def solve(self):
        for i in range(1, len(self.coins) + 1):
            for j in range(1, self.amount + 1):
                if self.coins[i - 1] <= j:
                    self.table[i][j] = min(self.table[i - 1][j], self.table[i][j - self.coins[i - 1]] + 1)
                else:
                    self.table[i][j] = self.table[i - 1][j]

    def print_table(self):
        for i in range(len(self.coins) + 1):
            for j in range(self.amount + 1):
                print(self.table[i][j], end=' ')
            print()

    def get_minimum_coins(self):
        return self.table[len(self.coins)][self.amount]

if __name__ == '__main__':
    amount = int(input('Enter the amount: '))
    coins = [int(i) for i in input('Enter the coins: ').split()]
    coin_change = CoinChange(amount, coins)
    coin_change.solve()
    print('Minimum coins needed to make the change: ', coin_change.get_minimum_coins())
    coin_change.print_table()

# Enter the amount: 10
# Enter the coins: 1 2 5
# Minimum coins needed to make the change:  2
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 1 2 2 3 3 4 4 5 5
# 0 1 1 2 2 1 2 2 3 3 2
# 0 1 1 2 2 1 2 2 3 3 2

# Path: CSE111 - Programming Language 2/Other tasks/DP Longest Common Subsequence.py