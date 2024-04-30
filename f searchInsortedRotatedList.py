# LC 33: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
def search(nums,target):
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            # left side sorted
            if nums[low] <= target and target <= nums[mid]:
                # element exists
                high = mid - 1
            else:
                # element doesnt exist on left
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                # element exists
                low = mid + 1
            else:
                # element not found on right
                high = mid - 1
    return -1