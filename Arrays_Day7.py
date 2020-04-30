
if __name__ == '__main__':
    n = int(input())
    arr=list(map(int,input().split()))
    for i in range(0,len(arr)):
        print(arr[len(arr)-i-1],end=' ')
