"""You are a detective trying to solve a mystery involving a group of suspects. You have a list of the suspects and their alibis, but you suspect some of them might be fabricated. To help you investigate, you have created a hash table to store the suspects' alibis. However, the suspects are very clever and have managed to fabricate their alibis in such a way that they all appear to be valid.
Your task is to write a function investigate(alibis)that will take in a list of alibis as strings and determine whether or not any of the alibis are fabricated. The function will return a Boolean value.
You can assume that an alibi is fabricated if it is a palindrome (i.e. it reads the same forwards and backward). If any of the alibis are fabricated, the function should return True, otherwise, it should return False.
You should implement the function using a recursive approach and use a hash table to store the alibis as you investigate them. An alibi is a suspect’s statement in their defense. 
Notes:
•	You should not use any built-in palindrome checking functions in your solution.
•	For palindrome checking, you can omit the alibi’s punctuation marks from your consideration.
"""

class AlibiInvestigator:
    def __init__(self):
        self.checked_alibis = {}

    def is_fabricated(self, alibi):
        alibi = alibi.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace('"', "").lower()
        if alibi in self.checked_alibis:
            return self.checked_alibis[alibi]
        # Remove punctuation marks and spaces using replace() method and convert to lowercase using lower() method
        if self.is_palindrome(alibi):
            self.checked_alibis[alibi] = True
            return True
        else:
            self.checked_alibis[alibi] = False
            return False

    def is_palindrome(self, alibi):
        if len(alibi) <= 1:
            return True
        if alibi[0] != alibi[-1]:
            return False
        return self.is_palindrome(alibi[1:-1])

def investigate(alibis):
    investigator = AlibiInvestigator()
    for alibi in alibis:
        if investigator.is_fabricated(alibi):
            return True
    return False

# Example
print(investigate(["I was at home all night.", "I was at the library."]))  # Output: False
print(investigate(["I was at the mall.", "Madam, in Eden, I'm Adam."]))  # Output: True
print(investigate(["Mr. Owl ate my metal worm", "I was at the mall.", "I was at home all night."]))  # Output: True
print(investigate(["I was at the mall.", "I was at home all night."]))  # Output: False
print(investigate(["I was at the mall.", "I was at home all night", "I was at the library."]))  # Output: False
print(investigate(["I was at the mall.", "I was at home all night", "I was at the library.", "Madam, in Eden, I'm Adam."]))  # Output: True
