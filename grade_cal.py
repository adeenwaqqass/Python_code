# Program to take in the marks of 5 subjects and display the grade.

a = (int(input("Enter marks scored in English:")))
b = (int(input("Enter marks scored in Maths:")))
c = (int(input("Enter marks scored in science:")))
d = (int(input("Enter marks scored in History:")))
e = (int(input("Enter marks scored in Geography:")))

x = (a+b+c+d+e)/500*100

print(x)

if(x>=90):
    print("Grade 'A'")
elif(x>=60):
    print("Grade 'B'")
elif(x>=30):
    print("Grade 'C'")         
else:
    (x>=20)
    print("Grade 'C'")