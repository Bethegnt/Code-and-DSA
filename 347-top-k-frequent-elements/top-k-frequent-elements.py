class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in m:
                m[nums[i]]=1
            else:
                m[nums[i]]+=1
        bucket = [[] for _ in range(n+1)]
        for num,count in(m.items()):
            bucket[count].append(num)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return []               
        