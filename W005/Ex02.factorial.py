def factotrial(n):
  sum=1
  if n==0:
    return 1
  elif n>0:
    for i in range(n):
      sum=sum*(i+1)
    return sum
a=factotrial(5)
print(a)

