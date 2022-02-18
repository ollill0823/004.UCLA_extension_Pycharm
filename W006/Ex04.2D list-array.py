def array(a):
    for i in range(a):
        for j in range(a):
            cal=(i+1)*(j+1)
            print('{:4}'.format(cal), end='')
        print('')



b=array(12)