LIST = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 300]

NEW_LIST = [LIST[el] for el in range(1, len(LIST)) if LIST[el] > LIST[el - 1]]

print(NEW_LIST)
