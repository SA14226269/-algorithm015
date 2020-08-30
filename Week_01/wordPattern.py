class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        print(list(map(pattern.index,pattern)))
        return list(map(pattern.index,pattern)) == list(map(words.index,words))