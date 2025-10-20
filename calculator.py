def add(a,b):
    return a+b

def substraction(a,b):
    return a-b

#Main loop
while (True):

    print("==== Operations ====\n1.Addition (+)\n2.Substration (-)\n3.Terminate (#)\n")
    operation = input("Enter operation : ")

    if (operation=="#"):
        break
    
    a = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))
    
    result = 0
    
    if (operation=="+"):
        result=add(a,b)

    elif (operation=="-"):
        result=substraction(a,b)
    
    else:
        print("Invalid operation. Enter again.\n")

    print(result,"\n")