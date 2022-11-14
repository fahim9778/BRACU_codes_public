"""Implement the design of the Author class so that the following output is produced:"""


# Write your code here

class Author:
    # def __init__(self, name = "Default", *books):
    #     self.name = name
    #     self.books = list(books)
    #     for book in books:
    #         self.addBooks(book)
    
    def __init__(self, *info):
        if len(info) == 0:
            self.name = "Default"
            self.books = []
        else:
            self.name = info[0]
            self.books = []
            for book in info[1:]:
                self.addBooks(book)

    def changeName(self, newName):
        self.name = newName

    def addBooks(self, *book):
        for b in book:
            self.books.append(b)
    
    def printDetails(self):
        print(f"Author Name: {self.name}" )
        print("--------")
        print("List of Books: ")
        for book in self.books:
            print(book)


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()


