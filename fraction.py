"""
    Class example

"""


class Fraction:
    def __init__(self, num=0, den=1):
        self.__num: int = num
        self.__den: int = den

    def __str__(self) -> str:
        return f"{self.__num}/{self.__den}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def get_den(self):
        return self.__den

    def get_num(self):
        return self.__num

    def __mul__(self, f):
        num = self.get_num() * f.get_num()
        den = self.get_den() * f.get_den()
        return Fraction(num, den)


if __name__ == "__main__":
    f1 = Fraction(2, 3)
    print(f1, f1.get_num(), f1.get_den())
    f2 = Fraction(4, 5)
    print(f1 * f2)
