class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        d = len(matrix) - 1
        print(f'd={d}')
        while t <= d:
            m = (t+d)// 2
            print(f'mid of cols is {m}')
            if matrix[m][-1] < target:
                t = m + 1
            elif matrix[m][0] > target:
                d = m - 1
            else:
                break
        l = 0
        r = len(matrix[0])- 1
        print(f'r = {r}')
        while l <= r:
            m2 = (l+r)// 2
            print(f'mid of rows is {m2}')
            if matrix[m][m2] < target:
                l = m2 + 1
            elif matrix[m][m2] > target:
                r = m2 - 1
            else:
                return True
        return False