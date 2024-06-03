def calc_se(y, y_hat):
  return (y - y_hat) * (y - y_hat)

if __name__ == "__main__":
  print(calc_se(2, 1))