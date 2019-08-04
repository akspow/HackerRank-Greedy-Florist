def getMinimumCost(k, c):
    c.sort()
    friendbuys=0
    sum=0
    for i in range(len(c)-1,-1,-1):
        sum+=((friendbuys//k)+1)*c[i]
        friendbuys+=1
    return sum
