# Base Condition for Binary Search : Sorted Array
# function below for list in ascending order

def checkLeft(nums,num,mid):
    if nums[mid]==num:
        if nums[mid]==nums[mid-1] and mid-1>=0:
            return 'left'
        else:
            return 'match'
    elif nums[mid]>num:
        return 'left'
    else:
        return 'right'

def binarySearch(nums,num):
    low=0
    high=len(nums)-1
    while (low<=high):
        mid=(low+high)//2
        print(low, high, mid, nums[mid])
        left=checkLeft(nums,num,mid)
        if left=='match':
            return mid
        elif left=='left':
            high=mid-1
        else:
            low=mid+1
    return -1

# print(binarySearch([1,2,3,4,5,6],5))
# print(binarySearch([1,2,3,4,5,6],7))
# print(binarySearch([1,2,4,4,5,6],5))
# print(binarySearch([2,2,3,4,5,6],2))
print(binarySearch([5,5,5,5,5,5,5,5],5))
# print(binarySearch([],0))
