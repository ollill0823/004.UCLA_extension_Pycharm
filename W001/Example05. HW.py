def sqSum1 (x, y):
    sumsq=x**2 + y**2
    return sumsq

def sqSum2 (x, y):
    sumsq=x**2 + y**2
    print (sumsq)

sqSum1(2,3) ## 沒有print,所以不做動作
sqSum2(2,3) # 本身沒有print所以不做動作,但是 第二個函數會做print的動作 所以Ans=13
print(sqSum1(2,3))  ##Ans=13
print(sqSum2(2,3))  ##因為沒有return,所以不會回傳數字,所以Ans=None,
## 但是因為做第二個函數的時候會有print的動作,所以最後答案為 Ans= 13, None