import math

def is_number(n):
  try:
    float(n)
  except ValueError:
    return False
  return True

def calc_activation_func (x , act_name ):
  alpha = 0.01
  if (act_name != 'sigmoid' and act_name != 'relu' and act_name != 'elu'):
    return 'ten_function_user is not supported'
  if (is_number(x) == False):
    return 'x must be number'
  if (act_name == 'sigmoid'):
    return (1 / (1 + math.pow(math.e, -x)))
  if (act_name == 'elu'):
    if (x <= 0):
      return alpha * (math.pow(math.e, x) - 1)
    else:
      return x
  if (act_name == 'relu'):
    if (x <= 0):
      return 0
    else:
      return x
    
if __name__ == '__main__':
  print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))