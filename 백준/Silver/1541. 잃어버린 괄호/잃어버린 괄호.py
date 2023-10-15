import sys

input = sys.stdin.readline

input_string = input()
li = []
current_num = ""
for char in input_string:
    if char.isdigit():
        current_num += char
    else:
        li.append(int(current_num))
        current_num = ""
        if char in ["-", "+"]:
            li.append(char)
check = 0
result = 0
for i in li:
    if type(i) == int and check == 0:
        result += i
    elif type(i) == int and check == 1:
        result -= i
    if i == "-":
        check = 1


print(result)
