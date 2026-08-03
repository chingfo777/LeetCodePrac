class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        # Bottom-Up DP working backwards from the last stone
        for i in range(n - 1, -1, -1):
            # Choice 1: Take 1 stone
            res = stoneValue[i] - dp[i + 1]
            
            # Choice 2: Take 2 stones
            if i + 1 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
            
            # Choice 3: Take 3 stones
            if i + 2 < n:
                res = max(res, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3])
                
            dp[i] = res
            
        # Determine the winner based on Alice's optimal relative score advantage at index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"