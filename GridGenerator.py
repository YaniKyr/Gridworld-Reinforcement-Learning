import random as rnd
def GridGenerator(N,M,lava,endstates):
    arr = [[-1 for j in range(M)]for i in range(N)]
    lax = []
    lay = []
    for i in range(lava):
        lax.append(rnd.randrange(0,N))
        lay.append(rnd.randrange(0,M))
    for i in range(lava):
        arr[lax[i]][lay[i]] = -10
    endx=[]
    endy =[]
    for i in range(endstates):
        endx.append(rnd.randrange(2,N))
        endy.append(rnd.randrange(2,M))
    temp=0
    for temp in range(endstates):
        arr[endx[temp]][endy[temp]] = 50
        
    arr[0][0] = -1
    #print("The generated arr is",arr)
    return arr
