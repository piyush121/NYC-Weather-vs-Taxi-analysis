from matplotlib import pyplot
from matplotlib import style
import numpy as np

style.use('ggplot')

time,numTrips = np.loadtxt('part-00000',
				unpack = True,
				delimiter = ',')
pyplot.plot(time,numTrips)

pyplot.title('Epic Chart')
pyplot.ylabel('Number of trips')
pyplot.xlabel('Time period')

pyplot.show()