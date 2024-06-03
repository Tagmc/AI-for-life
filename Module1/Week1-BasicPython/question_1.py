import math

def check_type_data(n):
  return isinstance(n, int)

def is_number(n):
  try:
    float(n)
  except ValueError:
    return False
  return True

def calc_f1_score(tp, fp, fn):
  if (check_type_data(tp) == False):
    return "tp must be int"
  if (check_type_data(fp) == False):
    return "fp must be int"
  if (check_type_data(fn) == False):
    return "fn must be int"
  precision = (tp / (tp + fp))
  recall = (tp / (tp + fn))
  f1_score = 2 * (precision * recall) / (precision + recall)
  return f1_score

if __name__ == "__main__":
  answer = calc_f1_score(tp=2, fp=4, fn=5)
  if (is_number(answer)):
    print(round(answer, 2))
  else:
    print(answer)