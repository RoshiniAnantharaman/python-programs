n,k=map(int,input().split())
if n>0:
    res=1
    for i in range(0,k):
        res=res*n
    print(res)
else:
    print(0)
