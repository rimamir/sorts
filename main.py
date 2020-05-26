import time

from bubbleSort import bubble_sort
from combSort import comb_sort
from heapSort import heap_sort
from mergeSort import merges_sort
from quickSort import quick_sort
from shellSort import shell_sort
from radixSort import radix_sort

from generate_lists import gen_short_ints, gen_ints, gen_strings, gen_time

sorts = [bubble_sort, quick_sort, comb_sort, heap_sort, merges_sort, shell_sort, sorted]

gen_lists = [gen_short_ints, gen_ints, gen_strings, gen_time]
list_type = ['rnd', 'half_sorted', 'equal']
lists_len = [500, 5000, 50000, 500000]


def measure_time(sort, list_, type_=None):
    start = (time.time())
    if type_ is not None:
        sort(list_, type_)
    else:
        sort(list_)
    end = (time.time())
    return sort.__name__, end - start


with open('result.txt', 'w') as file:
    for type_ in list_type:
        file.write(f'{type_}\n\n')
        for generate in gen_lists:
            file.write(f'{generate.__name__}\n')
            for len_ in lists_len:
                file.write(f'{len_}\n')
                for sort in sorts:
                    if sort.__name__ == 'bubble_sort' and len_ > 5000:
                        continue
                    if sort.__name__ == 'radix_sort':
                        measured_time = measure_time(sort=sort,
                                                     list_=generate(type_, len_),
                                                     type_=generate.__name__)
                    else:
                        measured_time = measure_time(sort=sort,
                                                     list_=generate(type_, len_))
                    file.write(f'{measured_time[0]}, {measured_time[1] * 1000}\n')
                file.write('____________\n')
            file.write('----------------------------\n')
