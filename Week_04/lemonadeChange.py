class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        initial = {'5':1, '10':0,'20':0}

        for i in range(1,len(bills)):
            charge = bills[i] - 5
            if charge == 5:
                if initial['5'] == 0:
                    return False
                initial['5'] -= 1
                initial['10'] += 1
            elif charge == 15:
                initial['20'] += 1
                if initial['10'] > 0 and initial['5'] > 0:
                    initial['10'] -= 1
                    initial['5'] -= 1
                elif initial['10'] == 0 and initial['5'] >= 3:
                    initial['5'] -= 3
                else:
                    return False
            else:
                initial['5'] += 1
        return True