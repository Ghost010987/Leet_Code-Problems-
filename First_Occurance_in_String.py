class Solution:
    def strStr(self, haystack, needle):
        x = len(haystack)
        y = len(needle)

        for i in range(x - y + 1):
            if haystack[i : i + y] == needle:
                return i
        
        return -1
