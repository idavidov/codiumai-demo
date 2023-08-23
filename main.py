from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return 0
        
        # Find the minimum and maximum numbers in the list
        min_num, max_num = min(nums), max(nums)
        
        # Calculate the bucket size and count
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1
        
        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Populate buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        # Calculate the maximum gap
        max_gap = 0
        prev_max = min_num
        for i in range(bucket_count):
            if buckets[i][0] == float('inf'):  # Skip empty buckets
                continue
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        return max_gap


