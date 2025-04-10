import numpy

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
      )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

numpy.random.shuffle(rolls)
print(rolls)
print("Type: ", type(rolls))
print("Functions: ", dir(rolls))

print(rolls.tolist())
print(rolls.mean())

rolls + 10
print(rolls)

print(rolls <= 3)

# ************************************************************************************
xlist = [[1, 2, 3], [2, 4, 6], ]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# Get the last element of the second row of our numpy array
print(x[1, -1])
