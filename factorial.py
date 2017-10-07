a=int(input('enter your number='))
fact=1
if a==0:
  print("sorry your number does not exist")
elif a==1:
  print(1)
else:
  for i in range(1,a+1):
    fact=fact*i
  print('factorial of number is  ',fact)
