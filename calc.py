op = -1
while op != 5:
    print ("Welcome to CalculatorGPT")
    print (") Add")
    print ("2) Subtract")
    print ("3) Multiply")
    print ("4) Divide")
    print ("5) Quit")
    try:
        op = input("Choose an operation")
        op = int(op)
        if op == 5:
            print("Okay. Bye!")
            continue
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        op = -1
    if op == 1:
        print(str(num1)+"+"+str(num2)+"="+str(num1+num2))
    elif op == 2:
        print(str(num1)+"-"+str(num2)+"="+str(num1-num2))
    elif op == 3:
        print(str(num1)+"x"+str(num2)+"="+str(num1*num2))
    elif op == 4:
        print(str(num1)+"÷"+str(num2)+"="+str(num1/num2))
    else: 
        print("Sorry. I don't understand!")
