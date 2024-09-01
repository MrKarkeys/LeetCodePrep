class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def getCoor(c):
            return (ord(c[0])-ord('a'), int(c[1])-1)
        def getColor(coordinate):
            val1, val2 = getCoor(coordinate)
            return val1%2 == val2%2
        return getColor(coordinate1) == getColor(coordinate2)
