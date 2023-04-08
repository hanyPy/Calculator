'''
The determinant and inverse of a 3x3 matrix.
Written between 26th-27th February, 2023.
Last edit on 7th April, 2023.
'''
det= ()
def matrix(det):
    try:   
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        num3 = float(input("Enter a number: "))
        num4 = float(input("Enter a number: "))
        num5 = float(input("Enter a number: "))
        num6 = float(input("Enter a number: "))
        num7 = float(input("Enter a number: "))
        num8 = float(input("Enter a number: "))
        num9 = float(input("Enter a number: "))
    except TypeError  as e:
                print(e)
                print('You entered a string, please re-rerun the program')
    except ValueError  as a:
                print(a)
                print('You entered a string, please re-rerun the program')
                
    #finding and printing the determinant.    
    det = ((num1)*(((num5)*(num9))-((num8)*(num6)))) - ((num2)*(((num4)*(num9))- ((num7)*(num6)))) + ((num3)*(((num4)*(num8)) - ((num7)*(num5))))
    print("\nThe determinant is " + str(det) + ".\n")
    
    c11 = (pow(-1, 2))*((num5)*(num9)-(num8)*(num6))
    c12 = (pow(-1, 3))*((num4)*(num9)-(num7)*(num6))
    c13 = (pow(-1, 4))*((num4)*(num8)-(num7)*(num5))
    c21 = (pow(-1, 3))*((num2)*(num9)-(num8)*(num3))
    c22 = (pow(-1, 4))*((num1)*(num9)-(num7)*(num3))
    c23 = (pow(-1, 5))*((num1)*(num8)-(num7)*(num2))
    c31 = (pow(-1, 4))*((num2)*(num6)-(num5)*(num3))
    c32 = (pow(-1, 5))*((num1)*(num6)-(num4)*(num3))
    c33 = (pow(-1, 6))*((num1)*(num5)-(num4)*(num2))
        
    try:
        num1 = c11/det
        num4 = c21/det
        num7 = c31/det
        num2 = c12/det
        num5 = c22/det
        num8 = c32/det
        num3 = c13/det
        num6 = c23/det
        num9 = c33/det
            
     # Just incase the determinant is 0.
    except ZeroDivisionError:
        print("Since the determinant is 0, dividing the numbers isn't possible. But anyway, this is their disjoint order.")
            
    Inverse1 =  [num1 , num4 , num7]
    Inverse2 = [num2 , num5 , num8]
    Inverse3 = [num3 , num6 , num9]
    print(Inverse1)
    print(Inverse2)
    print(Inverse3)

matrix(det)
