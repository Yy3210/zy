def a(x):
    b={}
    for i in x:
        if x.count(i)!=1:
            b[i]=x.count(i)
    return b
list=[1,2,1,3,4,2,4,3,1,3]
c=a(list)
print(c)