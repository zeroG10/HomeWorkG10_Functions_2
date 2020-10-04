import random


def find_argument():
    # list_length = int(input())
    list_range = range(int(input('Enter the number of arguments in the list: ')))
    a = int(input('Start the generation with a number: '))
    b = int(input('Finish the generation on the number: '))
    some_list = [random.randint(a, b) for l in list_range]
    print(some_list)
    print(some_list[int(input('Enter the position in the list that interests you: '))])


find_argument()

