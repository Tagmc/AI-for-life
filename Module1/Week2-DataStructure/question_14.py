def my_function(x):
    answer = ''.join(reversed(x))
    return answer


if __name__ == "__main__":
    x = 'apricot'
    print(my_function(x))
