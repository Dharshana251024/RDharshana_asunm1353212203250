n=int(input("Enter the number:"))
fact=1
count=2
if n==0:
  print("Factorial 0 is 1")
if n>0:
  while(count<=n):
    fact=fact*count
    count=count+1
print("The factorial of the given number",fact)