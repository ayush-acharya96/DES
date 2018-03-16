from permutation import initial_keyPermutation
from shifts_XOR import shifting
from permutation import secondPermutation

#   generates 16 subkeys
def generate_subkey(key):
    key = initial_keyPermutation(key)
    k = [key]
    k = shifting(k)
    k = secondPermutation(k)
    return k



