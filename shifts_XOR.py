# funtion to left shift by one bit
def shiftsByone(key):
    #print(key)
    temp = key[0]
    key = key[1:] + temp
    return key

#function to left shift by two bit
def shiftsBytwo(key):
    temp = key[0:2]
    key = key[2:] + temp
    return key

#   functiom to shift the data as per the requirement
def shifting(key):
    c = []
    d = []
    for i in range(0,17):
        if i == 0:
            c.append(key[i][0:28])
            d.append(key[i][28:])
        elif i == 1 or i == 2 or i == 9 or i == 16:
            c.append(shiftsByone(c[i-1]))
            d.append(shiftsByone(d[i-1]))
            key.append(c[i] + d[i])
        else:
            c.append(shiftsBytwo(c[i - 1]))
            d.append(shiftsBytwo(d[i - 1]))
            key.append(c[i] + d[i])
    return key


# function to XOR
def XOR(K,R):
    KR = "a"
    k = 0
    r = 0
    for i in range(0,len(K)):
        k = int(K[i])
        r = int(R[i])
        temp = bin(k ^ r)
        temp = temp[2:]
        KR = KR + temp
    KR = KR[1:]
    return KR



