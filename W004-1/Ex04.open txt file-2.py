<<<<<<< HEAD
def words(filename):
    filename= open(filename, 'r', encoding="utf-8")
    f = filename.read()
    specialchars = '.,-!:'
    for c in specialchars:
        f = f.replace(c, ' ')   ## 一定要f=f.replace 要重複


    return f


a=words('i-have-a-dream.txt')
print(a)

=======
with open ('i-have-a-dream.txt', 'r', encoding="utf-8") as f:
    article=f.read()
    split=article.split()

print(split)


>>>>>>> origin/main

