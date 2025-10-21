def add(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

#Main loop
while (True):

    print("\n==== Operations ====")
    print("Addition (+)")
    print("Substraction (-)")
    print("Multiplication (*)")
    print("Multiplication (/)")
    print("Terminate (#)")
    operation = input("Enter operation : ")

    if (operation=="#"):
        break

    num1 = int(input("\nEnter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    
    result = 0
    
    if (operation=="+"):
        result=add(num1,num2)

    elif (operation=="-"):
        result=substraction(num1,num2)

    elif (operation=="*"):
        result=multiply(num1,num2)

    elif (operation=="/"):
        result=division(num1,num2)
    
    else:
        print("Invalid number. Enter again.\n")

    print(f"{num1} {operation} {num2} = {result} \n")