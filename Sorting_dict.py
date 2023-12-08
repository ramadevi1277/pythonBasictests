#### Sorting dict using values




xs = {'g':6, 'h':1, 'a':3, 'k':3, 'f':4}

print(sorted(xs.items(), key=lambda x: x[1]))

###Sorting dict by keys

print((sorted(xs.items(), key=lambda x: x[0])))
sor_dcit =sorted(xs.items(), key=lambda x: x[0])
print(max(zip(xs.values(),xs.keys())))

