badfile=True
while badfile:
    try:
        filename=input('Enter a filename: ')
        openfile= open(filename)
        badfile=False
    except:
        print('This file does not exist, please re-key a new one: ')
        badfile=True