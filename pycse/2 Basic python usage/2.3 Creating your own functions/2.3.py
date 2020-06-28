import numpy as np


# function x^3 - log(x) with x = 3
x = 3
print(x ** 3 - np.log(x))

# defining function as f(x)
def f(x):
    return (x ** 3 - np.log(x))

print(f(3))
print(f(5.1))