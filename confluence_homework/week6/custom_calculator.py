def calculate(*args, operation):
    if not args:
        return 0
    else:
        if operation == '+':
            result = 0
            for arg in args:
                result += arg
            return result
        if operation == '*':
            result = 1
            for arg in args:
                result *= arg
            return result
        if operation == '/':
            result = args[0]
            for arg in args[1:]:
                if arg == 0:
                    print("Division by 0")
                    return None
                result /= arg
            return result
        if operation == '-':
            result = args[0]
            for arg in args[1:]:
                result -= arg
            return result
        
print(calculate(2, 3, 4, operation='*'))
print(calculate(10, 0, operation='/'))
print(calculate(operation='-'))
            
