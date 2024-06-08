#is_number function: kiem tra x co hop le khong
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

#Check activation function name
def check_activation_function_name(function_name):
    if function_name == 'sigmoid' or function_name == 'relu' or function_name == 'elu':
        return True
    else:
        return False
    
#Activation function (sigmoid, relu, elu)
def activate(x, activation_function):
    import math
    print (f'Input x = {x}')
    print (f'Input activate Function (sigmoid|relu|elu): {activation_function}')
    if is_number(x) != True:
        print ('x must be a number')
        return
    if check_activation_function_name(activation_function) == False:
        print ('ten_function_user is not  supported')
        return
    converted_x = float (x)
    if activation_function == 'relu':
        if converted_x >0:
            result = converted_x
        else:
            result = 0
        return print(f'{activation_function} f({x}) = {result}')
    if activation_function == 'sigmoid':
        result = 1 / (1 + math.e**(-converted_x))
        return print(f'{activation_function} f({x}) = {result}')
    if activation_function == 'elu':
        alpha = 0.01
        if converted_x > 0:
            result = converted_x
        else:
            result = alpha*(math.e**converted_x-1)
        return print(f'{activation_function} f({x}) = {result}')
    
#Example
activate(1.5, 'sigmoid')
activate(-3, 'elu')
activate(2, 'belu')
    

    