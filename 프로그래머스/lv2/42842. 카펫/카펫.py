def solution(brown, yellow):
    return next([yellow//i+2, i+2] for i in range(1, int(yellow**0.5)+1) if yellow % i == 0 and (i + yellow//i) * 2 + 4 == brown)
