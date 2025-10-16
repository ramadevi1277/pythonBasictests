### a number divisible by a and itself is called prime number

for i in range(1,100):
    for j in range(2,i):
        print(i,j)
        if i % j == 0:
            break

    else:
        print("prime numbers are :", i)



result = [i for i in range(1,50) if all(i%j != 0 for j in range(2, i))]

print(result)