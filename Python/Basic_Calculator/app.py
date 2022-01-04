def calculate(num1, operation, num2): 
    operators = ['+','-','/','//','*','%']
    
    
    if operation not in operators:
        return None
    try:
        return eval(str(num1)+operation+str(num2))
    except ZeroDivisionError:
        return None