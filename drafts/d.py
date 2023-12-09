import numpy as np
import parselmouth
x = '/Users/226/Desktop/записи/2 армяне радость/1.wav'
def formants_praat(x):
    sound = parselmouth.Sound(x)  # read the sound
    pitch = sound.to_pitch()
    pitch = pitch.selected_array['frequency']
    formants = sound.to_formant_burg(time_step=0.010, maximum_formant=5000)

    f1_list, f2_list = [], []
    for t in formants.ts():
        f1 = formants.get_value_at_time(1, t)
        f2 = formants.get_value_at_time(2, t)
        # f3 = formants.get_value_at_time(3, t)
        # f4 = formants.get_value_at_time(4, t)
        if np.isnan(f1): f1 = 0
        if np.isnan(f2): f2 = 0
        # if np.isnan(f3): f3 = 0
        # if np.isnan(f4): f4 = 0
        f1_list.append(f1)
        f2_list.append(f2)
        # f3_list.append(f3)
        # f4_list.append(f4)


    return f1_list, f2_list
formants_praat(x)
print(formants_praat(x))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_graph(array, color):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(len(array))
    y = np.zeros(len(array))
    z = array
    ax.scatter(x, y, z, c=color)
    ax.set_xlabel('Index')
    ax.set_ylabel('Y')
    ax.set_zlabel('Value')
    plt.show()




f1_list = formants_praat(x)
f2_list = formants_praat(у)

plot_3d_graph(f1_list, 'r')
plot_3d_graph(f2_list, 'b')