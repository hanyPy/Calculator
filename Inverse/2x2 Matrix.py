# The inverse of a 2x2 matrix
# 3rd March 2023

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))

# finding the determinant  (ad-bc)
det = ((num1*num4) - (num2*num3))

print("The determinant is: " + str(det))

c11 = num1/det
c12 = num2/det
c21 = num3/det
c22 = num4/det

#We switch c11 and c22 , and multiply c21 and c12 with -1

Inverse=  [c22 , -c12]
inverse2= [-c21 , c11]
print(Inverse)
print(inverse2)