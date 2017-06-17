for i in range(0,10):
    m=[]
    for j in range(0,i+1): 
        m.append('%d*%d=%d' % (i,j,i*j))
    print("\t".join(m))