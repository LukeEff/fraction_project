"""
    Class example

"""
from typing import List, Set
import random
import string


class Self_Check_01:
    def __init__(self, lst=['cat', 'dog', 'rabbit']):
        self.lst = lst

    def __str__(self) -> str:
        return f"{self.lst} {self.letters}"

    def __repr__(self) -> str:
        return self.__str__()

    # Original
    def to_letters(self) -> list:
        letters: List[str] = []
        for word in self.lst:
            for lett in word:
                letters.append(lett)
        return letters

    # Single letter, set, no duplicates
    def to_letters_set(self) -> set:
        letters = set()
        for word in self.lst:
            for lett in word:
                letters.add(lett)
        return letters

    # Letter, list comprehension
    def to_letters_comp(self) -> list:
        letters = [letter for word in self.lst for letter in word]
        return letters

    # Single letter, list comprehension
    def to_letters_comp(self) -> list:
        letters = []
        [letters.append(letter) for word in self.lst for letter in word if not letters.__contains__(letter)]
        return letters

    def shakespeare(self):

        closest = ('', -1)
        quote = "ok"
        length = len(quote)
        letters = string.ascii_lowercase + ' '

        for i in range(90):
            scrambled = self.getRandomShake(letters, length)
            close = self.check_str_shake(quote, scrambled)
            closest = close if close[1] > closest[1] else closest
            print(scrambled )
            if closest[1] == 3:
                return closest

        return closest


    def check_str_shake(self, quote, scrambled):
        count = 0
        for i in range(len(quote)):
            if quote[i] == scrambled[i]:
                count += 1
        return scrambled, count

    def getRandomShake(self, letters, length):
        return ''.join(random.choice(letters) for i in range(length))

if __name__ == "__main__":
    f1 = Self_Check_01(['cat', 'dog', 'rabbit'])
    print(f1.shakespeare())
