# 8.5's 5 means overal number count is five (not include the decimanl number)
#8.5f's 5 means five digits numbers after the decimal number

print('{:8.5}'.format(1000/3))
print('{:8.6}'.format(1000/3))
print('{:10.6}'.format(1000/3))



print('{:8.5}'.format('phanalge'))
print('{:10.6}'.format('phanalge'))
print('{:-<10.6}'.format('phanalge'))


print('{:11.5f}'.format(1000/3))
print('{:011.5f}'.format(1000/3))
print('{:e}'.format(1000/3))
