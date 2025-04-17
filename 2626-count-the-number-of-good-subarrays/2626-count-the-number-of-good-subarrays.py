'''
in  k = 10 not even possible because length is less than k
[1,1,1,1,1]
out -> 1

k = 2, represents pairs
 x     x y y 
[3,1,4,3,2,2]   => 22, 33
 z   x z y y x
[3,1,4,3,2,2,4] => 22, 33, 44
[1,4,3,2,2,4]   => 22, 44
[4,3,2,2,4]     => 22, 44

contiguous - remove None, 0th, nth - 1
out -> 4

plan:

'''

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans 