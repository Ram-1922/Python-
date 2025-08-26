# A Basic Calculator

operator=input("Operator:")
num1=float(input("Enter Num1:"))
num2=float(input("Enter Num2:"))
result=0
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=="/":
    result=num1/num2
elif operator=="**":
    result=pow(num1,num2)
else:
    result = "Invalid"
    print("INVALID OPERATOR!!!")
print(f"The result for given operator {operator} is {result}.")