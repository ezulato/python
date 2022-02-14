# Write a Python code to reverse the given integer and print the integer

num = int(input("enter a number  : "))
rev = 0
while num > 0:
  print ("-----------------------------------")
  remainder = num % 10  # Finding the remainder
  print ("remainder :")
  print (remainder)
  rev = (rev*10) + remainder
  print ("rev : %d " %rev)

  print ("num  :")
  num = num//10  # Finding the quotient
  print ("num//10 :")
  print (num)
print("ET VOILA' -----> %d " %rev)
