a = 1
b = int(input("Enter your term:"))
c = 0
d = 0
for i in range(0 , b):
    d = a + c
    c = a
    a = d

print(a)