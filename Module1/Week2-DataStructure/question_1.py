def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        tmp = 1e-10
        for j in range(k):
            tmp = max(tmp, num_list[i + j])
        result.append(tmp)
    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))
