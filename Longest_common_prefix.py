# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

#  Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# E
# xample 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length_str = min(strs, key=len)
        for i, char in enumerate(min_length_str):
            for string in strs:
                if string[i] != char:
                    return min_length_str[:i]
        
        return min_length_str



            
            
        