'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kith(start1, end1, start2, end2, k):
            if start1 == end1:
                return nums2[start2 + k]
            if start2 == end2:
                return nums1[start1 + k]
            idx1, idx2 = start1 + (end1 - start1) // 2, start2 + (end2 - start2) // 2
            val1, val2 = nums1[idx1], nums2[idx2]
            # the Kith is in the right side of at least one value between val1, val2 
            # i.e. we can guarantee it's not on the left side of min(val1, val2)
            if k > (end1 - start1) // 2 + (end2 - start2) // 2:
                if val1 > val2:
                    return kith(start1, end1, idx2 + 1, end2, k - (end2 - start2) // 2 - 1)
                else:
                    return kith(idx1 + 1, end1, start2, end2, k - (end1 - start1) // 2 - 1)
            # Kith is guaranteed to be on the left side of max(val2, val2)
            else:
                if val1 > val2:
                    return kith(start1, idx1, start2, end2, k)
                else:
                    return kith(start1, end1, start2, idx2, k)

        m, n = len(nums1), len(nums2)
        if (n + m) % 2:
            return kith(0, m, 0, n, (n+m) // 2)
        else:
            return (kith(0, m, 0, n, (n+m) // 2 - 1) + kith(0, m, 0, n, (n+m) // 2)) / 2
