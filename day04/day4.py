from hashlib import md5
from itertools import count

key = "iwrupvqb"


def part_one():
    for num in count(1):
        test = key + str(num)
        hash = md5(test.encode()).hexdigest()
        if hash[:5] == "00000":
            print(num)
            return


def part_two():
    for num in count(1):
        test = key + str(num)
        hash = md5(test.encode()).hexdigest()
        if hash[:6] == "000000":
            print(num)
            return


part_one()
part_two()
