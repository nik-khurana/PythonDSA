# Base Condition for Binary Search : Sorted Array
# function below for list in ascending order
def binarySearch(nums,num):
    if len(nums)<1:
        return -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if num==nums[mid]:
            return mid
        elif nums[mid]<num:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binarySearch([1,2,3,4,5,6],5))
print(binarySearch([1,2,3,4,5,6],7))
print(binarySearch([],0))