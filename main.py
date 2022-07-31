import math
from array import array
from math import cos

horde_a = 0
horde_b = 3
a = 0
b = 1
h = 1
iterations = 0
accuracy = 0.001
y1 = []
y2 = []
x1 = []
xIp = []
n = 1


# вычисление корня методом хорд
def horde(local_a: float, local_b: float) -> float:
    return local_a - math_function(local_a) * (local_b - local_a) / (math_function(local_b) - math_function(local_a))


# функция f(x)
def math_function(local_x: float) -> float:
    return 3 * (local_x ** 4) - 8 * (local_x ** 3) - 18 * (local_x ** 2) + 2


# производная f'(x)
def math_function1(local_x: float) -> float:
    return 12 * (local_x ** 3) - 24 * (local_x ** 2) - 36 * local_x


# Производная функции в точке x,y
def function_rc(local_x: float, local_y: float) -> float:
    return (6 - (local_y ** 2)) * cos(local_x) + 2 * local_y


# метод Рунге-Кутта четвертого порядка
def runge_Cutt_4(local_x: float, local_y: float, local_h: float) -> float:
    k1 = function_rc(local_x, local_y)
    k2 = function_rc(local_x + local_h / 2, local_y + local_h / 2 * k1)
    k3 = function_rc(local_x + local_h / 2, local_y + local_h / 2 * k2)
    k4 = function_rc(local_x + h, local_y + h * k3)
    return local_y + local_h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


# Решение уравнения методом Рунге-Кутта четвертого порядка
def rC_calc(local_h: float) -> float:
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
            return
    local_h /= 2
    n *= 2
    y1.clear()
    y2.clear()
    x1.clear()
    rC_calc(local_h)


# значения функции с помощью линейной интерполяции
def interpolation(local_x: array, local_y: array, local_xIp: array, local_n: int, local_nIp: int) -> array:
    arr = []
    h = local_x[1] - local_x[0]
    for i in range(local_nIp):
        j = 0
        while j < local_n and local_x[j] <= local_xIp[i]:
            j += 1
        j -= 1
        q = (local_xIp[i] - local_x[j]) / h
        arr.append(round(local_y[j] + q * (local_y[j + 1] - local_y[j]), 4))
    return arr


# интеграл по формуле трапеции
def heat(local_y: array, local_n: int) -> float:
    h = (b - a) / local_n
    summa = 0
    for i in range(1, local_n):
        summa += local_y[i]
    return h * ((local_y[0] + local_y[local_n]) / 2 + summa)


while True:
    iterations += 1
    answer = horde(horde_a, horde_b)
    if math_function(horde_a) * math_function1(horde_a) > 0:
        horde_b = answer
    else:
        horde_a = answer
    if math_function(answer) <= accuracy:
        break
rC_calc(h)
nIp = math.trunc((b - a) / 0.1 + 1)
xIp = [0 + 0.1 * i for i in range(nIp)]
interpol_arr = interpolation(x1, y1, xIp, n, nIp)

print(f"\tПриблежённое значение к {round(answer, 4)}, количество итераций: {iterations}")
print("\n\tРешение дифференциального уравнения на интервале [0;1] \n\tc заданной точностью"
      " (интервал уменшен с [0;2],\n\tт.к. решение метедом Рунге-Кутта получает "
      "слишком \n\tбольшие значения из-за функции заданной y^2.):")
[print("\tx = ", x1[index], "\ty = ", round(y1[index], 4)) for index in range(len(x1))]
print("\n\t Результаты интерполяции:")
[print(f"\tx = {round(xIp[i], 1)}\ty = {interpol_arr[i]}") for i in range(len(xIp))]
interpol_arr = [value ** 2 for value in interpol_arr]
print(f"\n\tКоличество теплоты = {round(heat(interpol_arr, nIp - 1), 4)}")
