import math

def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

def approx_sin(x, n):
  answer = 0
  for i in range(n):
    answer += (math.pow(-1, i) * (math.pow(x, 2 * i + 1) / factorial(2 * i + 1)))
  return answer;

if __name__ == "__main__":
  print(round(approx_sin(x=3.14, n=10), 4))