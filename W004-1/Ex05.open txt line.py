<<<<<<< HEAD
def myGrep(filename,target):
    filename=open(filename, 'r', encoding="utf-8")
    f=filename.read()
    number=f.count(target)
    start =0
    for i in range(number):
        start =f.index(target,start)
        end=f.index('.',start)
        print(f[start : end+1] + '\n')
        start = end


a=myGrep('i-have-a-dream.txt','I have a dream')
=======
def words(filename):
    filename= open(filename, 'r', encoding="utf-8")
    f = filename.read()
    split = f.split()

    return split

a=words('i-have-a-dream.txt')
print(a)


>>>>>>> origin/main
