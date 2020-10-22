"""
    Class example

"""


# Get the greatest common factor.
def get_common_factor(num, den):
    while num % den != 0:
        old_num = num
        old_den = den

        num = old_den
        den = old_num % old_den

    return den


class Fraction:
    def __init__(self, num=0, den=1):
        if type(num) is not int or type(den) is not int:
            raise ValueError("Numerator and denominator must be integers!")
        gcf = get_common_factor(num, den)
        self.__num: int = int(num / gcf)
        self.__den: int = int(den / gcf)

    # String representation of object.
    def __str__(self) -> str:
        return f"{self.__num}/{self.__den}"

    # String representation of object.
    def __repr__(self) -> str:
        return self.__str__()

    # Fraction numerator.
    @property
    def num(self):
        return self.__num

    # Fraction denominator.
    @property
    def den(self):
        return self.__den

    # Get denominator of fraction.
    def get_den(self):
        return self.__den

    # Get numerator of fraction.
    def get_num(self):
        return self.__num

    # Multiplication operator override.
    def __mul__(self, f):
        num = self.get_num() * f.get_num()
        den = self.get_den() * f.get_den()
        return Fraction(num, den)

    # Subtraction operator override.
    def __sub__(self, f):
        num = self.get_num() * f.get_den() - self.get_den() * f.get_num()
        den = self.get_den() * f.get_den()
        common_fact = get_common_factor(num, den)
        return Fraction(num // common_fact, den // common_fact)

    # Addition operator override.
    def __add__(self, f):
        if type(f) is Fraction:
            num = self.get_num() * f.get_den() + self.get_den() * f.get_num()
            den = self.get_den() * f.get_den()
            common_fact = get_common_factor(num, den)
            return Fraction(num // common_fact, den // common_fact)
        return f + self

    # RAddition operator override.
    def __radd__(self, other):
        if type(other) is Fraction:
            return self + other
        return self + Fraction(other, 1)

    # IAddition operator override.
    def __iadd__(self, other):
        num = self + other
        return num

    # Less than or equal to operator override.
    def __lt__(self, f):
        first_num = self.get_num() * f.get_den()
        second_num = f.get_num() * self.get_den()
        return first_num <= second_num

    # Greater than operator override.
    def __gt__(self, f):
        return not (self < f)

    # Greater than or equal to operator override.
    def __ge__(self, f):
        return self > f or self == f

    # Greater than or equal to operator override.
    def __le__(self, f):
        return self < f or self == f

    # Division operator override.
    def __truediv__(self, f):
        num = self.get_num() * f.get_den()
        den = self.get_den() * f.get_num()
        return Fraction(num, den)

    # Equality operator override.
    def __eq__(self, f):
        num = self.get_num() * f.get_den()
        num_2 = f.get_num() * self.get_den()
        return num == num_2

    # Inequality operator override
    def __ne__(self, f):
        return not self == f


if __name__ == "__main__":
    f1 = Fraction(2, 3)
    f2 = Fraction(4, 5)

    print(f1)
    print(f2)

    print(f1 * f2)
    print(f1 / f2)
    print(f1 - f2)
    print(f1 > f2)
    print(f1 < f2)
    print(f1 + f2)

    f1 += f2
    print(f1)

    f1 += 4
    print(f1)
