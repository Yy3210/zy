list=[5,3,'a',1,'m',8,7]
alist=[x for x in list if type(x) !=str]
blist=sorted(alist)
print(blist)