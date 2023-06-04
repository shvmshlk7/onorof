t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    do=n-n*0.1
    if do<m:
        print("ONLINE")
    elif do>m:
        print("DINING")
    else:
        print("EITHER")
    
