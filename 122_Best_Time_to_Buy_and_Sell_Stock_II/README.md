# 122. Best Time to Buy and Sell Stock II

## 錯誤思路
目標
>觀察到說如果找到有valley peak valley peak的模式，再把每一個
(valley, peak)的pair相減，再加總就是答案了

直覺
>那就從左右兩邊開始進攻，左邊找valley，右邊找peak。再從裡面找，這樣就可以有更大的差異了。可以看到下方的兩張圖，如果再從裡面找，會有更大的差距。

![](https://i.imgur.com/rBtaIDE.png)

演算法簡要說明
>有點像是從array的兩邊一直拔掉東西，然後再處理剩下裡面的array。然後每次拔掉的東西就是(Min, Max) or (Max, Min)的index pair。然後再把這些pair搜集起來，用來算出之後答案。

實際的說
>這題一開始想的很複雜，主要的想法為
從左邊找小的-->從右邊找最大的-->把array的兩邊拿掉-->從裡面繼續找
從左邊找最大的-->從右邊找最小的-->把array的兩邊拿掉-->從裡面繼續找
就這樣一直輪迴下去，直到沒有找到為止，然後每一次找到(MIN,MAX) or (MAX,MIN)的時候都把他們的index放在兩個array，最後再去透過那兩個array算出答案

會這樣做的原因？
>這樣就會valley peak valley peak一直重複

想像一下？
>有點像是從array的兩邊一直拔掉東西，然後再處理剩下裡面的array。然後每次拔掉的東西就是(Min, Max) or (Max, Min)的index pair。然後再把這些pair搜集起來，用來算出之後答案。

```python=
class Solution(object):
    def Wrong_maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p_arr = []       # 用來放前面的index，分別是min,max,min,max...交替
        q_arr = []       # 用來放後面的index，分別是max,min,max,min...交替
        start = 0
        end = len(prices) - 1
        turn = 1        # 用turn來輪流找MinMaxPair和MaxMinPair
        while True:
            if turn:
                p,q = MinMaxPair(prices[start:end+1])
            else:
                p,q = MaxMinPair(prices[start:end+1])
                
            if (p == -1 or q == -1): ## 沒有找到 MinMaxPair 或是 MaxMinPair
                break
            p = p+start
            q = q+start
            p_arr.append(p)
            q_arr.append(q)
            end = q - 1
            start = p + 1 
            turn = 1 - turn  # turn的轉換方法

        ans = 0
        arr = p_arr + q_arr[::-1] # 要把存後面index的array反轉過來
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

```
為何錯誤？
>因為沒有考慮到prices= [1,0,2,0,1]這種情況，這種情況就是每個(valley,peak)不是包在(valley,peak)裡面的，而是分開獨立的。用此演算法的所得的結果是 prices[2] - prices[1] = 2。但實際上應該是（prices[2] - prices[1]）＋（prices[3] - prices[4]）才對

心得
>這題只是要找valley, peak, valley, peak交錯的情形就好了，其實可以由左到右scan一次就好，不用像我的作法一樣，從兩邊開始找，而忽略(valley,peak)分開獨立的case。
## 正確思路
後來跑去看discuss才知道這題其實很簡單...
### 法一：
找valley-->找peak-->先找valley-->先找peak.....
```python=
valley = prices[0]
peak = prices[0]
sum = 0
i = 0
while i < len(prices) - 1 :
    ################### 找valley ###################
    while(prices[i] >= prices[i+1]) && i < len(prices) -1):
        i = i + 1
    valley = prices[i]
    ################### 找peak ###################
    while(prices[i] <= prices[i+1]) && i < len(prices) -1):
        i = i + 1
    peak = prices[i]
    # i = i + 1    不用這個！    
    sum += peak - valley
return sum
    
```
#### Case 1 一般情形 : __valley-->peak-->valley-->peak....__
#### Case 2 一群peak : ~~valley~~-->peak-->peak-->peak-->~~valley~~
>一路向上，沒有遇到新的valley，那其實就是每隔間隔的差距的加起來，等效的的結果就是就是最後一個valley與遇到valley的前一個peak的差距
#### Case 3 一群valley : __~~peak~~-->valley-->valley-->valley-->~~peak~~__
>一路向下，沒有遇到新的peak，結果就會是一直在line 7,8一直跑，跑到下一個是peak的前一個index（=j），然後此時valley = peak = prices[j] ==> peak - valley = 0

## 法二
把法一的想法更精練一點，就是前面一個比前面大的時後，就相減ˋ，再加總起來，就是答案了...
```python=
total = 0
for i in range(len(prices)-1):
    if prices[i+1] > prices[i]:
        total += prices[i+1] - prices[i]
return total
```

ref : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

