# Ejemplo Return + Function

print("\n######## EJEMPLO 6 ########\n")

def calculator (number1, number2, basics = "False"):

    number1= int(input("What is the number1? "))
    number2= int(input("What is the number2? "))
    basics= input("Do you want only the basics operations? Write True or False ")

    addition = number1 + number2
    substaction = number1 - number2
    multi = number1*number2
    division = number1/number2
    chain = ""

    if basics == "True" or "true":
        chain += "Addition: " + str(addition)
        chain += "\n"
        chain += "Substraction: " + str(substaction)
        chain += "\n"

    else:
        chain += "Multi: " + str(multi)
        chain += "\n"
        chain += "Division: " +str(division)
        chain += "\n"
        
    print(basics)
    print(type(basics))

    return chain


print(calculator(2,5,))

    
