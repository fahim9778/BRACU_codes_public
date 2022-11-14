"""A dynamic programming algorithm to find the longest common subsequence of two strings."""
def lcs(s1, s2):
    """Finds the longest common subsequence of two strings."""
    row = len(s1) + 1
    col = len(s2) + 1
    table = [[0 for x in range(col)] for x in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    print (table[row-1][col-1])
    return lcs_helper(table, s1, s2, row-1, col-1)

def lcs_helper(table, s1, s2, i, j):
    """Helper function for lcs."""
    i = len(s1)
    j = len(s2)

    if i == 0 or j == 0:
        return ""
    LCS_str = ""
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            LCS_str += s1[i-1]
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1
    return LCS_str[::-1]

def main():
    """Main function."""
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("The longest common subsequence is:", lcs(s1, s2))

main()