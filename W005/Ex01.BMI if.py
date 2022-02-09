def myBMI(a, b):
  bmi= a*703/(b**2)
  if bmi<18.5:
    return 'Underweight'
  elif 18.5<=bmi<25:
    return 'Normal'
  else:
    return 'Overweight'

weight=eval(input('Enter your weight: '))
height=eval(input('Enter your height: '))

a=myBMI(weight, height)
print(a)

