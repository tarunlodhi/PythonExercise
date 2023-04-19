def removeDuplicates(self, nums):
    if len(nums)<2:
        return len(nums)
    pre = 0

    for cur in range(0,len(nums)):
        if nums[cur]!=nums[pre]:
            pre+=1
            nums[pre]=nums[cur]
    return pre+1

removeDuplicates([0,1,1,2,3,3,5])
