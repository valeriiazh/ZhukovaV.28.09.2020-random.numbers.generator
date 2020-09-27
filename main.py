def print_random_numbers():

    from random import randint

    lst = [randint(0, 9) for i in range(15)]
    print(lst)


print_random_numbers()
