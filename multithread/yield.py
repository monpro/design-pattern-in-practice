def isPrime(n):
  if n <= 1:
    return False
  if n <= 3:
    return True

  if n % 2 == 0 or n % 3 == 0:
    return False

  # All prime number is in the form of 6k + 1 or 6k - 1
  i = 5

  while i*i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6

  return True


def getPrimes():
  num = 1
  while True:
    if isPrime(num):
      yield num
    num += 1


if __name__ == "__main__":
  generator = getPrimes()
  for i in range(10):
    print(next(generator))