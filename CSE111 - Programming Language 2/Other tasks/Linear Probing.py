# Create a hash table with linear probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                        not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = HashTable(10)
H.put(54, "cat")
H.put(26, "dog")
H.put(93, "lion")
H.put(17, "tiger")
H.put(77, "bird")
H.put(31, "cow")
H.put(44, "goat")
H.put(55, "pig")
H.put(20, "chicken")
H.put(20, "duck")
H.put(41, "horse")
H.put(20,  "tortoise")

# H[54] = "cat"
# H[26] = "dog"
# H[93] = "lion"
# H[17] = "tiger"
# H[77] = "bird"
# H[31] = "cow"
# H[44] = "goat"
# H[55] = "pig"
# H[20] = "chicken"
# H[20] = "duck"
# H[41] = "horse"
# H[20] =  "tortoise"

print("Slots: ", H.slots)
print("Data: ", H.data)

print(H.get(20))
