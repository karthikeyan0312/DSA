#LT121
def maxProfit( prices: list[int]) -> int:
    small = 9999
    big=0
    for i in prices:
        if i <small:
            small = i
        else:
            temp = i-small
            big= max(big,temp)
    return big


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
