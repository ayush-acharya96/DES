from conversion import hexToBin
from subkeygeneration import generate_subkey
from functional_part import cal_rev
from permutation import initialPermutation
from conversion import binaryToHex
from conversion import hexTostr


def decrypt(message, key):
    dec_mes = "a"
    key = hexToBin(key)
    K = generate_subkey(key)
    for i in range(0,len(message),16):
        mess = message[i:i+16]
        mess = hexToBin(mess)
        IP = initialPermutation(mess)
        IP = cal_rev(IP,K)
        dec_mes = dec_mes + IP
    dec_mes = dec_mes[1:]
    dec_mes = binaryToHex(dec_mes)
    dec_mes = hexTostr(dec_mes)
    return dec_mes



