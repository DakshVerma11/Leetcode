class MyHashSet(object):

    def __init__(self):
        self.arr=[False]*1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key]=True
        return
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key]=False
        return 

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.arr[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
