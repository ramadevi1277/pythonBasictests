intervals = [(0,30),(15,20),(35,40),(38,50)]
output = [(0,30),(35,50)]

merged = []
intervals.sort()
for start,end in intervals:
  if not merged and merged[-1][1] < start:
    merged.append((start,end))
  else:
    merged[-1] = (merged[-1][0], max(merged[-1][1],end))
 print(merged)   
    
