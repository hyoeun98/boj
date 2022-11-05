import re
def solution(m, musicinfos):
    info = [i.split(",") for i in musicinfos]
    answer = '(None)'
    max_play_time = 0
    replaced_m = re.sub("([A-Z])#", r" \1#", m)
    
    for i in info:
        t = [list(map(int, i[0].split(":"))), list(map(int, i[1].split(":")))]
        play_time = (t[1][0] - t[0][0]) * 60 + (t[1][1] - t[0][1])
        flag = False
        
        if len(i[3]) >= play_time and not "#" in i[3]:
            music = i[3]
            
        else:
            replaced_len = len("".join(re.findall("[A-Z]#?", i[3])[:play_time]))
            music = i[3][:replaced_len]
            music = re.sub("([A-Z])#", r" \1#", music)  # C C# B
            len_music = len(i[3]) - i[3].count("#")
            music = music * ((play_time + len_music - 1) // len_music)
            if len_music != len(i[3]):
                flag = True

        if flag:
            if replaced_m in music and play_time > max_play_time:
                answer = i[2]
                max_play_time = play_time
            
        else:
            if m in music and play_time > max_play_time:
                answer = i[2]
                max_play_time = play_time
            
    return answer