# Importing all the functions from XInitial module
from XInitial import *

# This module uses the first logistic map and the value obtained from the XInitial modules.
# It iterates until we get 24 real number values that lie between 0.1 and 0.9.
# The above values are then converted into 24 integer values using a function pk.



# This function takes initial value of Xn (i.e. X0 calculated using XInitial module) and iterates until 24 real number values that lie between 0.1 and 0.9 are obtained.
# This function returns a list of 24 real numbers
def xn(XInitial,number_of_values=24):
    xn = XInitial
    f24 = list()

    while len(f24)<number_of_values:
        x_n_plus_1 = 3.9999*xn*(1-xn)
        xn = x_n_plus_1
        if 0.1 < x_n_plus_1 < 0.9:
            f24.append(x_n_plus_1)


    return f24

# This function takes the 24 real number values generated using the xn function  and converts them into 24 integer values
# This function returns a list of 24 integer values
def pk(_24_values_of_f):
    f24 = _24_values_of_f
    p24 = []
    for f in f24:
        p24.append(int(23 * ((f - 0.1) / 0.8)) + 1)
    return p24



## Test code
############################################################################
## To test this module we import all the previous modules
## First we generate 24 real numbers using xn() function and using we generate 24 integer values
## using pk() function
#
#
# binary_keys = to_8bit_keys('ankit12346')
# hex_keys = to_hex_keys('ankit12345')
#
# x0 = x0(x01(binary_keys),x02(hex_keys))
#
# f24 = xn(x0)
# print(f24)
# print("Length of f24:",len(f24))
# p24 = pk(f24)
# print(p24)
# print("Length of p24:",len(p24))
