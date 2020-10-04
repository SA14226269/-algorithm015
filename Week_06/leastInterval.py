class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskmap = [0 for i in range(26)]
        for i in tasks:
            taskmap[ord(i)-ord('A')] += 1
        time = 0
        taskmap.sort()

        while taskmap[25] > 0:
            i = 0
            while i <= n:
                if taskmap[25] == 0:
                    break
                if i < 26 and taskmap[25-i] > 0:
                    taskmap[25-i] -= 1
                i += 1
                time += 1
            taskmap.sort()
        return time