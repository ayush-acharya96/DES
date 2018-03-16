#   creating Expansion table using tuple E
E = (32 , 1 , 2 , 3 , 4 , 5 ,
     4 , 5 , 6 , 7 , 8 , 9 ,
     8 , 9 , 10 , 11 , 12 , 13 ,
     12 , 13 , 14 , 15 , 16 , 17 ,
     16 , 17 , 18 , 19 , 20 , 21 ,
     20 , 21 , 22 , 23 , 24 , 25 ,
     24 , 25 , 26 , 27 , 28 , 29 ,
     28 , 29 , 30 , 31 , 32 , 1)

#   function to expand 32-bit data to 48-bit
def Expansion(R):
    R0 = "a"
    for i in E:
        R0 = R0 + R[i-1]
    R0 = R0[1:]
    return R0



