class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        code = []
        for i in range(0,26):
            code.append(0)
        for i in s:
            code[ord(i) - 101] += 1
        for i in t:
            code[ord(i) - 101] -= 1
        for i in code:
            if i:
                return False
        return True