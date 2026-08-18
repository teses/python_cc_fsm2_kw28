class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    # string
    def __str__(self):
        return f"{self.name}, {self.alter}"

    # representation
    def __repr__(self):
        return f"Person('{self.name}', {self.alter})"

    # equal to (used in comparison)
    def __eq__(self, other):
        return self.name == other.name and self.alter == other.alter

    # less than (used in comparison)
    def __lt__(self, other):
        return self.alter < other.alter

    # greater than (used in comparison)
    #def __gt__(self, other):
    #    return self.alter > other.alter

    # less than or equal to (used in comparison)
    def __le__(self, other):
        return self.alter <= other.alter

    # greater than or equal to (used in comparison)
    #def __ge__(self, other):
    #    return self.alter >= other.alter

    # not equal to (used in comparison)
    def __ne__(self, other):
        return self.alter != other.alter

    # add (addition)
    def __add__(self, other):
        if isinstance(other, Person):
            return self.alter + other.alter
        elif isinstance(other, int):
            return self.alter + other

    # sub (subtraction)
    def __sub__(self, other):
        if isinstance(other, Person):
            return self.alter - other.alter
        elif isinstance(other, int):
            return self.alter - other

    # mul (multiplication)
    def __mul__(self, other):
        if isinstance(other, Person):
            return self.alter * other.alter
        elif isinstance(other, int):
            return self.alter * other

    # true div (true division, division with floating point result)
    def __truediv__(self, other):
        if isinstance(other, Person):
            return self.alter / other.alter
        elif isinstance(other, int):
            return self.alter / other

    # floor div (floor division, division with rounding down)
    def __floordiv__(self, other):
        if isinstance(other, Person):
            return self.alter // other.alter
        elif isinstance(other, int):
            return self.alter // other

    # mod (modulus)
    def __mod__(self, other):
        if isinstance(other, Person):
            return self.alter % other.alter
        elif isinstance(other, int):
            return self.alter % other

    # pow (power)
    def __pow__(self, other):
        if isinstance(other, Person):
            return self.alter ** other.alter
        elif isinstance(other, int):
            return self.alter ** other

    # neg (negative)
    def __neg__(self):
        return -self.alter

    # pos (positive)
    def __pos__(self):
        return +self.alter

    # abs (absolute value)
    def __abs__(self):
        return abs(self.alter)

    # len (length)
    def __len__(self):
        return len(self.name)

    # call (function call)
    def __call__(self):
        return self.alter

    # hash (hash value)
    def __hash__(self):
        return hash(str(element for element in self.__dict__.values()))


p = Person("Max", 26)
print("str")
print(p)
print("repr")
repr(p)

p2 = Person("Max", 25)
#print("eq")
#print(p == p2)
print("less than")
print(p > p2)
#print("less than or equal to")
#print(p <= p2)
print("greater than")
print(p < p2)
#print("greater than or equal to")
#print(p >= p2)
#print("not equal to")
#print(p != p2)
"""
print("add")
print(p + p2)
print("add int")
print(p + 10)

print("subtract")
print(p - p2)
print("subtract int")
print(p - 10)

print("multiply")
print(p * p2)
print("multiply int")
print(p * 10)

print("truediv")
print(p / p2)
print("truediv int")
print(p / 10)

print("floordiv")
print(p // p2)
print("floordiv int")
print(p // 10)

print("modulus")
print(p % p2)
print("modulus int")
print(p % 10)

print("pow")
print(p ** p2)
print("pow int")
print(p ** 10)

print("negative")
print(-p)
print("positive")
print(+p)
print("absolute value")
print(abs(p))

print("length")
print(len(p))

print("call")
print(p())

print("hash")
print(hash(p))
"""