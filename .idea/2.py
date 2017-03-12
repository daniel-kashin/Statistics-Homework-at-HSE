from functools import reduce
import numpy.random as rand
import numpy as np
import matplotlib.pyplot as plt

MEAN = 3
SCALE = 1.0/MEAN
VARIANCE = SCALE**(-2)
ELEMENTS_COUNT = 8
QUANTIL = 2.365
EXPERIMENT_COUNT = 10000

def test_mean(mean = MEAN, el_count = ELEMENTS_COUNT):
    scale = 1.0 / mean
    first_true = 0
    first_false = 0
    for i in range(0, EXPERIMENT_COUNT):
        selection = rand.exponential(1 / scale, el_count)
        average =  np.sum(selection) / el_count
        value = ((average - mean) * (el_count - 1)**(1.0/2)) / VARIANCE**(1.0/2)
        if (value < QUANTIL and value > -QUANTIL):
            first_true += 1
        else:
            first_false += 1
    return (first_true, first_false)




# first task
first_true, first_false = test_mean()
print("H0 true " + str(first_true) + " times")
print("H0 false " + str(first_false) + " times")
print("Probabolity of first type mistake is: " + str(float(first_false)/EXPERIMENT_COUNT) + '\n')



# second task
for i in range(2):
    seq_count = 8 if i == 0 else 50

    counters = []
    points = []
    for mean in np.arange(1.0,5.5,0.5):
        first_true, first_false = test_mean(mean, seq_count)
        counters.append(mean)
        points.append(float(first_false) / EXPERIMENT_COUNT)

    plt.figure()
    plt.title(str(seq_count) + " elements in a sequence")
    plt.plot(counters, points, "-bo")
    plt.xlabel("Mean")
    plt.ylabel("Probability that H0 is false")




plt.show()