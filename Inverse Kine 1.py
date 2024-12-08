from math import *
l1 = 2
l2 = 1

x = 1
y = 1
l3 = (x**2 + y**2) ** 0.5

beta = acos(l3**2 - l1**2 - l2**2)/(-l1 * l2)

q2 = pi - beta

alpha = atan(y,x)

theta = asin(sin(beta) / l3 * l2)

q1 = alpha - theta
