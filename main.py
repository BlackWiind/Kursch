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


def horde(local_a, local_b) -> float:
    return local_a - math_function(local_a) * (local_b - local_a) / (math_function(local_b) - math_function(local_a))


def math_function(local_x) -> float:
    return 3 * (local_x ** 4) - 8 * (local_x ** 3) - 18 * (local_x ** 2) + 2


def math_function1(local_x) -> float:
    return 12 * (local_x ** 3) - 24 * (local_x ** 2) - 36 * local_x


def function_rc(local_x, local_y) -> float:
    return (6 - (local_y ** 2)) * cos(local_x) + 2 * local_y


def runge_Cutt_4(local_x, local_y, local_h) -> float:
    k1 = function_rc(local_x, local_y)
    k2 = function_rc(local_x + local_h / 2, local_y + local_h / 2 * k1)
    k3 = function_rc(local_x + local_h / 2, local_y + local_h / 2 * k2)
    k4 = function_rc(local_x + h, local_y + h * k3)
    return local_y + local_h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def rC_calc(local_h) -> float:
    global n
    x2 = 0
    x1.append(0)
    y1.append(answer)
    y2.append(answer)
    while x1[-1] < 1:
        y1.append(runge_Cutt_4(x1[-1], y1[-1], local_h))
        x1.append(x1[-1] + local_h)
    while x2 <= 1:
        y2.append(runge_Cutt_4(x2, y2[-1], local_h / 2))
        x2 += (local_h / 2)
    for values in range(1, len(y1)):
        if abs(y1[values] - y2[values * 2]) < 0.0001 * 15:
            for index in range(len(y1)):
                print("x = ", x1[index], "\ty = ", round(y1[index], 4))
            return
    local_h /= 2
    n *= 2
    y1.clear()
    y2.clear()
    x1.clear()
    rC_calc(local_h)


def interpolation(local_x: array, local_y: array, local_xIp: array, local_n: int, local_nIp: int) -> array:
    arr = []
    h = local_x[1] - local_x[0]
    for i in range(local_nIp):
        j = 0
        while j <= local_n or local_x[j] <= local_xIp[i]:
            # print(i,'\t',j,'\t',n,'\t',x[j],'\t',xIp[i])
            j += 1
        j -= 1
        q = (local_xIp[i] - local_x[j]) / h
        arr.append(local_y[j] + q * (local_y[j + 1] - local_y[j]))
    return arr


while True:
    iterations += 1
    answer = horde(a, b)
    if math_function(a) * math_function1(a) > 0:
        b = answer
    else:
        a = answer
    if math_function(answer) <= accurcity:
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
