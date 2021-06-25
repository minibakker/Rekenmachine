print("choose an operation")
print ("1:+")
print ("2:-")
print ("3:/")
print ("4:*")
operation = input()
if operation == "1":
    num1 = input("add the first number:")
    num2 = input("add the second number")
    num12= float(num1) + float(num2)
    print("Answer: " , num12 )
elif operation == "2":
    num1 = input("add the first number:")
    num2 = input("add the second number")
    num12 = float(num1) - float(num2)
    print("Answer: ", num12)
elif operation == "3":
    num1 = input("add the first number:")
    num2 = input("add the second number")
    num12 = float(num1) / float(num2)
    print("Answer: ", num12)
elif operation == "4":
    num1 = input("add the first number:")
    num2 = input("add the second number")
    num12 = float(num1) * float(num2)
    print("Answer: ", num12)
else:
    print("error: invalid number")