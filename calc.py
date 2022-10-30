def calculator(operator):
    num1 = int(input("Enter number1 value\n"))
    num2 = int(input("Enter number2 value\n"))
    match operator:
        case '+':
            print("The sum is ",num1+num2)
        case '-':
            print("The difference is", num2-num1)
        case '*':
            print("The product is", num1*num2)
        case default:
            print("something")
  
if __name__ == "__main__":
    operator = input("Enter the value of the operator\n")
    calculator(operator)
