import functools

data = {}

with open("input.txt") as f:
    for line in f.readlines():
        command, key = line.split(" -> ")
        data[key.strip()] = command


@functools.lru_cache()
def get_value(key):
    try:
        return int(key)
    except ValueError:
        command = data[key].split(" ")

        if "AND" in command:
            return get_value(command[0]) & get_value(command[2])
        elif "OR" in command:
            return get_value(command[0]) | get_value(command[2])
        elif "LSHIFT" in command:
            return get_value(command[0]) << get_value(command[2])
        elif "RSHIFT" in command:
            return get_value(command[0]) >> get_value(command[2])
        elif "NOT" in command:
            return ~get_value(command[1]) & 0xFFFF
        else:
            return get_value(command[0])


result = get_value("a")
print("result", result)
data["b"] = str(result)
get_value.cache_clear()
print(get_value("a"))
