class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        left = 0
        right = len(matrix[0])-1
        while(row < len(matrix)):
            mid = (left+right)/2
            if(matrix[row][mid] == target):
                return True
            elif(matrix[row][mid] < target):
                left = mid + 1
            else:
                right = mid - 1
            if(left > right):
                left = 0
                right = len(matrix[0])-1
                row += 1
        return False
        