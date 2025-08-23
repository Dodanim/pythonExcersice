#Calculator just for fun, two numbers


def sum_numbers(number1, number2):
    result = number1 + number2
    return result

def subs(number1, number2):
    result = number1 - number2
    return result

def multiplication(number1, number2):
    result = number1 * number2
    return result

def division(number1, number2):
    if(number1 != 0 and number2 != 0):
        result = number1 / number2
    else:
        result = "operation no valid"
    return result

print("Select a choice \n1.Sum \n2.Substraction \n3.multiplication \n4.division")
nOperation = int(input("write the number of the operation you want to do: "))

number1 = float(input("first number: "))
number2 = float(input("second number: "))

if (nOperation == 1):
   print(sum_numbers(number1, number2))
elif(nOperation == 2):
    print(subs(number1, number2))
elif(nOperation == 3):
    print(multiplication(number1, number2))
elif(nOperation == 4):
    print(division(number1, number2))
else :
 print("This option is not in the menu")


