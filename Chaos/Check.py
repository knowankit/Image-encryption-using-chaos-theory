from Yn import *
from Convert import *

## This module has all the rules associated with yn and r,g,b values for encryption and decryption

def check_operations_to_be_performed(y_value,r_value,g_value,b_value,binary_keys,decryption=False):
    if 0.10 <= y_value <= 0.13 or 0.34 < y_value <= 0.37 or 0.58 < y_value <= 0.62:     #operation 1
        return operation_1(r_value, g_value, b_value)

    if 0.13 < y_value <= 0.16 or 0.37 < y_value <= 0.40 or 0.62 < y_value <= 0.66:     #operation 2
        return operation_2(r_value, g_value, b_value, binary_keys, i=3, j=4, k=5)

    if 0.16 < y_value <= 0.19 or 0.40 < y_value <= 0.43 or 0.66 < y_value <= 0.70:     #operation 3
        return operation_3(r_value, g_value, b_value, binary_keys, decryption, i=3, j=4, k=5)

    if 0.19 < y_value <= 0.22 or 0.43 < y_value <= 0.46 or 0.70 < y_value <= 0.74:     #operation 4
        return operation_4(r_value, g_value, b_value, binary_keys, decryption, i=3, j=4, k=5)

    if 0.22 < y_value <= 0.25 or 0.46 < y_value <= 0.49 or 0.74 < y_value <= 0.78:     #operation 5
        return operation_5(r_value, g_value, b_value, binary_keys, i=6, j=7, k=8)

    if 0.25 < y_value <= 0.28 or 0.49 < y_value <= 0.52 or 0.78 < y_value <= 0.82:     #operation 6
        return operation_6(r_value, g_value, b_value, binary_keys, decryption, i=6, j=7, k=8)

    if 0.28 < y_value <= 0.31 or 0.52 < y_value <= 0.55 or 0.82 < y_value <= 0.86:     #operation 7
        return operation_7(r_value, g_value, b_value, binary_keys, decryption, i=6, j=7, k=8)

    if 0.31 < y_value <= 0.34 or 0.55 < y_value <= 0.58 or 0.86 < y_value <= 0.90:     #operation 8
        return operation_8(r_value, g_value, b_value)
    else:
        return operation_6(r_value, g_value, b_value, binary_keys, decryption, i=0, j=5, k=9)




### Performs NOT operation on a given binary string and returns the resultant binary string
def NOT(binary_value):
    b = list(binary_value)
    for i in range(0,len(b)):
        if b[i] == '1':
            b[i] = '0'
        elif b[i] == '0':
            b[i] = '1'

    return ''.join(b)



# Takes r,g and b values in int and returns a list of these values respectively as a list[r,g,b] after performing a NOT operation
def operation_1(r_value,g_value,b_value):
    values = []
    r = NOT(int_to_binary_string(r_value))
    g = NOT(int_to_binary_string(g_value))
    b = NOT(int_to_binary_string(b_value))
    r = binary_string_to_int(r)
    g = binary_string_to_int(g)
    b = binary_string_to_int(b)

    values.append(r%256)
    values.append(b%256)
    values.append(g%256)
    return values


# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_2(r_value,g_value,b_value,binary_keys,i=3,j=4,k=5):
    values = []
    values.append((r_value ^ binary_list_to_int(binary_keys[i]))%256)     #modding here because values go above 256
    values.append((g_value ^ binary_list_to_int(binary_keys[j]))%256)
    values.append((b_value ^ binary_list_to_int(binary_keys[k]))%256)
    return values


# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_3(r_value,g_value,b_value,binary_keys,decryption=False,i=3,j=4,k=5):
    values = []
    k4 = binary_list_to_int(binary_keys[i])
    k5 = binary_list_to_int(binary_keys[j])
    k6 = binary_list_to_int(binary_keys[k])
    if decryption == False:
        values.append((r_value + k4+ k5) % 256)
        values.append((g_value + k5 + k6) % 256)
        values.append((b_value + k6 + k4) % 256)
    elif decryption == True:
        values.append((r_value + 256 - k4 - k5)%256)    #modding here because values go above 256
        values.append((g_value + 256 - k5 - k6)%256)
        values.append((b_value + 256 - k6 - k4)%256)

    return values

# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_4(r_value,g_value,b_value,binary_keys,decryption=False,i=3,j=4,k=5):
    values = []
    k4 = binary_list_to_int(binary_keys[i])
    k5 = binary_list_to_int(binary_keys[j])
    k6 = binary_list_to_int(binary_keys[k])
    if decryption == False:
        values.append(binary_list_to_int(NOT(int_to_binary_list(r_value^k4)))%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(g_value^k5)))%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(b_value^k6)))%256)
    elif decryption == True:
        values.append(binary_list_to_int(NOT(int_to_binary_list(r_value)))^k4%256)    #modding here because values go above 256
        values.append(binary_list_to_int(NOT(int_to_binary_list(g_value)))^k5%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(b_value)))^k6%256)

    return values

# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_5(r_value,g_value,b_value,binary_keys,i=6,j=7,k=8):
    values = []
    values.append(r_value ^ binary_list_to_int(binary_keys[i])%256)
    values.append(g_value ^ binary_list_to_int(binary_keys[j])%256)
    values.append(b_value ^ binary_list_to_int(binary_keys[k])%256)
    return values


# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_6(r_value,g_value,b_value,binary_keys,decryption=False,i=6,j=7,k=8):
    values = []
    k4 = binary_list_to_int(binary_keys[i])
    k5 = binary_list_to_int(binary_keys[j])
    k6 = binary_list_to_int(binary_keys[k])
    if decryption == False:
        values.append((r_value + k4+ k5) % 256)
        values.append((g_value + k5 + k6) % 256)
        values.append((b_value + k6 + k4) % 256)
    elif decryption == True:
        values.append((r_value + 256 - k4 - k5)%256)    #modding here because values go above 256
        values.append((g_value + 256 - k5 - k6)%256)
        values.append((b_value + 256 - k6 - k4)%256)

    return values


# Takes r,g ,b values in int and binary_keys and returns a list of these values respectively as a list[r,b,g] after modding
def operation_7(r_value,g_value,b_value,binary_keys,decryption=False,i=6,j=7,k=8):
    values = []
    k4 = binary_list_to_int(binary_keys[i])
    k5 = binary_list_to_int(binary_keys[j])
    k6 = binary_list_to_int(binary_keys[k])
    if decryption == False:
        values.append(binary_list_to_int(NOT(int_to_binary_list(r_value^k4)))%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(g_value^k5)))%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(b_value^k6)))%256)

    elif decryption == True:
        values.append(binary_list_to_int(NOT(int_to_binary_list(r_value)))^k4%256)    #modding here because values go above 256
        values.append(binary_list_to_int(NOT(int_to_binary_list(g_value)))^k5%256)
        values.append(binary_list_to_int(NOT(int_to_binary_list(b_value)))^k6%256)


    return values

# Takes r,g ,b values in int and returns a list of these values respectively as a list[r,b,g] after modding
def operation_8(r_value,g_value,b_value):
    values = []
    values.append(r_value)
    values.append(g_value)
    values.append(b_value)
    return values


# This function takes all the binary keys and return a new set of binary keys without modifying the 10th key
def modifying_session_keys(binary_keys):
    new_session_keys = []
    for i in range(0, 9):
        new_key = (binary_list_to_int(binary_keys[i]) + binary_list_to_int(binary_keys[9])) % 256
        new_session_keys.append(int_to_binary_list(new_key))

    new_session_keys.append(binary_keys[9])
    return new_session_keys






###TEST CODE
#######################################################################
## This test code tests all the functions defined and conversion codes
## check_operations_to_be_performed(.78)


# binary_keys = to_8bit_keys('ankit12345')
# print("RGB = 128,64,219")
# print("Operation..1")
# print(operation_1(128,64,219))
# print("Operation..1 to get back values:")
# print(operation_1(127, 36, 191))
# print("Operation..2")
# print(operation_2(128,64,219,binary_keys))
# print("Operation..2 to get back values:")
# print(operation_2(233, 52, 234,binary_keys))
# print("Operation..3")
# print(operation_3(128,64,219,binary_keys))
# print(operation_3(93,229,117,binary_keys,decryption=True))
# print("Operation..4")
# print(operation_4(128,64,219,binary_keys))
# print(operation_4(22,203,21,binary_keys,decryption=True))
# print("Operation..5")
# print(operation_5(128,64,219,binary_keys))
# print(operation_5(178,115,239,binary_keys))
# print("Operation..6")
# print(operation_6(128,64,219,binary_keys))
# print(operation_6(229,167,65,binary_keys,decryption=True))
# print("Operation..7")
# print(operation_7(128,64,219,binary_keys))
# print(operation_7(77,140,16,binary_keys,decryption=True))
# print("Operation..8")
# print(operation_8(128,64,219))
#
# print(binary_list_to_int(binary_keys[3]))
# print(binary_list_to_int(binary_keys[4]))
# print(binary_list_to_int(binary_keys[5]))
#
# r_value = 191
#
#
# print("Coverting int to binary string:",int_to_binary_string(191))
# print("Coverting binary string to binary list:",binary_string_to_binary_list(int_to_binary_string(191)))
# print("Coverting binary list to binary string:",binary_list_to_binary_string(['1', '0', '1', '1', '1', '1', '1', '1']))
# print("Coverting binary string to int:",binary_string_to_int('10111111'))
# print("Coverting binary list to int:",binary_list_to_int(['1', '0', '1', '1', '1', '1', '1', '1']))
#
#
# print(check_operations_to_be_performed(.22,128,64,110,binary_keys))
# print(check_operations_to_be_performed(.22,22, 203, 160,binary_keys,decryption=True))

