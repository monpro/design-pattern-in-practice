import logging
logging.basicConfig(level=logging.INFO)


def loggingDecorator(func):

  def wrapperLogging(*args, **kwargs):
    logging.info(f"execute function {func.__name__}")
    return func(*args, **kwargs)

  return wrapperLogging


@loggingDecorator
def testFunction(a, b):
  return a + b


if __name__ == "__main__":
  print(testFunction(1, 3))
