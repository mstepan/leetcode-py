import math


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        mul: int = int(math.ceil(low / k))

        cnt: int = 0

        while mul * k <= high:
            val = mul * k
            if is_beautiful_number(val):
                cnt += 1
            mul += 1

        return cnt


even_decimal_digits = {0, 2, 4, 6, 8}


def is_beautiful_number(val: int) -> bool:

    left_val: int = val

    even_digits_cnt = 0
    odd_digits_cnt = 0

    while left_val > 0:
        digit = left_val % 10

        if digit in even_decimal_digits:
            even_digits_cnt += 1
        else:
            odd_digits_cnt += 1

        left_val //= 10

    return even_digits_cnt == odd_digits_cnt
