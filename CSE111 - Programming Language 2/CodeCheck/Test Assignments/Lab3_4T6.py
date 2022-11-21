"""Public URL (for your students): https://codecheck.io/files/2211201218brnqm3vrpr20qefl1mmddmr9f
Edit URL (for you only): https://codecheck.io/private/problem/2211201218brnqm3vrpr20qefl1mmddmr9f/DGCNHZB30OTH9S7RWQF600W68"""

class Customer:
    def __init__(self, name):
        self.name = name

    ##HIDE
    def greet(self, c_name = None):
    ##EDIT def greet(. . .):
    ##HIDE
        if c_name is None:
            print(f"Hello!")
        else:
            print(f"Hello {c_name}!")
    ##EDIT . . .
    
    ##HIDE
    def purchase(self, *items):
    ##EDIT def purchase(self, . . .):
    ##HIDE
        print(f"{self.name}, you purchased {len(items)} item(s):")
        for item in items:
            print(item)
    ##EDIT . . .


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")


## SOME ADDITIONAL HIDDEN TEST CASES MAY RUN TO JUSTIFY PROPER LOGIC
##HIDE
customer_3 = Customer("John")
customer_3.greet("John")
customer_3.purchase("books", "pens", "pencils", "erasers", "rulers")

customer_4 = Customer("Mary")
customer_4.greet()
customer_4.purchase("medicine", "bandages", "gauze", "antiseptic", "antibiotics")

# create unit test for the above code
import unittest

class TestCustomer(unittest.TestCase):
    def test_greet(self):
        customer_1 = Customer("Sam")
        customer_1.greet()
        customer_2 = Customer("David")
        customer_2.greet("David")
        customer_3 = Customer("John")
        customer_3.greet("John")
        customer_4 = Customer("Mary")
        customer_4.greet()

    def test_purchase(self):
        customer_1 = Customer("Sam")
        customer_1.purchase("chips", "chocolate", "orange juice")
        customer_2 = Customer("David")
        customer_2.purchase("orange juice")
        customer_3 = Customer("John")
        customer_3.purchase("books", "pens", "pencils", "erasers", "rulers")
        customer_4 = Customer("Mary")
        customer_4.purchase("medicine", "bandages", "gauze", "antiseptic", "antibiotics")

if __name__ == '__main__':
    unittest.main()