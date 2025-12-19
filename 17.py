def split_and_join(line):
    return "-".join(line.split(" "))

input_string = input()
print(split_and_join(input_string))