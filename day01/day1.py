# testInput = ")())())"
from input import input


def find_floors(parens):
    height = 0
    for paren in parens:
        height += 1 if paren == "(" else -1
    print(height)


def find_basement(parens):
    height = 0
    for index, paren in enumerate(parens):
        height += 1 if paren == "(" else -1
        if height < 0:
            print(index + 1)
            return


find_floors(input)
find_basement(input)
