from expansion import Expansion
from shifts_XOR import XOR
from shrinking import shrink
from permutation import Permutation
from permutation import inversePermutation

# f(R,K) part of the algorithm
def func(R,K):
    ER = Expansion(R)
    B = XOR(ER,K)
    B = shrink(B)
    B = Permutation(B)
    return B

#  function to calculate 16 stages during encryption
def calculate(IP,K):
    L = [(IP[0:32])]
    R = [(IP[32:])]
    for i in range(1,17):
        L.append(R[i-1])
        f = func(R[i-1],K[i-1])
        f = XOR(L[i-1],f)
        R.append(f)
    mess = R[16] + L[16]
    mess = inversePermutation(mess)
    return mess

#   function to calculate 16 stages during decryption
def cal_rev(IP,K):
    L = [(IP[0:32])]
    R = [(IP[32:])]
    for i in range(1,17):
        L.append(R[i-1])
        f = func(R[i-1],K[16-i])
        f = XOR(L[i-1],f)
        R.append(f)
    mess = R[16] + L[16]
    mess = inversePermutation(mess)
    return mess



