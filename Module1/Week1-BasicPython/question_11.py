import math

def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)

def approx_sinh(x, n):
  answer = 0
  for i in range(n):
    answer += ((math.pow(x, 2 * i + 1) / factorial(2 * i + 1)))
  return answer;

if __name__ == "__main__":
  print(round(approx_sinh(x=3.14, n=10), 2))