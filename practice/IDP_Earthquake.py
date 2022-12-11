a = int(input('Enter a:'))
b = int(input('Enter b:'))
c =[a,b]
if a ==max(c):
    diff = a-b
    mag = a**diff - b
    eq_mag = mag**2
else:
    diff = b-a
    mag = b ** diff -a
    eq_mag = mag ** 2
print(mag)
print(eq_mag)

