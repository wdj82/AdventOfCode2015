def parseInput():
    with open("input.txt") as f:
        data = [sorted([int(num) for num in x.strip().split("x")]) for x in f]
    return data


def find_wrapping(length, width, height):
    sideAreas = [length * width, width * height, height * length]
    return 2 * sum(sideAreas) + min(sideAreas)


def find_ribbon(length, width, height):
    volume = length * width * height
    return length * 2 + width * 2 + volume


def total_wrapping(input):
    total_square_feet = 0
    total_ribbon = 0
    for length, width, height in input:
        total_square_feet += find_wrapping(length, width, height)
        total_ribbon += find_ribbon(length, width, height)
    print(total_square_feet)
    print(total_ribbon)


# input = sorted([int(num) for num in "3x4x2".split("x")])
# l, w, h = input
# print(l, w, h)
# print(find_wrapping(l, w, h))
# print(find_ribbon(l, w, h))
input = parseInput()
total_wrapping(input)
