from input import input


def update_position(pos, key):
    return {
        ">": (pos[0] + 1, pos[1]),
        "<": (pos[0] - 1, pos[1]),
        "^": (pos[0], pos[1] - 1),
        "v": (pos[0], pos[1] + 1),
    }[key]


def houses_one_present(input):
    current_loc = [0, 0]
    visited = {(0, 0): True}
    for direction in input:
        current_loc = update_position(current_loc, direction)
        visited[current_loc] = True
    print(len(visited))


def houses_with_robot(input):
    santa_location = [0, 0]
    robot_location = [0, 0]
    visited = {(0, 0): True}
    for index, direction in enumerate(input):
        if index % 2 == 0:
            santa_location = update_position(santa_location, direction)
            visited[santa_location] = True
        else:
            robot_location = update_position(robot_location, direction)
            visited[robot_location] = True
    print(len(visited))


# input = "^v"
# input = "^>v<"
# input = "^v^v^v^v^v"
houses_one_present(input)
houses_with_robot(input)
