X = int(input())

line = 0
end = 0

while(X>end):
    line += 1
    end += line


if (line % 2 == 0):    # 짝수라인
    top = line - (end-X)
    bottom = (end-X) + 1
    print(f"{top}/{bottom}")

else:                   # 홀수라인
    top = (end-X) +1
    bottom = line - (end-X)
    print(f"{top}/{bottom}")