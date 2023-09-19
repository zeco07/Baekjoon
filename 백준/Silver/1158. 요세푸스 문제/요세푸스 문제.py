n, k = map(int,input().split())

people = [_ for _ in range(1,n+1)]
ans = []
idx = k-1
while (people):
    if idx >= len(people):
        idx %= len(people)
    ans.append(people.pop(idx))
    idx += k-1

# formatted_list = "<" + ", ".join(map(str, ans)) + ">"
# print(formatted_list)

print(str(ans).replace('[','<').replace(']','>'))
