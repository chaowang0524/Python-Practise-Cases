# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
# The number 27 is written as XXVII, which is XX + V + II.
 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# 499 = CD XC IX
# **************************************************
# Key algorithm: 
# if one character's value is less than the next value, subtract the value from the next value. 
# Otherwise add it to the total.
# **************************************************

def romanToInt(s: str) -> int:
    """Convert roman numeral to an integer

    Args:
        s (str): The given roman numeral

    Returns:
        int: the converted integer
    """

    resint = 0
    # find all the subtraction instances
    

    # convert each letter to number:

    # convert to list
    s = list(s)
    # print(s)
    # convert each item to number
    for i in range(len(s)):
        if s[i] == 'I':
            s[i] = 1
        elif s[i] == "V":
            s[i] = 5
        elif s[i] == "X":
            s[i] = 10
        elif s[i] == "L":
            s[i] = 50
        elif s[i] == "C":
            s[i] = 100
        elif s[i] == "D":
            s[i] = 500
        elif s[i] == "M":
            s[i] = 1000
    print(s)
    # # find all the subtraction instances
    for i in range(len(s)-1):
            if s[i] < s[i+1]:
                resint -= s[i]
            else:
                resint += s[i]
    resint += s[-1]
    return resint

romanToInt("MCMXCIV")
