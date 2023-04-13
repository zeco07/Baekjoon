def solution(sizes):
    w = []
    h = []
    for a, b in sizes:
        if a < b:
            a, b = b, a
        w.append(a)
        h.append(b)
    return max(w)*max(h)