class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Calculate sum of ones for each row and each column
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[r][c] for r in range(m)) for c in range(n)]
        
        special_count = 0
        
        # Check every element
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and row_sum[r] == 1 and col_sum[c] == 1:
                    special_count += 1
                    
        return special_count