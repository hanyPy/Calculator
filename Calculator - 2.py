#18th february 2023

from math import*

#variables
num1 = float(input("Enter a number here to calculate: "))
method = input("How do you want to calculate the numbers?\nChoose from + , - , / , * , ^ , pi , abs , sqrt:  ")
num2 = float(input("Enter another number here: "))

result = float(num1+num2)  
if method=="+":
    print(str(num1) +"+"+str(num2)+" = " + str(result))
result = float(num1*num2)
if method =="*":
    print(str(num1) +" x "+str(num2)+" = " + str(result))
result = float(num1-num2)
if method=="-":
    print(str(num1) +"-"+str(num2)+" = " + str(result))
result = float(num1/num2)
if method=="/":
    print(str(num1) +"/"+str(num2)+" = " + str(result))

result = int(pow(num1, num2))
if method == "^":
    print(str(num1) +"^"+str(num2)+" = " + str(result))
result = float(num1 *3.1415929 )
if method == "pi":
    print(float(num1) * float(3.1415929))
if method == "abs":
    print(abs(float(num1)))
if method == "sqrt":
    print(sqrt(num1))