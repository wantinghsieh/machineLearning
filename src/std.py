import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)
print("std=" + str(x))

speed2 = [32,111,138,28,59,77,97]

x = numpy.std(speed2)

print("std=" + str(x))

x = numpy.var(speed2)
print("var=" + str(x))
