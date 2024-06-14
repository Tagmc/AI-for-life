def my_function(integers, number=1):
    for i in integers:
        if i == number:
            return True
    return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    print(my_function(my_list, 2))
