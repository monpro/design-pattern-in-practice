if __name__ == "__main__":
  listInteger = list()
  listInteger.append(1)
  listInteger.append(2)
  listInteger.append(3)

  iterator = listInteger.__iter__()
  print("iterator of list: {0}".format(str(iterator)))

  print("iterator of list: {0}".format(str(listInteger.__getitem__(2))))

  print("iterator is iterator(iterator) = {0}".format(str(iterator is iter(iterator))))

  listIntegerGene = iter(listInteger)

  print("iterator generated {0}".format(str(listIntegerGene)))

  for element in listInteger:
    print(element)

  for element in listIntegerGene:
    print(element)
