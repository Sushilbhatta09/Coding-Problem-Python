#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs):
        # sort the array and then compare the first and last string
        short = min(strs, key=len) #// short = "flow"
        for item in strs: #// When item = "flight"
            while len(short) > 0:
                if item.startswith(short): #// during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                    break
                else:
                    short = short[:-1] #// during loop 1 short = flo, during loop 2 short = fl
        return short
