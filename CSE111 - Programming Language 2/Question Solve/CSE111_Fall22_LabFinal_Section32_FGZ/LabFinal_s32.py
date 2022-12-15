##HIDE

# Public URL (for your students): https://codecheck.io/files/2212140659817p9no1b28j4cjqttgqz5a23
# Edit URL (for you only): https://codecheck.io/private/problem/2212140659817p9no1b28j4cjqttgqz5a23/ANDVD00Q92KSF9N3T3HUBOP17
class Grandfather:
    _title = "Khan"
    __wealth = "1 Crore"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(
            f"My name is {self.name} and I am {self.age} years old. My title is {self._title} and I have {self.__wealth} in my bank account.")

    @classmethod
    def display_title(cls):
        print(f"My title is {cls._title}")

    @classmethod
    def display_wealth(cls):
        if issubclass(Grandfather, cls):
            print(f"My wealth is {cls.__wealth}")
        else:
            print(f"You are not a {Grandfather._title}. You can't access my wealth.")


class Father(Grandfather):
    _title = "Hasan"  # Variable Overriding

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.hair = "Black"
        self.eye = "Brown"

    def display(self):
        print(
            f"My name is {self.name} and I am {self.age} years old. My title is {self._title} and I income {self.salary} per month.")
        print(f"I have {self.hair} hair and {self.eye} eyes.")


# Implement the Mother class as instructed in the question paper

class Mother:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hair = "Red"
        self.eye = "Blue"

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old. I have {self.hair} hair and {self.eye} eyes.")


class Son(Father, Mother):
    def __init__(self, name, age, salary, tech):
        super().__init__(name, age, salary)
        self.tech = tech

    def display(self):
        super().display()
        print(f"I have hobby for {self.tech}.")


class Daughter(Mother, Father):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def display(self):
        super().display()
        print(f"I like {self.hobby}.")

##EDIT Paste your code in this white box
