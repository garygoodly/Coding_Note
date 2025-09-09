################# Ver 1 ##########################################

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            while j < len(nums):
                left = j + 1
                right = len(nums) - 1
                while (left < right):
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while (left < right and nums[left] == nums[left - 1]):
                            left += 1
                        right -= 1
                        while (left < right and nums[right] == nums[right + 1]):
                            right -= 1
                    else:
                        right -= 1
                while ((j < len(nums) - 3) and nums[j] == nums[j + 1]):
                    j += 1
                j += 1
        return ans
    
############################### Ver 2 #############################################
class Solution(object):
    def fourSum(self, nums, target):
      ans = []

      def nSum(l, r, target, n, path, ans):
        if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
          return
        if n == 2:
          while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
              ans.append(path + [nums[l], nums[r]])
              l += 1
              while nums[l] == nums[l - 1] and l < r:
                l += 1
            elif summ < target:
              l += 1
            else:
              r -= 1
          return

        for i in range(l, r + 1):
          if i > l and nums[i] == nums[i - 1]:
            continue

          nSum(i + 1, r, target - nums[i], n - 1, path + [nums[i]], ans)

      nums.sort()
      nSum(0, len(nums) - 1, target, 4, [], ans)
      return ans

###################### Ver 3 ###########################################
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        s=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k=j+1
                l=len(nums)-1
                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ==target:
                        s.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
                        k+=1
                        l-=1
                    elif summ>target:
                        l-=1
                    else:
                        k+=1
        lst=list(s)
        return lst

        