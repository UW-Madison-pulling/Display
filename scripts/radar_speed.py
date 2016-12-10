import pandas as pd
import glob
import os
import math
import numpy as np
import matplotlib.pyplot as plt

path = "../../radar_tests/"

data = {}
angle = 35
speed_of_light = 6.706e+8

os.chdir(path)
for file in glob.glob("*.csv"):
    temp = pd.read_csv(file)
    name = file[:file.rindex("_")]
    if name in data:
        data[str(name)] = data[str(name)].append(temp)
    else:
        # create empty pandas dataframe
        data[str(name)] = pd.DataFrame({'duration': []})

max = 0
for mph in data.keys():
    if data[mph]['frequency'].size > max:
        max = data[mph]['frequency'].size

arr = np.zeros(shape=(3, max))
i = 0
for mph in data.keys():
    f_not = data[mph]["frequency"]
    trial_speed = float(mph[:mph.index("_")])
    f_d = 2 * trial_speed * (f_not / speed_of_light) * math.cos(math.radians(angle))
    speed = (f_d * speed_of_light) / (2 * f_not * math.cos(math.radians(angle)))
    speed = np.array(speed)
    offset = max - speed.size
    arr[i] = np.concatenate((speed, np.zeros(offset)), axis=0)
    i = i + 1

# ax = pd.DataFrame(np.rot90(arr, 3), columns=data.keys()[::-1])
# ax.plot()
# plt.show()
