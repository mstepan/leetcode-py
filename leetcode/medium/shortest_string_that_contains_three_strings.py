class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        s1 = Solution.combine3(a, b, c)
        s2 = Solution.combine3(a, c, b)

        s3 = Solution.combine3(b, a, c)
        s4 = Solution.combine3(b, c, a)

        s5 = Solution.combine3(c, a, b)
        s6 = Solution.combine3(c, b, a)

        return Solution.smallest([s1, s2, s3, s4, s5, s6])

    @staticmethod
    def combine3(a: str, b: str, c: str) -> str:
        first = Solution.combine2(a, b)
        second = Solution.combine2(first, c)
        return second

    @staticmethod
    def combine2(a: str, b: str) -> str:

        if a in b:
            return b
        elif b in a:
            return a

        min_len = min(len(a), len(b))

        res = a + b

        for length_to_check in range(1, min_len + 1):
            a_suffix = a[len(a) - length_to_check :]
            b_prefix = b[0:length_to_check]

            if a_suffix == b_prefix:
                res = a + b[length_to_check:]

        return res

    @staticmethod
    def smallest(values: list[str]) -> str:
        smallest_str = values[0]

        for i in range(1, len(values)):
            if len(values[i]) < len(smallest_str):
                smallest_str = values[i]
            elif len(values[i]) == len(smallest_str):
                smallest_str = min(values[i], smallest_str)

        return smallest_str
