from conversion import strTohex
from conversion import hexToBin
from subkeygeneration import generate_subkey
from permutation import initialPermutation
from functional_part import calculate
from conversion import binaryToHex

def DES_encryption(message,key):
    enc_mess = "a"
    message = strTohex(message)
    key = hexToBin(key)
    K = generate_subkey(key)
    for i in range(0,len(message),16):
        mess = message[i:i+16]
        mess = hexToBin(mess)
        IP = initialPermutation(mess)
        IP = calculate(IP, K)
        IP = binaryToHex(IP)
        enc_mess = enc_mess +IP
    enc_mess = enc_mess[1:]
    return enc_mess



