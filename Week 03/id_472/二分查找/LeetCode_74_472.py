"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        length = m * n - 1
        left, right = 0, length

        # 把一维索引转换成行列索引
        def one_two(index):
            x = index // n
            y = index % n
            return x, y

        # 根据二分查找判断
        while left <= right:
            mid = left + (right - left) // 2
            x, y = one_two(mid)
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                left = mid + 1
            else:
                right = mid - 1
        return False
