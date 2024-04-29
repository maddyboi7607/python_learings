a=input("Enter the word:")
l=len(a)
if l%2 == 0:
    t = l//2
    for i in range(1,l+1):
        print(i*t)
else:
    for i in range(1,l+1):
        print(i*l)
