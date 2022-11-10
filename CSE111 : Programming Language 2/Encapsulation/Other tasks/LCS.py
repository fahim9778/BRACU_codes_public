"""A Python program that finds the longest common subsequence of two strings."""

def lcs(s1, s2):
    """Finds the longest common subsequence of two strings."""
    if s1 == "" or s2 == "":
        return ""
    elif s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:], s2[1:])
    else:
        return max(lcs(s1[1:], s2), lcs(s1, s2[1:]), key=len)   
    
def main():
    """Main function."""
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("The longest common subsequence is:", lcs(s1, s2))

main()