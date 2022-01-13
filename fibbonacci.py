prv1=0;
prv2=1;
cur=1;

while cur<100:
    print(cur)
    cur=prv1+prv2;
    prv1=prv2
    prv2=cur
