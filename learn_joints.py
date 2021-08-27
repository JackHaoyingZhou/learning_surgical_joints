import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# matplotlib.use('TkAgg')
# plt.interactive(False)

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
        #m, l = JointPosLoader.load_by_prefix(prefix='JP#2021-06-28 13', folder_path='./joint_data/'+str(file))
        m, l = JointPosLoader.load_by_prefix(prefix='JP#2021-08-17', folder_path='./joint_data/'+str(file))
        demo = {}

        for i in range(6):
            demo[i] = []
        for i in range(len(m)):
            for j in range(len(m[0])):
                pos = m[i][j]['pos']
                # print(pos)
                for k in range(len(pos)):
                    demo[k].append(pos[k])
        for key, value in demo.items():
            # print(demo[key])
            demos[key].append(smooth(demo[key]) )

    return demos


def smooth(x):
    N=10
    return np.convolve(x, np.ones(N)/N, mode='valid')

def resample(data):

    t = np.linspace(0, 1, len(data))
    coefs = poly.polyfit( t , data, 3)
    ffit = poly.Polynomial(coefs)  # instead of np.poly1d
    t = np.linspace(0,1,100)
    y_fit = ffit(t)
    return y_fit

def plot_raw(my_data,runner_file=None):

    f, ax = plt.subplots(6)

    for ii, traj in enumerate([my_data[0], my_data[1],my_data[2],my_data[3],my_data[4],my_data[5]]):
        for demo in traj:
            ax[ii].plot(smooth(demo), '-')




    if runner_file is not None:
        runner = TPGMMRunner.TPGMMRunner(runner_file)
        path = runner.run()
        for i in range(6):
            ax[i].plot(path[:, i], linewidth=4)

    plt.show(block=True)
    plt.interactive(False)




def train(my_data, name):


    # # data set 1
    # trainer = TPGMMTrainer.TPGMMTrainer(demo=[my_data[0], my_data[1],my_data[2],my_data[3],my_data[4],my_data[5]],
    #                                     file_name=name,
    #                                     n_rf=30,
    #                                     dt=0.01,
    #                                     reg=[1e-2, 1e-2,1e-2, 1e-2,1e-2, 1e-2],
    #                                     poly_degree=[25,25,25,25,25,25])


    # data set 2
    trainer = TPGMMTrainer.TPGMMTrainer(demo=[my_data[0], my_data[1],my_data[2],my_data[3],my_data[4],my_data[5]],
                                        file_name=name,
                                        n_rf=30,
                                        dt=0.01,
                                        reg=[1e-2, 1e-2,1e-2, 1e-2,1e-2, 1e-2],
                                        poly_degree=[25,25,25,25,25,25])

    my_model = trainer.train()
    # print(my_model)


if __name__ == '__main__':
    # #temp_test()
    my_data = read_data()
    name = "joint_data_2"
    # train(my_data, name)
    plot_raw(my_data, name)
