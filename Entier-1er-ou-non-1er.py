while 1:
    try:
        n=int(input('taper n'))
    except:
        print('erreur')
    else:
        if n>0:
            break
        for i in range(2,n//2+1):
            if n%i==0:
                print('non premier')
                break
            else:
                print('premier')
        
