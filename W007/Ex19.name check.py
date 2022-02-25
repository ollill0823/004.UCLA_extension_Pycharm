def names():
    store= []

    while True:
        ask = input('Enter next name: ')
        if ask != ' ':
            store.append(ask)
        else:
            break
    count = 0
    Student = {}
    for i in store:
        if i in Student:
            Student[i] +=1
        else:
            Student[i] = 1
    print(Student)

    for i in range(0,len(Student)):
        if list(Student.values())[i]==1:
            print('There are 1 student named {}'.format(list(Student.keys())[i]))
        else:
            print('There are {} students named {}'.format(list(Student.values())[i], list(Student.keys())[i]))

names()






