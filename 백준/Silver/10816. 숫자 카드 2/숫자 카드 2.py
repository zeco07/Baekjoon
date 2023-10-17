import sys

input = sys.stdin.readline

n = int(input())
target_card = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))


def BinarySearch(arr, target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return cnt.get(target)
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0


target_card.sort()
cnt = {}
for i in target_card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
for i in card:
    print(BinarySearch(target_card, i), end=" ")
