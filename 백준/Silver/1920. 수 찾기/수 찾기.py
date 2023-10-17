import sys

input = sys.stdin.readline

n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))


def BinarySearch(arr, target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


a1.sort()
for i in a2:
    print(BinarySearch(a1, i))
