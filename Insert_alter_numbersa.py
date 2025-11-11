asr = [-8,4,0,-21,-1,-6,5,9,7,6,3,21,2]


neg_num = [neg for neg in asr if neg < 0]
pos_num = [pos for pos in asr if pos >= 0]

result = []
i=j=0

if i < len(neg_num) and j < len(pos_num):
    result.append(neg_num[i])
    result.append(pos_num[j])
    i += 1
    j += 1


result.extend(neg_num[i:])
result.extend(pos_num[j:])

print(result)

