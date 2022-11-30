# Create a python class "Clock" that shows examples of Operator Overloading.

class Clock:
    def __init__(self, time):
        self.hour, self.min = int(time.split(':')[0]), int(time.split(':')[1])
        if (self.hour < 0 or self.hour > 23) or (self.min < 0 or self.min > 59):
            self.hour, self.min = None, None
            raise ValueError('Invalid time')

    def __add__(self, other):
        if isinstance(other, int):
            return Clock(f'{(self.hour + other) % 24}:{self.min}')
        elif isinstance(other, Clock):
            # new_hour, new_min = divmod(self.min + other.min, 60)
            new_hour = (self.min + other.min) // 60
            new_min = (self.min + other.min) % 60
            return Clock(f'{(new_hour + self.hour + other.hour) % 24}:{new_min}')
        else:
            raise TypeError('Invalid type')

    def __sub__(self, other):
        if isinstance(other, int):
            return Clock(f'{(self.hour - other) % 24}:{self.min}')
        elif isinstance(other, Clock):
            # new_hour, new_min = divmod(self.min - other.min, 60)
            new_hour = (self.min - other.min) // 60
            new_min = (self.min - other.min) % 60
            return Clock(f'{(new_hour + self.hour - other.hour) % 24}:{new_min}')
        else:
            raise TypeError('Invalid type')

    def __repr__(self):
        return f'{str(self.hour).zfill(2)}:{str(self.min).zfill(2)}'
        # zfill() method returns the string left filled with zeros in a string of length width.
        # For example, '7'.zfill(2) returns '07'.
        # If width is less than or equal to the length of the string, no filling is done.
        # For example, '23'.zfill(1) returns '23'.

    __radd__ = __add__
    __rsub__ = __sub__


time_1 = Clock('10:30')
time_2 = Clock('19:45')
time_3 = Clock('16:16')

print(time_1 + time_2)
print(time_2 - time_1)
print(time_2 - 10)
print(time_1 + 10)
print(10 - time_2)

print(time_1 - time_2 + time_3)

# time_4 = Clock('25:30')
# time_5 = Clock('10:70')
