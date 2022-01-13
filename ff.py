def getPoints():
    try:
        return int(input("Points:"))
    except r:
        return getPoints()
p=getPoints()
print(p)
