names={'mary':10999, 'sams':2111, 'aimy':9778, 'tom':20245, 'michale':27115, 'bob':5887, 'kelly':7885}
ret1=sorted(names)
print(ret1)

def f1(x):
    return x[0]

def f2(x):
    return x[1]

ret2=sorted(names.items(), key=f1)
print(ret2)

ret3=sorted(names.items(), key=f2)
print(ret3)

ret4=sorted(names.items(), key=f2, reverse=True)
print(ret4)