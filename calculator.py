num1 = int(input("Enter the first value: "))
num2 = int(input("enter the second value: "))

Opr = input("enter the operation: ")

if Opr == "+":
    print (num1 + num2)
elif Opr =="-":
    print(num1-num2)
elif Opr == "*":
    print(num1*num2)
elif Opr == "/":
    print(num1//num2)

else:
    print("Unexpected operator")
