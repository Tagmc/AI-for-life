import math

def calc_ae(y, y_hat):
  return abs(y - y_hat)

if __name__ == "__main__":
  y = 2
  y_hat = 9
  print(calc_ae(y, y_hat))