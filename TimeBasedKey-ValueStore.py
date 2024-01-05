class TimeMap(object):

    def __init__(self):
        self.hashmap = {}
        self.stack = []
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.hashmap.get(key, [])
        left = 0
        right = len(values)-1 
        while(left <= right):
            mid = (left+right)/2
            if(values[mid][1] <= timestamp):
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)