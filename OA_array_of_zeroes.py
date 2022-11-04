'''
https://leetcode.com/discuss/interview-question/2674448/Google-OA-or-Array-of-Zeroes-(HackerEarth-OA)
'''


def arrayOfZeroes(arr, m):
    left, right = 1, max(arr)
    while left < right:
        mid = (left + right) // 2
        if sum([(x-1)//mid + 1 for x in arr]) <= m:
            right = mid
        else:
            left = mid + 1
    return left
