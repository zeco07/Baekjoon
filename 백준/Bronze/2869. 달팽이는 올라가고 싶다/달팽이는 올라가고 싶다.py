import math

a, b, v = map(int,input().split())

if (1 <= b and b < a and a <= v and v <= 1000000000):
    day = (v-b)/(a-b)
    print(math.ceil(day))