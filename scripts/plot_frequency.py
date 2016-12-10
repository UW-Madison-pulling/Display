import pandas as pd
import glob, os
import numpy as np
import matplotlib.pyplot as plt

path = "../../radar_tests/"

data = {}

os.chdir(path)
for file in glob.glob("*.csv"):
    temp = pd.read_csv(file)
    name = file[:file.rindex("_")]
    if name in data:
        data[str(name)] = data[str(name)].append(temp)
    else:
        # create empty pandas dataframe
        data[str(name)] = pd.DataFrame({'duration' : []})

max = 0
for mph in data.keys():
    if data[mph]['frequency'].size > max:
        max = data[mph]['frequency'].size

arr = np.zeros(shape=(3,max))
i = 0
for mph in data.keys():
    temp = data[mph]['frequency'].as_matrix()
    offset = max - temp.size
    arr[i] = np.concatenate((temp, np.zeros(offset)), axis=0)
    i = i + 1

ax = pd.DataFrame(np.rot90(arr, 3), columns=data.keys()[::-1])
ax = ax.plot.area(stacked=False)
ax.set_ylabel('Frequency')
ax.set_xlabel('Time from start')

plt.show()
