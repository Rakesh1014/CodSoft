a = int(input("enter a number"))
b = int(input("enter a number"))
print("Enter your choice")
print('1.Addition\n2.subtraction\n3.Multiplication\n4.Division\n5.Modulus')
ch = int(input())
if(ch == 1):
    print("sum is ",a+b)
elif (ch == 2):
    print("subtraction : ",a-b)
elif(ch == 3):
    print('product:',a*b)
elif(ch == 4):
    print('div :',a/b)
elif(ch == 5):
    print('Mod:',a%b)
else:
    print('Invalid choice')