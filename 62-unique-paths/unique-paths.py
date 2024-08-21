class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a 2d array
        cache = [[0]*n for _ in range(m)]

        def dfs(r, c):
            # base
            if r==m-1 and c==n-1:
                return 1
            
            # out of bound condition
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            
            if cache[r][c] != 0:
                return cache[r][c]

            # main
            cache[r][c] = dfs(r+1, c) + dfs(r, c+1)
            return cache[r][c]

        return dfs(0, 0)