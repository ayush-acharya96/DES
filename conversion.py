#  Function to convert hexadecimal to binary
def hexToBin(s):
    lst = "a"
    for i in s:
        new = "{0:04b}".format(int(i,16))
        lst = lst + new
    lst = lst[1:]
    return lst


#   converts 64-bit binary to hexadecimal
def binaryToHex(m):
    mes = "a"
    for i in range(0,len(m),4):
        temp = m[i:i+4]
        # print(temp)
        temp = hex(int(temp,2))[2:]
        # print(temp)
        mes = mes + temp
        # print(mes)
    mes = mes[1:]
    return mes

#   function to convert plain text into hexadecimal
def strTohex(s):
    temp = "a"
    for ch in s:
        temp = temp + "{0:02x}".format(ord(ch))
    temp = temp[1:]
    temp = temp + "0d0a"
    if len(temp)%16 != 0:
        add = 16 - (len(temp)%16)
        for i in range(0,add):
            temp = temp + "0"
    return temp

#   function to convert hexadecimal to corresponding string
def hexTostr(s):
    temp = "a"
    for i in range(0,len(s),2):
        b = int(s[i:i+2],16)
        temp = temp + chr(b)
    temp = temp[1:]
    return temp



