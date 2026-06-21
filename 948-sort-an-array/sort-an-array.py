class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l:int,r:int):
            if l>=r:
                return
            mid = (l+r)//2
            merge_sort(l,mid)
            merge_sort(mid+1,r)
            merge(l,mid,r)
        def merge(l:int,mid:int,r:int):
            temp = []
            i,j=l,mid+1
            while i<=mid and j<=r:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            if i<= mid:
                temp.extend(nums[i:mid+1])
            if j<=r:
                temp.extend(nums[j:r+1])
            for idx in range(l,r+1):
                nums[idx] = temp[idx -l]
        merge_sort(0, len(nums)-1)
        return nums                        