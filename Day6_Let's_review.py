T=int(input())
for i in range(T):
    x=list(input())
    EVEN=[]
    ODD=[]
    for i in range(0,len(x)):
        if i==0 or i%2==0:
            EVEN.append(x[i])
        elif i%2!=0:
            ODD.append(x[i])
            
    print('{} {}'.format(''.join(EVEN),''.join(ODD)))
