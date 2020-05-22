def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n-r)))


while True:
    
    print("""enter operators
      + for addition
      - for subtraction
      / for division
      * for multiplication
      r for root
      ^ to raise a number
      %" for modulus
      ! for factoriol
      nCr for combinations
      sin to find the sine of a number
      cos to find the cosine of a number
      tan to find the tangent of a number
      pie 
      e to find the exponent of a number
      ln to get the log of a number
      """)
    from math import sin, cos, pi, e, tan, log
    from itertools import permutations, combinations
    new_input = input(" ")

    if new_input == "+":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "+", second_number, "=", first_number + second_number )
        break
    elif new_input == "-":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "-", second_number, "=", first_number - second_number)
        break
    elif new_input == "/":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "/", second_number, "=", first_number / second_number)
        break
    elif new_input == "*":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "*", second_number, "=", first_number * second_number)
        break
    elif new_input == "%":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "%", second_number, "=", first_number % second_number)
        break
    elif new_input == "^":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print( first_number, "^", second_number, "=", first_number ** second_number)
        break
    elif new_input == "r":
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter the second number: "))
        print(first_number, "root", second_number, "=", second_number ** (1 / first_number))
        break
    elif new_input == "!":
        number = int(input("enter your number: "))
        fact = 1
        if number < 0:
            print("no factoriols for negative numbers")
            break
        elif number == 0:
            print("The factoriol of 0 is 1")
            break
        else:
            for i in range (1,number + 1):
                fact = fact * i
                print("the factoriol of" +number+ "is" +fact+ ".")
    elif new_input == "nCr":
        n = int(input("enter your first number: "))
        r = int(input("enter the second number: "))
        print(int(nCr(r, n))) 
        break
    elif new_input == "sin":
        number = int(input("enter your number: "))
        print("sin(", number, ")=", sin(number))
        break
    elif new_input  == "cos":
        number = int(input("enter your number: ")) 
        print("cos(", number, ")=", cos(number))
        break
    elif new_input == "tan":
        number = int(input("enter your number: "))
        print("tan(", number, ")=", tan(number))
        break   
    elif new_input == "pie":
        number = int(input("enter your number: "))
        print("pie {}".format, pi * number)
        break
    elif new_input == "e":
        number = int(input("enter your number: "))
        print( "exponential is", e * number )
        break
    elif new_input == "ln":
        number = int(input("enter your number: "))
        print("ln(", number, ")=", log(number))
        break
    else:
        print("wrong operator")  