import random
def find_argument(list_range, start_num, stop_num, position):
    some_list = [random.randint(start_num, stop_num) for l in range(list_range)]
    print(some_list, some_list[position], sep='\n')


find_argument(11, 2, 50, 5)


