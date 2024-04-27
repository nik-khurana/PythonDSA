def linearSearch(nums,num):
    for i in range(len(nums)):
        if num==nums[i]:
            return i
    return -1

print(linearSearch([1,2,3,4,5,6],6))
print(linearSearch([1,2,3,4,5,6],7))
print(linearSearch([],0))
