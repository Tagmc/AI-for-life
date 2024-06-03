import math

def is_number(n):
  try:
    float(n)
  except ValueError:
    return False
  return True

def calc_elu(x):
  alpha = 0.01
  if (is_number(x) == False):
    return "x must be number"
  if (x <= 0):
    elu_output = alpha * (math.pow(math.e, x) - 1)
  else:
    elu_output = x
  return elu_output

if __name__ == "__main__":
  answer = calc_elu(-1)
  if (is_number(answer)):
    print(round(answer, 2))
  else:
    print(answer)