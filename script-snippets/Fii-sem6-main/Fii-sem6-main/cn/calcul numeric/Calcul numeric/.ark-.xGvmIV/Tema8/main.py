import random
import math


def F(x):
    return (1 / 3) * x ** 3 - 2 * x ** 2 + 2 * x + 3


def G(x):
    return x ** 2 + math.sin(x)


def H(x):
    return x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4


def secanta(min, max, epsilon, k_max, F):
    G_1 = lambda x, h: (3 * F(x) - 4 * F(x - h) + F(x - 2 * h)) / (2 * h)
    x = random.uniform(min, max)
    x0 = random.uniform(min, max)
    h = 10.0 ** (-5)
    y = G_1(x, h)
    y0 = G_1(x0, h)

    k = 0
    dx = 0
    while True:
        dx = ((x - x0) * y) / (y - y0)
        if abs(y - y0) <= epsilon:
            if abs(y) <= epsilon / 100:
                dx = 0
            else:
                dx = 10.0 ** (-5)
        x0 = x
        y0 = y
        x = x - dx
        y = G_1(x, h)
        if abs(dx) < epsilon or k > k_max or abs(dx) > 10 * 8:
            break
    F_2 = lambda x, h: (-F(x + 2 * h) + 16 * F(x + h) - 30 * F(x) + 16 * F(x - h) - F(x - 2 * h)) / (12 * (h ** 2))
    if abs(dx) < epsilon < F_2(x, h):
        return x, F_2
    else:
        return None, "Functia este divergenta"


f_min, second_der = secanta(1, 7, 10.0 ** (-4), 1000, F)
print("Punctul de minim: ", f_min)
print("Derivata de ordinul 2: ", second_der(f_min, 10.0 ** (-5)))
