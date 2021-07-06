import matplotlib.pyplot as plt
import numpy as np

from joint_data.joint_pos_recorder import JointPosLoader
import pickle
from GaitAnaylsisToolkit.LearningTools.Runner import TPGMMRunner
from GaitAnaylsisToolkit.LearningTools.Trainer import TPGMMTrainer
import numpy.polynomial.polynomial as poly



def temp_test():

    data = read_data()[0]
    resampled = resample(data)
    t = np.linspace(0, 1, len(data)  )
    plt.plot(t, data  )
    t = np.linspace(0, 1, len(resampled))
    plt.plot(t, resampled)
    plt.show()


def read_data():

    demos = {}
    for i in range(6):
        demos[i] = []


    for file in [1,2,3,4,5]:
        m, l = JointPosLoader.load_by_prefix(prefix='JP#2021-06-28 13', folder_path='./joint_data/'+str(file))
        demo = {}

        for i in range(6):
            demo[i] = []
        for i in range(len(m)):
            for j in range(len(m[0])):
                pos = m[i][j]['pos']
                for k in range(len(pos)):
                    demo[k].append(pos[k])
        for key, value in demo.items():
            demos[key].append( np.array(demo[key]) )

    return demos



def resample(data):

    t = np.linspace(0, 1, len(data))
    coefs = poly.polyfit( t , data, 3)
    ffit = poly.Polynomial(coefs)  # instead of np.poly1d
    t = np.linspace(0,1,100)
    y_fit = ffit(t)
    return y_fit

def plot_raw(my_data,runner_file=None):

    for traj in [my_data[0],my_data[1]]:
        for demo in traj:
            plt.plot(demo)

    with open(runner_file, "rb") as f:
        unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
        scores = unpickler.load()
        print(scores)

    runner = TPGMMRunner.TPGMMRunner(runner_file)
    path = runner.run()
    plt.plot(path[:, 0], linewidth=4)
    if runner_file is not None:
        runner = TPGMMRunner.TPGMMRunner(runner_file)
        path = runner.run()
        for i in range(2):
            plt.plot(path[:, i], linewidth=4)

    plt.show()




def train(my_data):
    # trainer = TPGMMTrainer.TPGMMTrainer(demo=[my_data],
    #                                     file_name="first_test",
    #                                     n_rf=15,
    #                                     dt=0.01,
    #                                     reg=[1e-4],
    #                                     poly_degree=[3])


    trainer = TPGMMTrainer.TPGMMTrainer(demo=[my_data[0], my_data[1] ],
                                        file_name="new_test",
                                        n_rf=30,
                                        dt=0.01,
                                        reg=[1e-5, 1e-5],
                                        poly_degree=[15,15])
    trainer.train()


if __name__ == '__main__':
    # #temp_test()
    my_data = read_data()
    train(my_data)
    plot_raw(my_data,"new_test.pickle")