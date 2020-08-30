class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.max_len = k
        self.circularDeque = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.circularDeque) < self.max_len:
            self.circularDeque = self.circularDeque[::-1]
            self.circularDeque.append(value)
            self.circularDeque = self.circularDeque[::-1]
            return True
        return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.circularDeque) < self.max_len:
            self.circularDeque.append(value)
            return True
        return False
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.circularDeque):
            del self.circularDeque[0]
            return True
        return False
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.circularDeque):
            del self.circularDeque[-1]
            return True
        return False
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.circularDeque):
            return self.circularDeque[0]
        return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.circularDeque):
            return self.circularDeque[-1]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if len(self.circularDeque):
            return False
        return True
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if len(self.circularDeque) == self.max_len:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()