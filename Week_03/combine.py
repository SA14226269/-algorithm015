class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = list(range(1,n+1))

        res = []
        if n < k or k == 0:
            return res
        def DFS(l, subnums):
            if len(subnums) == k:
                res.append(subnums)
            for j in range(len(l)):
                DFS(l[j+1:],subnums+[l[j]])
        DFS(l,[])
        return res