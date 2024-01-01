class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()
        stack = []
        for i in range(len(pair)-1, -1, -1):
            time = (float(target - pair[i][0])/pair[i][1])
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)