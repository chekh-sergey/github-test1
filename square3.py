def sq_mult(a,b):
    return (a[0]*b[1] - a[1]*b[0]) / 2.
# initial data
abc=((0,4),(3,4),(3,0))
s = 0
for i in range(2):
    s+= sq_mult(abc[i],abc[i+1])
s += sq_mult(abc[2],abc[0])
print(abs(s))
