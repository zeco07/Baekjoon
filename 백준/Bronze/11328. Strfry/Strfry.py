n = int(input())

li = []

for i in range(n):
    li.append(input().split())

for i in range(n):
    if ''.join(sorted(li[i][0])) == ''.join(sorted(li[i][1])):
        print("Possible")
    else:
        print('Impossible')