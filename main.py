import sympy as sm
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot

x = sm.Symbol('x')
def task1(X, Y):
    L = 0
    n = len(X)
    for i in range(n):
        P = 1
        for j in range(n):
            if(i != j):
                P *= (x-X[j])/(X[i]-X[j])
        L += P*Y[i]
    return L

X = np.array([0.68, 0.73, 0.80, 0.88, 0.93, 0.99])
Y = np.array([0.80866, 0.89492, 1.02964, 1.20966, 1.34087, 1.52368])

F = task1(X, Y)
print("X = ", X, "\n")
print("Y = ", Y, "\n")
print("F = ", F, "\n")

print(sm.expand(F), "\n")


def plot_function(func, a, b, dx, dy):
    # Находим значения переменных на интервалах на осях OX и OY
    domain_x = np.arange(a, b, 0.001)  # с интервалом 0.001 находим значения X
    image = [func.subs(x, value) for value in domain_x]  # подставляем значения X в выражение, чтобы найти Y

    # Строим заданный график

    fig = plt.figure(figsize=(14, 10))  # задаем размер области графика
    plt.plot(domain_x, image, color='MediumSlateBlue')  # Строим заданный график

    plt.xticks(np.arange(a, b + dx, dx))  # подписываем значения на оси X
    a_y, b_y = float(func.subs(x, a).evalf(3)), float(
        func.subs(x, b).evalf(3))  # находим предельные значения для оси OY
    plt.yticks(np.arange(a_y, b_y, dy))  # подписываем значения на оси y

    plt.text(b + dx, a_y - 3 * dy, "X", fontsize=14)  # Добавляем подпись к оси OX
    plt.text(a - 3 * dy, b_y + dy, "Y", fontsize=14)  # Добавляем подпись к оси OY

    plt.grid()  # добавляем сетку
    plt.show()  # выводим график


# plot_function(F, a, b, dx, dy) F-ф-ция графика, a,b - диапазон значений на оси OX, dx,dy-точность разметки на осях OX,OY,
#plot_function(F, 0, 0.33, 0.02, 0.015)  # рисуем график на заданном на оси OX диапазоне
#plot_function(F, 0.10, 0.212, 0.007, 0.005)  # график для значений функции, в которых ее надо найти


X1 = np.array([0.89, 0.81, 0.77, 0.95, 0.71])
length = len(X1)
for i in range(length):
    print("F[", X1[i], "] = ", F.subs(x, X1[i]), "\n")

# Проверка
# подставим исходные значения
f = np.array([0.02,0.08,0.12,0.17,0.23,0.30])
length = len(f)
for i in range(length):
    print("F[", f[i],"] = ", F.subs(x, f[i]), "\n") #вычисляем значение функции

print(Y)