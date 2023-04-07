def solution(players, callings):
    #선수 : 위치
    p_idx_dict = {player: i for i, player in enumerate(players)}
    #위치 : 선수
    idx_p_dict = {i: player for i, player in enumerate(players)}
    
    for call in callings:
        cur_idx = p_idx_dict[call]              # 부른 선수의 현재 등수
        pre_idx = cur_idx-1                     # 부른 선수의 앞 등수
        cur_player = call                        # 부른 선수
        pre_player = idx_p_dict[pre_idx]         # 부른 선수의 앞 선수
        
        p_idx_dict[cur_player] = pre_idx
        p_idx_dict[pre_player] = cur_idx
        
        idx_p_dict[cur_idx] = pre_player
        idx_p_dict[pre_idx] = cur_player
        
    return list(idx_p_dict.values())