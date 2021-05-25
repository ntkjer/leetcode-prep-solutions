class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Intution:
            Brute-force solution is to combine nums1 + nums2 and merge-sort
            Too much memory, and the time complexity is O(m + n).

            PS asks for O(lg(m + n))     

            Instead, we only care about getting the middle most element
            We only really need up to half of nums1 + nums2 to find the median.
            The median can be defined as the mid most elem that perfectly partitions a 
            sequence of integers into two equal halves.

            To find the middle we need to find four items, two for each array.
            We need the max elements to the left of the middle for both
            And we need the min elements to the right st:
            
            When we have: max_left_x <= min_right_y
                          max_left_y <= min_right_x

                           we are done. 

            For odd len nums1 + nums2:
                The mid most elem will be max(max's) since we only need left extreme.
            If even: 
                We need the average of the max(max's) + min(min's)
            
            We us binary search to traverse search space in lg (m + n) time, finding the min
            amount of elements to pick from x

            We offset y's from x, which is still valid for above. 
            This is why implementation is only correct iff m < n.
        """
        m, n = map(len, (nums1, nums2))
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        start, end = 0, m
        total_len = m + n
        
        while start <= end:
            x_idx = start + (end - start) // 2
            y_idx = ((m + n + 1) // 2) - x_idx
            
            max_left_x = float('-inf') if x_idx == 0 else nums1[x_idx - 1]
            min_right_x = float('inf') if x_idx == m else nums1[x_idx]
                
            max_left_y = float('-inf') if y_idx == 0 else nums2[y_idx - 1]
            min_right_y = float('inf') if y_idx == n else nums2[y_idx]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if total_len & 1:
                    return float(max(max_left_x, max_left_y))
                else:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2

            elif max_left_x > min_right_y:
                end = x_idx - 1
            else:
                start = x_idx + 1
                        
            
        
        
        
            
        
        