def radix_sort(arr, type):
    len_ = len(str(max(arr)))
    if type == 'gen_short_ints' or 'gen_ints' or 'gen_time':
        rang = 10
    elif type == 'gen_strings':
        rang = 26

    for i in range(len_):
        B = [[] for k in range(rang)]  # список длины range, состоящий из пустых списков
        for x in arr:
            figure = x // 10 ** i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A = A + B[k]
    return A