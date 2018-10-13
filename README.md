# Leercode - 121. Best Time to Buy and Sell Stock 

## 基本款
```python=
def MinMax(prices):
    MaxIncrease = 0
    MIN = sys.maxint
    for i in range(len(prices)):
        if prices[i] < MIN:
            MIN = prices[i]
        if prices[i] - MIN > MaxIncrease:
            MaxIncrease = prices[i] - MIN
    return MaxIncrease

```
## 進階款 - 求出買的時間點和賣的時間點
## 易錯：MinMax買的時間點
如果要問買的時間點，和賣的時間點的話，有一個地方容易錯，給一個例子
例如 ==prices = [5,3,7,8,100,**1**]==  的話，用下面的寫法，買的時間點會等於最後一個，可是真確的答案應該是第2個位置(prices[1]=3)才對。錯誤的程式碼如下。 
```python=
def MinMax(prices):
    MaxIncrease = 0
    MIN = sys.maxint
    p = -1                            ######
    q = -1                            ######
    for i in range(len(prices)):
        if prices[i] < MIN:
            MIN = prices[i]
            p = i                     ######             
        if prices[i] - MIN > MaxIncrease:
            MaxIncrease = prices[i] - MIN
            q = i                     ######
    return p, q, MaxIncrease

``` 
正確的程式碼應該如下
```python=
def MinMax(prices):
    MaxIncrease = 0
    MIN = sys.maxint
    p = -1
    q = -1
    tem_p = -1                              ######
    for i in range(len(prices)):
        if prices[i] < MIN:
            MIN = prices[i]
            tem_p = i                       ######
        if prices[i] - MIN > MaxIncrease:
            MaxIncrease = prices[i] - MIN
            q = i 
            p = tem_p                       ######
    return p, q, MaxIncrease
``` 
### 說明：
因為如果把買的時間點的判斷放在求min的時候會出錯，因為買的時間點一該搭配賣的時間點一起得出，所以應該要在求出最佳買賣時間點時判斷才對。
 
