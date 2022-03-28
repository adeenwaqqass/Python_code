# program to chech numbers divisible by a given number in range

a = (int(input("Enter a number to get its divisibles : ")))

x = (int(input("from : ")))
y = (int (input("upto : ")))

for i in range(x,y+1):
    if i%a==0:
        print(i)