def solution(wallpaper):
    lux = []
    luy = []
    rux = []
    ruy = []
    answer = []
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            lux.append(i)
            luy.append(wallpaper[i].find('#'))
    answer.extend([min(lux),min(luy)])
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            rux.append(i+1)
            ruy.append(max([j for j, ele in enumerate(wallpaper[i]) if ele == '#'])+1)
    answer.extend([max(rux),max(ruy)])
    return answer
            