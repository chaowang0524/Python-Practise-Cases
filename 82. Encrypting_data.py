# Encrypt the raw data with following rules:
# Add 5 to each number
# divide the sum by 10
# replace the number with the remainder
# swap the first and last digits and the second and the third digits

def encrypting(raw:int)->int:
    """Encrypting the raw data

    Args:
        raw (int): a four digit integer

    Returns:
        int: the encrypted number
    """

    # split the number into 4 single numbers by converting to string first
    add5_str = [i for i in str(raw)]
    # convert back to numbers then add 5
    add5 = [int(i)+5 for i in add5_str]
    # divide by 10 and take the remainder
    dividedlist = [i%10 for i in add5]
    # swap the number
    swaplist = dividedlist
    swaplist[0],swaplist[3] = swaplist[3],swaplist[0]
    swaplist[1],swaplist[2] = swaplist[2],swaplist[1]

    return (swaplist[0]*1000+swaplist[1]*100+swaplist[2]*10+swaplist[3])

encrypting(9999)