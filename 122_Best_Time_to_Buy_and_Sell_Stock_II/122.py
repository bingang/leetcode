class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total

def main():
    prices = [7,1,5,3,6,4]

    S = Solution()
    print S.maxProfit(prices) 

if __name__ == "__main__":
    main()