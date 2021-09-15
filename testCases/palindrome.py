n = int(input("Enter number:"))
print("Input Integer:",n)
temp = n
r = 0
while n>0:
	r = r*10 + n%10
	n = n//10
print("Reversed Integer:",r)
if temp == r:
   print("palindrome")
else :
   print("not Palindrome")

s=input("Enter String:")
if s[::-1] == s:
   print("palindrome")
else :
   print("not Palindrome")
