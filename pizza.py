arr=[]
row=[]
col=[]
def valuerect(x1,y1,x2,y2):
    val=[0,0] #mushrrom:tomato
    for i in range(x1,x2):
        val[0]+=row[y1][y2-1][0]
        val[1]+=row[y1][y2-1][1]
    return val


def factors(a):
    arr=[]
    for i in range(int(a**(0.5))):
        if(a%i==0):
            arr.extend([i,a//i])
    return arr

r,c,mini,maxi=map(int,input().strip().split())
dimmini=2*mini
for i in range(r):
    inp=[1 if x=='T' else 0 for x in input().strip()]
    arr.append(inp)

#preprocess

for i in range(r):
    for j in range(c):
        for k in range(i):
            row[k][i][0]+=int(not arr[i][j])
            row[k][i][1]+=arr[i][j]

if(maxi>=(r*c)):
    v=valuerect(0,0,r,c)
    if(all([x>=mini for x in v])): #if count of each > mini
        print(1)
        print(0,0,r-1,c-1)

elif((r*c)<dimmini):
    print(0)

else:
    rectdimmax=factors(maxi)
    rectdimmin=factors(dimmini)
