def parseInput():
    with open("input.txt") as f:
        data = [x.strip() for x in f]
    return data


def is_nice_string(string):
    vowels = 0
    has_duplicate = False
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False
    for i in range(len(string)):
        if string[i] in "aeiou":
            vowels += 1

        # make sure we don't go out of bounds looking for duplicates
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                has_duplicate = True

    # print(has_duplicate, vowels)
    return has_duplicate and vowels >= 3


def is_really_nice_string(string):
    found_pair = False
    for i in range(len(string) - 3):
        substring = string[i : i + 2]
        if substring in string[i + 2 :]:
            found_pair = True
            break

    if not found_pair:
        return False

    found_duplicate = False
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            found_duplicate = True
            break
    return found_duplicate


def num_nice_strings(input):
    count_one = 0
    count_two = 0
    for string in input:
        if is_nice_string(string):
            count_one += 1
        if is_really_nice_string(string):
            count_two += 1
    print(count_one)
    print(count_two)


input = parseInput()
num_nice_strings(input)
