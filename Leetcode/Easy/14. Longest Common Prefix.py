# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# ****************************************************************
# Key algorithm: Only to compare letters in other words to the ones in the shortest word. 
# The time of comparison is the length of the shortest word.
# ****************************************************************

def longestCommonPrefix(strs: list[str]) -> str:
    """Find the longest common prefix string amongst an array of strings.

    Args:
        strs (list[str]): the given list of strings 

    Returns:
        str: the longest common prefix string
    """

    ### method 1
    # set up the variables
    # comprefix = ""
    # list_to_check = []
    # secpointer = 0
    # resultlist = []
    # result = ""
    # strs=sorted(strs)
    # # 要将第一个词的第一个字和第二个词的第一个字和第三个词的第一个字...对比
    # while secpointer <= len(strs[0])-1:
    #     for i in range(len(strs)): # 遍历每个词：
    #         # 拿到所有词的第一个字
    #         comprefix = strs[i][secpointer]
    #         # 把结果放到一个列表中
    #         list_to_check.append(comprefix)
    #     # 第一个字全部加到列表之后，去重
    #     copylist = list_to_check # copy列表，准备以set方式去重，分开操作以方便继续append
    #     list_to_check = [] # 列表清零，准备拿下一个字，以免与此次混淆
    #     copylist = set(copylist) # 将新列表转为set去重
    #     # 这时如果出现不一致（元素数大于一），跳出
    #     if len(copylist) != 1:
    #         break
    #     # 目前全部一致，那么第二指针+1，去拿所有词的第2个字
    #     secpointer += 1 
    #     # set转回列表以收集结果至新列表
    #     copylist = list(copylist)
    #     resultlist.append(copylist[0])
    # # 输出结果
    # for i in resultlist:
    #     result += i
    # return result.lower()

    # method 2: 
    result = ""
    # sort the list to get the number of times we need to iterate
    strs = sorted(strs)
    # loop starts:
    for i in range(len(strs[0])):
        for s in strs: 
            # compare letters in the same position in other words to letters in the first words
            # The resutl of the first iteration should be same s[0] == strs[0][0]
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += i
    return result


        
longestCommonPrefix(["dog","racecar","car"])
