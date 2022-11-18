'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        def count_and_return(num, divider):
            return num // divider, num % divider
        def add_roman(ans, ten_symbol, five_symbol, five_count, one_symbol, one_count):
            if one_count == 4:
                if five_count:
                    ans += [one_symbol, ten_symbol]
                else:
                    ans += [one_symbol, five_symbol]
            else:
                ans += [five_symbol] * five_count + [one_symbol] * one_count

        Ms, num = count_and_return(num, 1000)
        Ds, num = count_and_return(num, 500)
        Cs, num = count_and_return(num, 100)
        Ls, num = count_and_return(num, 50)
        Xs, num = count_and_return(num, 10)
        Vs, num = count_and_return(num, 5)
        Is, num = count_and_return(num, 1)

        ans = []
        ans += ['M'] * Ms
        add_roman(ans, 'M', 'D', Ds, 'C', Cs)
        add_roman(ans, 'C', 'L', Ls, 'X', Xs)
        add_roman(ans, 'X', 'V', Vs, 'I', Is)
        return ''.join(ans)
