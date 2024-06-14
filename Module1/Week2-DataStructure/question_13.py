def my_function(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


if __name__ == "__main__":
    print(my_function(4))
