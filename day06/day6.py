def parseInput():
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
            command, start, _, end = line.strip().rsplit(" ", 3)
            data.append(
                [
                    [int(num) for num in start.split(",")],
                    [int(num) for num in end.split(",")],
                    command,
                ]
            )
    return data


def count_lights(input):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for start, end, command in input:

        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if command == "toggle":
                    lights[row][col] = 1 - lights[row][col]
                elif command == "turn on":
                    lights[row][col] = 1
                else:
                    lights[row][col] = 0

    print(sum(sum(status) for status in lights))


def count_brightness(input):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    brightness = 0
    for start, end, command in input:

        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if command == "toggle":
                    lights[row][col] += 2
                    brightness += 2
                elif command == "turn on":
                    lights[row][col] += 1
                    brightness += 1
                elif lights[row][col] > 0:
                    lights[row][col] -= 1
                    brightness -= 1

    print(brightness)


input = parseInput()
count_lights(input)
count_brightness(input)
