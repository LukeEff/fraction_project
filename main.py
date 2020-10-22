# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    nom = 1
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    x, y = (4, 66), (55, 67)
    print(x, y)


def test():
    a = 0

    def test2(a):
        a += 1
        return a

    return test2(a)

def make_counter():
    count = [0]

    def next_num():
        count[0] += 1
        return count[0]

    return next_num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    #print(test())

    counter1 = make_counter()
    counter2 = make_counter()

    for i in range(1,4):
        print(counter1())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
