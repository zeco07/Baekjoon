def solution(today, terms, privacies):
    t_dic = {}
    p_dic = []
    answer = []
    for term in terms:
        key, value = term.split()
        t_dic[key] = int(value)
    for privacie in privacies:
        p_dic.append(privacie.split())
    today = int(today.replace('.', ''))
        
    for i in range(len(p_dic)):
        p_yyyy = int(p_dic[i][0][0:4])       # 개인정보 수집 연도
        p_mm = int(p_dic[i][0][5:7])         # 개인정보 수집 월
        p_dd = int(p_dic[i][0][8:])          # 개인정보 수집 일
        p_t = p_dic[i][1]                    # 개인정보 약관 종류
        
        p_mm += t_dic[p_t]
        while True:
            if p_mm > 12:
                p_yyyy += 1
                p_mm -= 12
            else:
                break
            
        p = str(p_yyyy).zfill(4) + str(p_mm).zfill(2) + str(p_dd).zfill(2)
        
        if today >= int(p):
            answer.append(i+1)
            
    return(answer)
