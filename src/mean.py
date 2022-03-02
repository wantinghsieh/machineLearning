import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print("mean=" + str(x))

x = numpy.median(speed)

print("median=" + str(x))

x = stats.mode(speed)
print(x)
