class AnagramCounter:
    def __init__(self):
        self.counts = {}
        self.original_word = set()
    
    def put(self, word):
        sorted_word = "".join(sorted(word))
        if sorted_word in self.counts:
            self.counts[sorted_word] += 1
        else:
            self.counts[sorted_word] = 1
    
    def get_most_common(self):
        max_word = max(self.counts, key=self.counts.get)
        for word in self.original_word:
            if sorted(word) == sorted(max_word):
                return word

    def print_counts(self):
        print(self.counts)

def get_target_color(burglaries):
    counter = AnagramCounter()
    for burglary in burglaries:
        first_color = burglary[0]
        counter.original_word.add(first_color)
        for item in burglary:
            counter.put(item)
    return counter.get_most_common()

burglaries_case_1 = [
    ["red", "der", "dre"],
    ["red", "dre"],
    ["green", "ngree", "gneer"],
    ["blue", "lube"],
    ["red", "dre"],
    ["pink", "knip"],
    ["pink", "knip"],
    ["pink", "knip"]
]
burgulary_color = get_target_color(burglaries_case_1)
print(burgulary_color)  # Output: red

burglaries_case_2 = [
    ["red", "der"],
    ["green", "ngree", "gneer"],
    ["blue", "lube"],
    ["pink", "knip"]
]

burgulary_color = get_target_color(burglaries_case_2)
print(burgulary_color)  # Output: green
