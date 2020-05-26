import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in arr:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)