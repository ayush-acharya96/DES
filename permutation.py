#   creating initial permutation table using tuple IP for initial permutation
IP = (58 , 50 , 42 , 34 , 26 , 18 , 10 , 2 ,
      60 , 52 , 44 , 36 , 28 , 20 , 12 , 4 ,
      62 , 54 , 46 , 38 , 30 , 22 , 14 , 6 ,
      64 , 56 , 48 , 40 , 32 , 24 , 16 , 8 ,
      57 , 49 , 41 , 33 , 25 , 17 , 9 , 1 ,
      59 , 51 , 43 , 35 , 27 , 19 , 11 , 3 ,
      61 , 53 , 45 , 37 , 29 , 21 , 13 , 5 ,
      63 , 55 , 47 , 39 , 31 , 23 , 15 , 7)

# PC - 1  table for initial key permutation
PC_1 = ( 57 , 49 , 41 , 33 , 25 , 17 , 9 ,
         1 , 58 , 50 , 42 , 34 , 26 , 18 ,
         10 , 2 , 59 , 51 , 43 , 35 , 27 ,
         19 , 11 , 3 , 60 , 52 , 44 , 36 ,
         63 , 55 , 47 , 39 , 31 , 23 , 15 ,
         7 , 62 , 54 , 46 , 38 , 30 , 22 ,
         14 , 6 , 61 , 53 , 45 , 37 , 29 ,
         21 , 13 , 5 , 28 , 20 , 12 , 4 )

# permutation table for  permutation done after the s-box calculation for permutation
P = (16 , 7 , 20 , 21 ,
     29 , 12 , 28 , 17 ,
     1 , 15 , 23 , 26 ,
     5 , 18 , 31 , 10 ,
     2 , 8 , 24 , 14 ,
     32 , 27 , 3 , 9 ,
     19 , 13 , 30 , 6 ,
     22 , 11 , 4 , 25)

#   PC-2 table  data for second permutation
PC_2 = (14 , 17 , 11 , 24 , 1 , 5 ,
        3 , 28 , 15 , 6 , 21 , 10 ,
        23 , 19 , 12 , 4 , 26 , 8 ,
        16 , 7 , 27 , 20 , 13 , 2 ,
        41 , 52 , 31 , 37 , 47 , 55 ,
        30 , 40 , 51 , 45 , 33 , 48 ,
        44 , 49 , 39 , 56 , 34 , 53 ,
        46 , 42 , 50 , 36 , 29, 32)

#   Inverse permutation table for inverse permutation
IP_1 = (40 , 8 , 48 , 16 , 56 , 24 , 64 , 32 ,
        39 , 7 , 47 , 15 , 55 , 23 , 63 , 31 ,
        38 , 6 , 46 , 14 , 54 , 22 , 62 , 30 ,
        37 , 5 , 45 , 13 , 53 , 21 , 61 , 29 ,
        36 , 4 , 44 , 12 , 52 , 20 , 60 , 28 ,
        35 , 3 , 43 , 11 , 51 , 19 , 59 , 27 ,
        34 , 2 , 42 , 10 , 50 , 18 , 58 , 26 ,
        33 , 1 , 41 , 9 , 49 , 17 , 57 , 25)

#   function for second permutation for PC_2 table
def secondPermutation(key):
    k = []
    for i in range(1,17):
        key0 = "a"
        for j in PC_2:
            key0 = key0 + key[i][j-1]
        k.append(key0[1:])
    return k

#    function for the permutation  after s-box implementation for P table
def Permutation(m):
    m0 = "a"
    for i in P:
        m0 = m0 + m[i-1]
    m0 = m0[1:]
    return m0

#   function to apply initial permutation to the message from IP table
def initialPermutation(m):
    m0 = "a"
    for i in IP:
        m0 = m0 + m[i-1]
    m0 = m0[1:]
    return m0

#   function for initial permutation of the 64-bit message from PC_1 table
def initial_keyPermutation(key):
    key0 = "a"
    for i in PC_1:
        key0 = key0 + key[i-1]
    key0 = key0[1:]
    return key0

# function to inverse permute for IP_1 table
def inversePermutation(m):
    m0 = "a"
    for i in IP_1:
        m0 = m0 + m[i-1]
    m0 = m0[1:]
    return m0



