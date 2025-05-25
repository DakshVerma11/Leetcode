class MyHashMap(object):

    def __init__(self):
        self.arr=[-1]*1000001

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.arr[key]=value
        return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.arr[key]

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr[key]=-1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
