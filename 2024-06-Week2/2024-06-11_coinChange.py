"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. brute force 쓰면 안될 듯
        # 2. DP
        inf = sys.maxsize
        # 예외 처리
        if amount == 0:
            return 0
    
        dp = [inf] * (amount + 1)
        dp[0] = 0
            
        # print(dp)
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    # print(f"i={i},coin={coin}, dp={dp}")
        
        if dp[amount] == inf:
            return -1
        else:
            return dp[amount] 