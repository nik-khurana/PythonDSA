#Sorted List in ascending/descending order rotated n times
#Binary Search
# In a rotation, last element comes to first
# O(LogN) Binary Search solution
#O (N) Linear Search Solution : search for min element, the index represents remainder and no of rotations in equation-  c x len(nums) + index, return remainder

def linearSearchSolution(nums):
    for i in range(0,len(nums)):
        if nums[i]<nums[i-1] and i>0:
            return i
    return 0

# print(linearSearchSolution([1,2,3,4,5]))
# print(linearSearchSolution([5,1,2,2,4]))
# print(linearSearchSolution([4,5,1,2,3,4]))
# print(linearSearchSolution([1,1,1,1,1,1]))
# print(linearSearchSolution([2,3,4,5,1]))

def countNoOfRotations(nums):

    low=0
    high=len(nums)-1
    while (low<=high):
        mid=(low+high)//2
        #print(low,high,mid,nums[mid])
        if mid>0 and nums[mid]<nums[mid-1]:
            return mid
        elif nums[high]>nums[mid]:
        #right side is sorted, answer lies to left side
            high=mid-1
        else:
            #left side is sorted, answer lied to right side
            low=mid+1
    return 0

print(countNoOfRotations([1,2,3,4,5]))
print(countNoOfRotations([5,1,2,2,4]))
print(countNoOfRotations([4,5,1,2,3,4]))
print(countNoOfRotations([1,1,1,1,1,1]))
print(countNoOfRotations([2,3,4,5,1]))
print(countNoOfRotations([5,6,6,9,9,9,0,0,2,3,3,3,3,4,4]))




