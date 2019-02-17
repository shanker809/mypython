def add_fraction(n1,d1,n2,d2):
    num=(n1*d1)+(n2*d1)
    den=d1*d2
    return num,den

    n1=2
    d1=3
    n2=3
    d2=4

    res= add_fraction(n1,d1,n2,d2)
    print (str(res[0])+"/"+str(res[1]))