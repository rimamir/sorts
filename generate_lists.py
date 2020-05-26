import random
import string
from datetime import datetime, timedelta


def half_sort(list_):
    return list_[:int(len(list_) / 2)] + sorted(list_[int(len(list_) / 2): len(list_)])


def gen_short_ints(type, list_len=50):
    if type == 'rnd':
        rand_nums = [random.randint(0, 10) for x in range(list_len)]
    elif type == 'half_sorted':
        temp_nums = [random.randint(0, 10) for x in range(list_len)]
        rand_nums = half_sort(temp_nums)
    elif type == 'equal':
        rand_nums = [1 for x in range(list_len)]
    return rand_nums


def gen_ints(type, list_len=50):
    if type == 'rnd':
        rand_nums = [random.randint(0, 500) for x in range(list_len)]
    elif type == 'half_sorted':
        type_nums = [random.randint(0, 500) for x in range(list_len)]
        rand_nums = half_sort(type_nums)
    elif type == 'equal':
        rand_nums = [111 for x in range(list_len)]
    return rand_nums


def gen_strings(type, list_len=50):
    letters = string.ascii_lowercase

    if type == 'rnd':
        strings_list = list()
        for i in range(list_len):
            strings_list.append(''.join(random.choice(letters) for i in range(5)))
    elif type == 'half_sorted':
        temp_strings = list()
        for i in range(list_len):
            temp_strings.append(''.join(random.choice(letters) for i in range(5)))
        strings_list = half_sort(temp_strings)
    elif type == 'equal':
        strings_list = ['aaaaa' for x in range(list_len)]
    return strings_list


def gen_time(type, list_len=50):
    max_year = datetime.now().year
    min_year = 1900

    if type == 'rnd':
        times_list = list()
        for i in range(list_len):
            start = datetime(1900, 1, 1, 00, 00, 00)
            years = max_year - min_year + 1
            end = start + timedelta(days=365 * years)
            time = start + (end - start) * random.random()
            times_list.append(int(str(time.year) + str(time.month) + str(time.day)))
    elif type == 'half_sorted':
        temp_list = list()
        for i in range(list_len):
            start = datetime(1900, 1, 1, 00, 00, 00)
            years = max_year - min_year + 1
            end = start + timedelta(days=365 * years)
            time = start + (end - start) * random.random()
            temp_list.append(int(str(time.year) + str(time.month) + str(time.day)))
        times_list = half_sort(temp_list)
    elif type == 'equal':
        times_list = [20001215 for x in range(list_len)]

    return times_list
