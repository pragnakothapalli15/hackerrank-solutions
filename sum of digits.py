#sum of digits of a number
n=int(input("enter a number")
sum_digits=0

while n>0:
   sum_digits += n%10
   n//=10

print(sum_digits)
