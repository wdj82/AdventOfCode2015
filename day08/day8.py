def parseInput():
    with open("input.txt") as f:
        data = [x.strip() for x in f]
    return data


input = parseInput()

code_count = 0
char_count = 0
encode_count = 0
for string in input:
    # print(string)
    code_count += len(string)
    char_count += len(bytes(string[1:-1], "utf-8").decode("unicode_escape"))
    encode_count += string.count('"') + 2 + string.count("\\")


print(code_count - char_count)
# print(encode_count)
print(encode_count)
