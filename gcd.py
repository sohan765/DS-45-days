
def gcd(m,n):
    fm = []
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    
    fn = []
    for j in range(1,n+1):
        if(n%j==0):
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[-1])  



def gcd2(m,n):
    cf= []
    for i in range(1,min(m,n)+1):
        if (m%i==0 and n%i==0):
            cf.append(i)
    return (cf[-1])


def gcd3(m,n):
    cf= []
    for i in range(1,min(m,n)+1):
        if (m%i==0 and n%i==0):
            mrcf = i
    return (mrcf)


print(gcd3(8,12))
def gcd4(m,n):
    i = min(m,n)
    while i>0:
        if (m%i==0 and n%i==0):
            return(i)
        else:
            i = i-1

print(gcd4(8,12))
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return n

    else:
        return (gcd(n,m%n))
print(gcd(4,8))

