# Program to Calculate the Average of Numbers in a Given List.

x = int(input("Enter Numbers for calculating average"))
y = []

for i in range(0,x):
    elem = int(input("enter elements"))
    y.append(elem)
avg = sum(y)/x
print("Avrage elements",round(avg,2))
