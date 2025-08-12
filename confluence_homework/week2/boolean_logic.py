def eval_bool(x, y, z):
    if x > 0 and y > 0 and z > 0:
        print('All numbers greater than zero')
    elif x == y or x == z or y == z:
        print('At least one number is equal to another')
    elif x >= 0 and y >= 0 and z >= 0:
        print('None of the numbers are negative')
    else:
        print('Nothing')
        
eval_bool(5, 0, -3)