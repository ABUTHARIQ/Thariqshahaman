b=int(input())
c=list(map(int,input().split()))
d=[]
for x in range(b):
    for i in range(x+1,len(c)):
        if(c[i]==c[x]):
          d.append(c[x])
if (len(d)==0):
    print("unique")
else:
    d.sort()
    l=set(d)
    for x in l:
        print(x,end=" ")
