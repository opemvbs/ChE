import numpy as np

def f(x):
    # return the inverse square of x.
    x = np.array(x)
    return (1.0 / (x ** 2))

print(f(3)) # 0.1111111111111111
print(f([4, 5])) # [0.0625 0.04  ]


def func(x, y):
    # return product of x and y
    return x * y

print(func(2, 3)) # 6
print(func(np.array([2, 3]), np.array([3, 4]))) # [ 6 12]




from scipy.integrate import quad

print(quad(lambda x:x ** 3, 0, 2)) # (4.0, 4.440892098500626e-14)


def wrapper(x):
    a = 4
    def func(x, a):
        return a * x
    
    return func(x, a)

print(wrapper(4)) # 16


def func(x, a):
    return a * x

def wrapper(x):
    a = 4
    return func(x, a)

print(wrapper(4)) # 16




from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

k = 2.2
def myOde(y, t):
    # Ordinary differential equation defining
    # exponential growth.
    return k * y

y0 = 3
tSpan = np.linspace(0, 1)
y = odeint(myOde, y0, tSpan)

plt.plot(tSpan, y)
plt.xlabel('Time')
plt.ylabel('y')
plt.grid(True)
plt.savefig('pycse/2 Basic python usage/2.4 Defining functions in python/funcs-ode.png')