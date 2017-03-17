# This module helps in key generation process
# Our key consists of minimum 10 characters of ASCII



# This function takes a key string of 10 characters(80 bit) for example: password12 and returns a list of 8 8bit keys in the form of list
# accessing a bit number 2 of key3 will be keys[2][1]
def to_8bit_keys(secret_key_80bits):
    keys = []
    for i in range(0,10):
        bits = bin(ord(secret_key_80bits[i]))[2:]
        binary_value = '00000000'[len(bits):]+bits
        keys.append(list(binary_value))

    return keys

# This function takes a key string of 10 characters(80 bit) for example: password12 and returns a list of 20 hexadecimal value of each letter in key string
# accessing the first hex value of 2nd character of key string will be keys[3]
def to_hex_keys(secret_key_80bits):
    keys = []
    for i in range(0,10):
        hexa = hex(ord(secret_key_80bits[i]))[2:]
        hex_value = hexa
        keys.extend(hex_value)
    return keys



## Test Code
#####################################################################
## This code tests this module by converting 10 ascii characters to 10 8-bits key and 20 hexadecimal keys

# binary_keys = to_8bit_keys('ankit12345')
# hex_keys = to_hex_keys('ankit12345')
# print(binary_keys)
# print(len(binary_keys))
# print(hex_keys)
# print(len(hex_keys))
#
