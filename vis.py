#import matplotlib as mpl
#mpl.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
def three_D(dataSet):
    print("3D display...")
    from mpl_toolkits.mplot3d import Axes3D
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.scatter(dataSet[:,0], dataSet[:,1], dataSet[:,2])
    plt.show()



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


if __name__ == '__main__':
    dataSet = [
            [0,1,0],
            [1,1,1],
            [2,1,3],
            [4,1,9],
            [5,2,12],
            [3,-3,6],
            ]
    three_D(np.asarray(dataSet))
