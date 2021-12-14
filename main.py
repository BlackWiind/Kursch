import math
from array import array
from math import cos

a = 0
b = 3
h = 1
iterations = 0
accurcity = 0.0001
y1 = []
y2 = []
x1 = []
xIp = []
n = 1


def horde(_a, _b):
    return _a - function(_a) * (_b - _a) / (function(_b) - function(_a))


def function(_x):
    return 3 * (_x ** 4) - 8 * (_x ** 3) - 18 * (_x ** 2) + 2


def function1(_x):
    return 12 * (_x ** 3) - 24 * (_x ** 2) - 36 * _x


def function_rc(_x, _y):
    return (6 - (_y ** 2)) * cos(_x) + 2 * _y


def runge_Cutt_4(_x, _y, _h):
    k1 = function_rc(_x, _y)
    k2 = function_rc(_x + _h / 2, _y + _h / 2 * k1)
    k3 = function_rc(_x + _h / 2, _y + _h / 2 * k2)
    k4 = function_rc(_x + h, _y + h * k3)
    return _y + _h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def rC_calc(_h):
    global n
    x2 = 0
    x1.append(0)
    y1.append(answer)
    y2.append(answer)
    while x1[-1] < 1:
        y1.append(runge_Cutt_4(x1[-1], y1[-1], _h))
        x1.append(x1[-1] + _h)
    while x2 <= 1:
        y2.append(runge_Cutt_4(x2, y2[-1], _h / 2))
        x2 += (_h / 2)
    for values in range(1, len(y1)):
        if abs(y1[values] - y2[values * 2]) < 0.0001 * 15:
            for index in range(len(y1)):
                print("x = ", x1[index], "\ty = ", round(y1[index], 4))
            return
    _h /= 2
    n *= 2
    y1.clear()
    y2.clear()
    x1.clear()
    rC_calc(_h)


def interpolation(x: array, y: array, xIp: array, n: int, nIp: int) -> array:
    arr = []
    h = x[1] - x[0]
    for i in range(nIp):
        j = 0
        while j < n and x[j] <= xIp[i]:
            #print(i,'\t',j,'\t',n,'\t',x[j],'\t',xIp[i])
            j += 1
        j -= 1
        q = (xIp[i] - x[j]) / h
        arr.append(y[j] + q * (y[j + 1] - y[j]))
    return arr


while True:
    iterations += 1
    answer = horde(a, b)
    if function(a) * function1(a) > 0:
        b = answer
    else:
        a = answer
    if function(answer) <= accurcity:
        break
rC_calc(h)
nIp = math.trunc((1 - 0) / 0.1)
xIp = [0 + 0.1 * i for i in range(1, nIp)]
[print(value) for value in xIp]
interpol_arr = interpolation(x1, y1, xIp, n, nIp)

print("\ta = ", a)
print("\tb = ", b)
print("\tanswer = ", answer)
print("\titerations = ", iterations)
