"""Write a program to find the minimum number of coins required to make change for an amount of n cents."""
def min_coins(n):
    """Finds the minimum number of coins required to make change for an amount of n cents."""
    coins = [1, 5, 10, 25]
    num_coins = [0 for x in range(n+1)]
    num_coins[0] = 0
    for i in range(1, n+1):
        num_coins[i] = float("inf")
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins[i] = min(num_coins[i], num_coins[i-coins[j]] + 1)
    return num_coins[n]

def main():
    """Main function."""
    n = int(input("Enter amount of cents: "))
    print("Minimum number of coins:", min_coins(n))

main()