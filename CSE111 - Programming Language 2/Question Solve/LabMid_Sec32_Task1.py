"""Implement the design of the Person class so that the following output is produced:

Hint:
One person can create only one personal or shared bank account where each account contains an 8 digit account number.
Shared account can be created only if each of the persons has a personal bank account. If one person doesn’t have a personal bank account both of them will fail to create a shared account.
If any person already owns a shared account s/he will not be able to create another shared account even if the other person doesn't own any shared account.
So during the creation of any bank account there might be a use of validity to check whether any person has a personal/ shared account or not.
Shared account number = First 4 digits of the personal bank account number of one person + Last 4 digits of the personal bank account number of another person.
"""


class Person:
    def __init__(self, name, address, age=None):
        self.name = name
        self.address = address
        self.age = age
        self.NID = None
        self.personal_account = None
        self.shared_account = None

    def create_personal_account(self, account_number, NID):
        if self.personal_account is None:
            self.personal_account = account_number
            self.NID = NID
        else:
            print(f"{self.name} has already created a personal account!")

    def create_shared_account(self, other_person):
        if self.personal_account is None or other_person.personal_account is None:
            if self.personal_account is None:
                print(f"{self.name} doesn't have any personal account!")
            else:
                print(f"{other_person.name} doesn't have any personal account!")
        elif self.shared_account is not None or other_person.shared_account is not None:
            if self.shared_account is not None:
                print(f"{self.name} has already created a shared account!")
            else:
                print(f"{other_person.name} has already created a shared account!")
        else:
            new_shared_account = self.personal_account[:4] + other_person.personal_account[-4:]
            self.shared_account, other_person.shared_account = new_shared_account, new_shared_account

    def show_details(self):
        print(f"General Information of {self.name}:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"NID: {self.NID if self.NID is not None else 'N/A'}")
        print(f"Personal Bank Account Number: {self.personal_account if self.personal_account is not None else 'No Personal Account Found!'}")
        print(f"Shared Bank Account Number: {self.shared_account if self.shared_account is not None else 'No Shared Account Found!'}")


p1 = Person("Iqbal", "Banani", 22)
p1.show_details()
print("========================================")
p1.create_personal_account("11112222", 5656)
p1.show_details()
p2 = Person("Afif", "Mohakhali")
p1.create_shared_account(p2)
print("========================================")
p2.create_personal_account("33334444", 7878)
p1.create_personal_account("99990000", 17174848)
print("========================================")
p1.create_shared_account(p2)
p1.show_details()
p2.show_details()
print("========================================")
p3 = Person("Emran", "Gulshan", 34)
p3.create_personal_account("55556666", 4949)
p1.create_shared_account(p3)
p3.show_details()
