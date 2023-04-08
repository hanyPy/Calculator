'''
The determinant and inverse of a 2x2 matrix.
Written on 3rd March, 2023.
Last edit on 7th April, 2023.
'''

det= ()
def matrix(det):
    try:   
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        num3 = float(input("Enter a number: "))
        num4 = float(input("Enter a number: "))
    except TypeError  as e:
                print(e)
                print('You entered a string, please re-rerun the program')
    except ValueError  as a:
                print(a)
                print('You entered a string, please re-rerun the program')
                
    #finding and printing the determinant.    
    det = ((num1*num4) - (num2*num3))
    print("\nThe determinant is " + str(det) + ".\n")
      
    try:
        c11 = num1/det
        c12 = num2/det
        c21 = num3/det
        c22 = num4/det
        
    # Just incase the determinant is 0.
    except ZeroDivisionError:
        print("Since the determinant is 0, dividing the numbers isn't possible. But anyway, this is their disjoint order.")
        Ifzero1 = [num4, -num2]
        Ifzero2 = [-num3, num1]
        print(Ifzero1)
        print(Ifzero2)
        
    #We switch c11 and c22 , and multiply c21 and c12 with -1
    try:
        Inverse1 = [c22, -c12]
        Inverse2 = [-c21, c11]
        print(Inverse1)
        print(Inverse2)
    except:
        pass

matrix(det)
