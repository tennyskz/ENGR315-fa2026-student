
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows; set a comma as the delimiter

### Your code here ###
data = np.loadtxt(path, delimiter=',', skiprows=2)

# save each vector as own variable

### Your code here ###
time = data[:,0]
MLII = data[:,1]
V1 = data[:,2]


# use matplot lib to generate a single

### Your code here ###

plt.title('EKG data')
plt.xlabel('Time (s)')
plt.ylabel('V1 (mV)')
plt.plot(time, V1, label='V1 Signal')
plt.plot(time, MLII, label='MLII Signal')
plt.legend()
plt.show()