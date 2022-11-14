"""design the EnigmaMachine class that will generate the given output for the provided driver code. Keep in mind that the cipher method takes as input an arbitrary number of texts for encryption and will print a warning message if no text is passed. On the other hand, the decipher method takes as input a list containing ciphered texts for decryption and will print a warning message if no list is passed. Also, the encryption works by replacing the key of the Enigma Machine inside a text with ‘#’ character. The decryption works the other way around. Both the methods return a list of either ciphered or deciphered texts as output."""
class EnigmaMachine:
    def __init__(self, team, key):
        self.team = team
        self.key = key
        print(f"Enigma Machine used by {self.team} works with '{self.key}' key.")
    def cipher(self, *texts):
        if len(texts) == 0:
            print(f"No message to cipher!")
            return None
        ciphered = []
        for text in texts:
            ciphered.append(text.replace(self.key, '#'))
        return ciphered
    def decipher(self, *texts):
        if len(texts) == 0:
            print(f"No message to decipher!")
            return None
        deciphered = []
        for text in texts[0]:
            deciphered.append(str(text).replace('#', self.key))
        return deciphered

em1 = EnigmaMachine("German Luftwaffe", 't')
em2 = EnigmaMachine("British Royal Air Force", 'i')
print("=================================")

encrypted_texts = em1.cipher()
print(f"Encrypted texts: {encrypted_texts}")
encrypted_texts = em1.cipher("We will attack the British cities!")
print(f"Encrypted texts: {encrypted_texts}")
print("=================================")

decrypted_texts = em2.decipher()
print(f"Decrypted texts: {decrypted_texts}")
decrypted_texts = em2.decipher(encrypted_texts)
print(f"Decrypted texts: {decrypted_texts}")
print("=================================")

em2.key = 't'
decrypted_texts = em2.decipher(encrypted_texts)
print(f"Decrypted texts: {decrypted_texts}")
print("=================================")

em2.key = 'i'
encrypted_texts = em2.cipher("We will defend our air!", "Alan Turing is our hero!")
print(f"Encrypted texts: {encrypted_texts}")
print("=================================")

decrypted_texts = em1.decipher(encrypted_texts)
print(f"Decrypted texts: {decrypted_texts}")
