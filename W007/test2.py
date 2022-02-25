def networks(n, lst):
    check=[set(lst[0])]

    for a in range(1,len(lst)):
        for b in range(len(check)):

            if len(set(lst[a])) + len(check[b]) == len(set(lst[a]) | check[b]):
                check.append(set(lst[a]))
                break
            else:
                pass
            check[b] = set(lst[a]) | check[b]

    for i in range(len(check)):
        print('Social network {} is {}'.format(i,check[i]))

a = networks(6, [(0, 1), (1, 2), (3, 4),(4,7),(5, 6)])
