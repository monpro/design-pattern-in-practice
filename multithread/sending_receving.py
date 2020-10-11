def generateNumbers():
  num = 0
  while True:
    num += 1
    k = (yield num)
    # # return the value to outside
    # yield num
    # # the value sent from outside
    # k = yield
    print(k)


if __name__ == "__main__":
  generator = generateNumbers()
  value = next(generator)
  print('received in main function {0}'.format(value))

  for i in range(10):
    value = generator.send(i + 10)
    print('received in main function {0}'.format(value))
