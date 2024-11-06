def fibonacci_series(n):

  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_series = [0, 1]
    for i in range(2, n):
      fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

n = int(input("Enter the number: "))
print(fibonacci_series(n))
