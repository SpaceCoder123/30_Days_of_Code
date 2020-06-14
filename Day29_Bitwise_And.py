#!/bin/python3

def bitwise(n,k):
    maxb=0
    for i in range(1,n+1):
        for j in range(1,i):
            b=i&j
            if maxb<b<k:
                maxb=b
                if maxb==k-1:
                    return maxb
    return maxb
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(bitwise(n,k))
