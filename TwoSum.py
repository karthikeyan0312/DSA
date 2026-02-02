#O(n)
def twoSum(nums,target):
    dt={}
    for i in range(0,len(nums)):
        temp=target-nums[i]
        if temp in dt:
            return dt[temp],i
        dt[nums[i]]=i
    return dt

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
