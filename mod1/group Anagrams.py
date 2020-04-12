# Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#     ["ate","eat","tea"],
#     ["nat","tan"],
#     ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

###
# written by Bhuwan Singh
###


def fun1(arr, occ):
    arr2 = []
    for itator in range(len(arr)):
        if occ == arr[itator]:
            arr2.append(itator)
    return arr2


if __name__ == "__main__":
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    t = []
    for i in range(len(inp)):
        sorted_var = "".join(sorted(inp[i]))
        t.append("".join(sorted(inp[i])))
    dis_t = set(t)
    op = []
    for i in dis_t:
        temp = []
        for k in fun1(t, i):
            temp.append(inp[k])
        op.append(temp)
    print(op)

# best solution

# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ana = defaultdict(list)
#         for word in strs:
#             ana[''.join(sorted(word))].append(word)
#         return [value for value in ana.values()]
