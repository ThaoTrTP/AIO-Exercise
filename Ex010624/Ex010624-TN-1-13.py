#Cau 1
import math
def calc_f1_score (tp, fp, fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    return f1_score

print(round(calc_f1_score(2, 4, 5), 2))

#Cau 2
import math
def is_numberic (n):
    try:
        float(n)
    except ValueError:
        return False
    return True

print(is_numberic(10))
print(is_numberic('n'))

#Cau3: ReLU

#Cau 4
import math
def cal_sig(x):
    result = 1/(math.e**-x+1)
    return result

print(round(cal_sig(2), 2))

#Cau 5
import math
def cal_elu(x):
    if x <= 0:
        result = 0.01*(math.e**x-1)
    else:
        result = x
    return result

print(round(cal_elu(-1), 2))

#Cau 6: 0.95
#Cau 7:
def abs_error (y, y_hat):
    result = abs(y-y_hat)
    return result

print('cau 7:', abs_error(2, 9))

#Cau 8
def squared_error(y, y_hat):
    result  = (y-y_hat)**2
    return result

print (f'cau 8: {squared_error(2,1)}')

#Cau 9
def factorial (x):
    result = 1
    for i in range (1, x+1):
        result = result * i
    return result

def approx_cos(x, n):
    cos = 0
    for i in range(n+1):
        cos = (-1)**i * (x**(2*i)/factorial(2*i))
        cos += cos
    return cos

print(f'cau 9: {round(approx_cos(3.14, 10), 2)}')
