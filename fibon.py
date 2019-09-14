def fibonacci_number(n):
  assert n>=0
  f0, f1 = 0, 1
  for i in range(n-1):
    f0, f1 = f1, f0 + f1
  return(f1)
  
def print_results(a):
  print(a)
  
  
if __name__ == '__main__':
  c = fibonacci_number(100)
  print_results(c)