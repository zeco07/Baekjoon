n = int(input())
li = [int(i) for i in input().split()]
x = int(input())
li.sort()
left, right = 0, n - 1
count = 0

while (left < right):
    if li[left] + li[right] > x:
        right -= 1
    elif li[left] + li[right] < x:
        left += 1
    else:
        count += 1
        left += 1
        right -= 1
print(count)