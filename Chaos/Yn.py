# Importing all the functions from YInitial module for testing
from YInitial import *


# This module generates yn values

# This function takes initial value of y0 (as 'YInitial') generated using YInitial module
# and number of values to be generated (as 'number_of_values') and computes a chaotic value

def yn(YInitial, number_of_values=16):
    yn=YInitial
    yn_values = []
    while len(yn_values)<=number_of_values:
        y_n_plus_1 = (3.9999)*yn*(1-yn)
        yn = y_n_plus_1
        yn_values.append(y_n_plus_1)


    return yn_values[len(yn_values)-1]





## Unit Test code
#############################################################################
## This test code evaluates the value of yn using all the previous modules
## It also prints all the values generated at each step


# secret_key_80bits = 'ankit12345'
#
# binary_keys = to_8bit_keys(secret_key_80bits)
# print("Binary Keys:")
# for key in binary_keys:
#     print(key)
#
# print("Total binary keys: " + str(len(binary_keys)))
# hex_keys = to_hex_keys(secret_key_80bits)
#
#
# print("Hex Keys")
# print(hex_keys)
# print("Total hex keys: " + str(len(hex_keys)))
#
# print("Value of X01: "+str(x01(binary_keys)))
# print("Value of X02: "+str(x02(hex_keys)))
# x0 = x0(x01(binary_keys),x02(hex_keys))
# print("Value of X0: "+str(x0))
#
# f24 = xn(x0)
# print("24 values of f: ",f24)
#
# p24 = pk(f24)
# print("24 values of Pk: ",p24)
#
# y0 = y0(y01(binary_keys),y02(binary_keys,p24))
# print("Value of Y01: "+str(y01(binary_keys)))
# print("Value of Y02: "+str(y02(binary_keys,p24)))
# print("Value of Y0: "+str(y0))
# #print(y0)
# #0.5015889365167396
# #yn(y0,int(''.join(binary_keys[9]),2))
# yn_once = yn(y0,5)
# print((yn_once))
# print(len(yn_once))
#
