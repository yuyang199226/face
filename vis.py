#import matplotlib as mpl
#mpl.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility

def display(dataSet):
    for c_id, d in dataSet.items():
        # print(c_id,d)
        x = [ i[0] for i in d]
        y = [ i[1] for i in d]
        if c_id == 0:
            c = 'r'
        elif c_id == 1:
            c = 'b'
        else:
            c= 'g'
        plt.scatter(x, y,c=c, label=str(c_id))

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend(loc='upper left')
    plt.show()
