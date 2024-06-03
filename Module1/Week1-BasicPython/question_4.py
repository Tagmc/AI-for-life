import math

def is_number(n):
  try:
    float(n)
  except ValueError:
    return False
  return True

def calc_sig(x):
  if (is_number(x) == False):
    return "x must be number"
  sigmoid_output = (1 / (1 + math.pow(math.e, -x)))
  return sigmoid_output

if __name__ == "__main__":
  answer = calc_sig(2)
  if (is_number(answer)):
    print(round(answer, 2))
  else:
    print(answer)