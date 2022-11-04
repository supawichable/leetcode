'''
1323. Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/
'''


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_lst = list(str(num))
        for i in range(len(num_lst)):
            if num_lst[i] == '6':
                num_lst[i] = '9'
                break
        return int(''.join(num_lst))

class Solution2:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))

# space: O(1)
class Solution3:
    def maximum69Number (self, num: int) -> int:
        first_six = -1
        i = 0
        tmp_num = num
        while tmp_num > 0:
            last_digit = tmp_num % 10
            if last_digit == 6:
                first_six = i
            tmp_num //= 10
            i += 1
        return num if first_six == -1 else num + 3*10**first_six