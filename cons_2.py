def solution(A, k, l):
    alice_apples = 0
    Bob_apples = 0
    total = 0
    # Implement your solution here
    if len(A) > k + l:
        #import pdb;pdb.set_trace()
        for each in range((k - 1), (k-1)+k):
            alice_apples += A[each]
        for each_1 in range((k + l) + 1, len(A)):
            Bob_apples += A[each_1]
        total = alice_apples + Bob_apples
        #return total
        print(total)

    else:
        #return -1
        print("-1")


solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2)
solution([10, 19, 15], 2, 2)
solution([10,19,15,20,28],2,2)
