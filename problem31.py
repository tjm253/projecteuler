# Problem 31
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many ways can £2 be made using any number of coins?
# ---
# Solution method:
# in other words find the solution to
# A + 2B + 5C + 10D + 20E + 50F + 100G + 200H = 200
# where {A, B, C, D, E, F, G, H} are whole numbers

import numpy as np

Lst_val = [1, 2, 5, 10, 20, 50, 100, 200]  # values of coins
Lst_max = [200, 100, 40, 20, 10, 4, 2, 1]  # the max count of each coin

# for 200 p, there is one solution
# A = [200, 100

# F(x) = Sum from k = 0, inf (c_k * X^m)
# c is the coefficient, x is ?

## ------ F1 ------
# - what would the problem look like with 1p
# F1(x) = Sum from k = 0, inf (c_k * X^m)
# = sum from k = 0 to inf (1 * x^2) = 1 + x + x^2 + ... + x^n = 1 / (1 - x)

## ------ F2 ------
# how many ways to have [0p, 1p, 2p, 3p, 4p] with 2p coins (the power expresses the amount)
# 2, 4, 6, 8, 10, 12, ...
# F2(x) = (1 * x^0) + (0 * x^1) + (1 * x^2) + (0 * x^3) + (1 * x^4) + (0 * x^5)...
# F2(x) = 1 / (2 * (1 - x))
# F2(x) = sum k=0 to inf [1 * x^(2*k) ]
# F2(x) = sum k=0 to inf [1 * (x^2)^k ] = 1 / (1 - x^2)

## ------ F5 -------
# how many ways to have [0p, 1p, 2p, 3p, 4p, 5p] with 5p coins
# F5(x) = 1*x^0 + 0*x^1 + 0*x^2 + 0*x^3 + 0*x^4 + 1*x^5 +...
# F5(x) = sum k=0 to inf [1 * x^(5*k) ] = sum k=0 to inf [1 * (x^(5))^k ]
# F5(x) = 1 / (1 - x^5)

## ------ F2(x) * F5(x) --------
# F2(x) * F5(x) = [(1 * x^0) + (0 * x^1)...] * [1*x^0 + 0*x^1 + 0*x^2...]
# F2(x) * F5(x) = sum k=0 to inf [1 * x^(2*k) ] * sum k=0 to inf [1 * x^(5*k) ]

## ------ F1(x) * F2(x) * F5(x) -------
# F1(x) * F2(x) * F5(x) = [1 / (1 - x)] * [1 / (1 - x^2)] * [1 / (1 - x^5)]
# F1(x) * F2(x) * F5(x) = 1 / [(1 - x) (1 - x^2) (1 - x^5)]

## ------ Finding Taylor Series -------
# F2(x) * F5(x) = sum k=0 to inf [1 * x^(2*k) ] * sum k=0 to inf [1 * x^(5*k) ]
# F2(x) = sum k=1 to 200 [1 * x^(2*k) ] = a (1 - r^n) / (1 - r) = 1 (1 - x^(2*k)) / (1 - x)

## ------ Finding Geometric Series 1 -------
# F2(x) = (1 - x^(2*200)) / (1 - x)
# 1 is the initial term, the ratio is 1/2
# k = {1, 2, 3, 4} then {1/2, 1/4, 1/8, 1/16} = 1 / 2^k where k = 0 to inf
# 1 / 2^(2) = 1 / 4
# 1 / 2^(3) = 1 / 8
# the initial term is 1 where k = 0, and the geometric ratio is 1/2
# series1 = r (1 - r^n) / (1 - r) = 1/2 * (1 - (1/2)^200) / (1 - 1/2) = 1.0
print(float(1 / 2) * float(1 - float((1 / 2) ** 200)) / float(1 - 1 / 2))

## ------ Finding Geometric Series 2 -------
# F2(x) = sum k=0 to inf [1 * (x^2)^k ] = 1 / (1 - x^2)
#

# series - adding
# progression - sequence

# GOAL: sum from k = 1 to Lst_max (F1(x) * F2(x) * F5(x) = 1 / [(1 - x) (1 - x^2) (1 - x^5)])














