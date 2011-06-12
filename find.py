def find(str, ch, start=0, end="None"):
    index = start
    if end == "None":
        end = len(str)
    while index < end:
        if str[index] == chr:
            return str[index]
        index += 1
    return -1

