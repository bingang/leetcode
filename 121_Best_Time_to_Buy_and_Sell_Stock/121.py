import sys
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
    return p, q, MaxIncrease

def main():
    prices = [7,1,5,3,6,4]
    p, q, MaxIncrease =  MinMaxPair(prices)
    print "MaxProfit = ",MaxIncrease
    print "BuyTime = ",p
    print "SellTime = ",q

if __name__ == "__main__":
    main()