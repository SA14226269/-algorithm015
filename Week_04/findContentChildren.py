class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s or not g:
            return 0
        g.sort()
        s.sort()
        s_count = len(s) - 1
        g_count = len(g)-1
        result = 0
        while s_count >= 0 and g_count >= 0:
            if s[s_count] >= g[g_count]:
                s_count -= 1
                g_count -= 1
                result += 1
            else:
                g_count -= 1
        return result