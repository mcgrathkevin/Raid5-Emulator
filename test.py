oldData = bytearray([1, 2, 3])
newData = bytearray([1, 0, 2])
dataXOR = bytes(oldData ^ newData for (oldData, newData) in zip(oldData, newData))
print(str(dataXOR))
dataXOR_bytearr = bytearray(dataXOR)
print(str(dataXOR_bytearr))