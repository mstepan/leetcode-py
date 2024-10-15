"""
2659. Make Array Empty
https://leetcode.com/problems/make-array-empty/
# TODO: TLE: 505 / 514 testcases passed
"""

from collections import deque


class Solution:
    """
    time: O(N*10), b/c Radix sort has linear complexity
    space: O(N)
    """

    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        if nums is None:
            raise ValueError("'nums' is None")

        data: deque[int] = deque(nums)

        radix_sort(nums)

        min_idx: int = 0
        ops_count: int = 0

        while len(data) > 0:
            cur = data.popleft()

            if cur == nums[min_idx]:
                min_idx += 1
            else:
                data.append(cur)

            ops_count += 1

        return ops_count


def radix_sort_chunk(data: list[int], left: int, right: int):
    if right - left + 1 < 2:
        return

    for digit_idx in range(max_digits_count(data)):
        counting_sort(digit_idx, data, left, right)


def radix_sort(data: list[int]):
    # partition negative and positive values
    partition_idx = partition(data)

    radix_sort_chunk(data, 0, partition_idx)
    radix_sort_chunk(data, partition_idx + 1, len(data) - 1)

    if partition_idx > 0:
        left = 0
        right = partition_idx

        while left < right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    return data


def partition(data: list[int]) -> int:
    boundary: int = -1

    for i in range(len(data)):
        if data[i] < 0:
            data[boundary + 1], data[i] = data[i], data[boundary + 1]
            boundary += 1

    return boundary


def max_digits_count(data: list[int]) -> int:
    max_digits_cnt = 0

    for val in data:
        max_digits_cnt = max(max_digits_cnt, count_decimal_digits(val))

    return max_digits_cnt


def count_decimal_digits(value: int) -> int:
    value = abs(value)

    digits_count: int = 0
    while value != 0:
        value //= 10
        digits_count += 1

    return digits_count


def digit(value: int, idx: int) -> int:
    return abs(value) // int(10**idx) % 10


def counting_sort(digit_idx: int, data: list[int], left: int, right: int):
    """
    This sorting algorithm should be stable, otherwise Radix sort using the least significant digit won't work.
    """
    counter_table = [0 for _ in range(10)]

    for value in data[left : right + 1]:
        counter_table[digit(value, digit_idx)] += 1

    prefix_sum(counter_table)

    data_chunk_copy = data[left : right + 1]

    for val in reversed(data_chunk_copy):
        digit_value = digit(val, digit_idx)
        idx_to_put = left + counter_table[digit_value] - 1
        data[idx_to_put] = val
        counter_table[digit_value] -= 1


def prefix_sum(counter_table: list[int]):
    for i in range(1, len(counter_table)):
        counter_table[i] += counter_table[i - 1]
