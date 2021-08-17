import typing as tp


class Solution:
    @staticmethod
    def find_ind(pre_sum: tp.List, n: int, val: int) -> int:
        start_ind, end_ind = 0, n - 1
        ans = -1

        while start_ind <= end_ind:
            mid = (start_ind + end_ind) // 2
            if pre_sum[mid][0] <= val:
                ans = mid
                start_ind = mid + 1
            else:
                end_ind = mid - 1

        return ans

    @classmethod
    def longest_positive(cls, number_list: tp.List[int]) -> int:
        number_list_len = len(number_list)
        max_len = 0
        pre_sum = []
        current_sum = 0
        min_ind: tp.List = [None] * number_list_len

        for i in range(0, number_list_len):
            current_sum = current_sum + number_list[i]
            pre_sum.append([current_sum, i])

        pre_sum.sort()
        min_ind[0] = pre_sum[0][1]

        for i in range(1, number_list_len):
            min_ind[i] = min(min_ind[i - 1], pre_sum[i][1])

        current_sum = 0
        for i in range(0, number_list_len):
            current_sum = current_sum + number_list[i]

            if current_sum >= 0:
                max_len = i + 1
            else:
                # Check for prefix array with sum >= 0
                ind = cls.find_ind(pre_sum, number_list_len, current_sum)
                if ind != -1 and min_ind[ind] < i:
                    max_len = max(max_len, i - min_ind[ind])

        return max_len
