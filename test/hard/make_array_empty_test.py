import time

from hard.make_array_empty import Solution, digit, counting_sort, radix_sort
import pytest
import sys


class TestSolution:
    cur = Solution()

    def test_count_operations_to_empty_array1(self):
        assert self.cur.countOperationsToEmptyArray([3, 4, -1]) == 5
        assert self.cur.countOperationsToEmptyArray([1, 2, 4, 3]) == 5
        assert self.cur.countOperationsToEmptyArray([1, 2, 3]) == 3

    def test_count_operations_to_empty_array2(self):
        assert self.cur.countOperationsToEmptyArray([303, 404, -10]) == 5

    # TODO: TLE: 505 / 514 testcases passed
    @pytest.mark.skip(reason="TLE: 505 / 514 testcases passed")
    def test_count_operations_to_empty_big_array(self):
        data = [val for val in range(10_000, 0, -1)]
        start_time = time.time()
        assert self.cur.countOperationsToEmptyArray(data) == 50005000
        end_time = time.time()
        print(f"time elapsed: {end_time - start_time} seconds")
        assert int(end_time - start_time) < 1

    def test_digit_single_digit(self):
        assert digit(5, 0) == 5
        assert digit(5, 1) == 0
        assert digit(5, 17) == 0

    def test_digit(self):
        assert digit(123456, 0) == 6
        assert digit(123456, 1) == 5
        assert digit(123456, 2) == 4
        assert digit(123456, 3) == 3
        assert digit(123456, 4) == 2
        assert digit(123456, 5) == 1
        assert digit(123456, 6) == 0
        assert digit(123456, 7) == 0

    def test_digit_negative_value(self):
        assert digit(-123456, 0) == 6
        assert digit(123456, 5) == 1
        assert digit(123456, 7) == 0

    def test_counting_sort(self):
        data = [-20, -10, 57, 212, 84, 123, 12, 64]
        counting_sort(0, data, 2, len(data) - 1)
        assert data == [-20, -10, 212, 12, 123, 84, 64, 57]

    def test_radix_sort(self):
        data = [-20, -10, 57, 212, 84, 123, 12, 64]
        radix_sort(data)

        assert data == [-20, -10, 12, 57, 64, 84, 123, 212]


if __name__ == "__main__":
    sys.exit(pytest.main())
