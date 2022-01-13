


def shuffle(number):
    shuffles=list()
    
    tolist=[]
    tolist[:0]=str(number)
    for i,v in enumerate(tolist):
        cpy=tolist.copy()
        for j,v2 in enumerate(cpy):
            tmp=cpy[i]
            cpy[i]=cpy[j]
            cpy[j]=tmp
            shuffles.append(int("".join(cpy)))

    return shuffles



print(shuffle(12389474957563373))
