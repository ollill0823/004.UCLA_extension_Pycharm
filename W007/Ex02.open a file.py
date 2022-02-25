
def safe_open(filename, mode):
    try:
        openfile=open(filename, mode)
        return openfile
    except:
        return None

safe_open('test2.txt', 'r')