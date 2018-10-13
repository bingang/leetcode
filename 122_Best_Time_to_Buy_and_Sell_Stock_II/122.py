import sys
class Solution(object):
    def Wrong_maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p_arr = []
        q_arr = []
        start = 0
        end = len(prices) - 1
        turn = 1
        while True:
            if turn:
                p,q = MinMaxPair(prices[start:end+1])
            else:
                p,q = MaxMinPair(prices[start:end+1])
            if (p == -1 or q == -1):
                break
            p = p+start
            q = q+start
            p_arr.append(p)
            q_arr.append(q)
            end = q - 1
            start = p + 1 
            turn = 1 - turn

        ans = 0
        arr = p_arr + q_arr[::-1]
        for i in range(len(arr)/2):
            ans += (prices[arr[2*i+1]] - prices[arr[2*i]])
        return ans
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
def MinMaxPair(prices):
    MaxIncrease = 0
    MIN = sys.maxint
    p = -1
    q = -1
    tem_p = -1
    for i in range(len(prices)):
        if prices[i] < MIN:
            MIN = prices[i]
            tem_p = i
        if prices[i] - MIN > MaxIncrease:
            MaxIncrease = prices[i] - MIN
            q = i
            p = tem_p            
    return p,q
def MaxMinPair(prices):
    MaxDecrease = 0
    MAX = -sys.maxint-1
    p = -1
    q = -1
    tep_q = -1
    for i in range(len(prices)):
        if prices[i] > MAX:
            MAX = prices[i]
            tem_p = i
        if prices[i] - MAX < MaxDecrease:
            MaxDecrease = prices[i] - MAX
            q = i
            p = tem_p
    return p,q

def main():
    prices = [7,1,5,3,6,4]

    S = Solution()
    print S.Wrong_maxProfit(prices) # problematic if prices = [1,0,2,0,1]
    print S.maxProfit(prices)

if __name__ == "__main__":
    main()