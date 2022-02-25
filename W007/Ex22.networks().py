def networks(n, lst):
    check=[set(lst[0])]

    # allow to combine set if in set of list has the same number
    for a in range(1,len(lst)):
        YesorNoCheck = True
        for b in range(len(check)):
            # check by if the two set are all different, if the same, pass to check another b
            if len(set(lst[a])) + len(check[b]) == len(set(lst[a]) | check[b]):
                pass
            else:

                # if the two set has something the same, combine to one
                check[b] = set(lst[a]) | check[b]
                YesorNoCheck = False
                break

        # if all the two set has checked and all sets are total different, append to a new one
        if YesorNoCheck == True:
            check.append(set(lst[a]))

    for i in range(len(check)):
        print('Social network {} is {}'.format(i,check[i]))

a = networks(6, [(0, 1), (1, 2), (3, 4),(4,7),(5, 6)])



