import pickle
import numpy as np
import matplotlib.pyplot as plt
import pickle
from GaitAnaylsisToolkit.LearningTools.Runner import TPGMMRunner
from GaitAnaylsisToolkit.LearningTools.Trainer import TPGMMTrainer
import numpy.polynomial.polynomial as poly

def read_file():
    data = []
    for joint in range(6):
        data.append([])

    for i in range(1,6):
        file = "/home/nathanielgoldfarb/learning_surgical_joints/joint_data_task/test" + str(i) +"_pose.pickle"
        with open(file, 'rb') as handle:
            raw_data = pickle.load(handle)
        my_data = np.array(raw_data)
        for j in range(6):
            data[j].append(my_data[:,j])
    return data


def train(my_data, name):


    trainer = TPGMMTrainer.TPGMMTrainer(demo=[my_data[0], my_data[1],my_data[2],my_data[3],my_data[4],my_data[5]],
                                        file_name=name,
                                        n_rf=30,
                                        dt=0.01,
                                        reg=[1e-2, 1e-2,1e-2, 1e-2,1e-2, 1e-2],
                                        poly_degree=[25,25,25,25,25,25])

    my_model = trainer.train()
    print(my_model)



def plot_raw(my_data,runner_file=None):

    f, ax = plt.subplots(6)

    for ii, traj in enumerate([my_data[0], my_data[1],my_data[2],my_data[3],my_data[4],my_data[5]]):
        for demo in traj:
            ax[ii].plot(demo, '-')



    if runner_file is not None:
        runner = TPGMMRunner.TPGMMRunner(runner_file)
        path = runner.run()
        for i in range(6):
            ax[i].plot(path[:, i], linewidth=4)

    plt.show()


if __name__ == '__main__':
    data = read_file()
    train(data,"task_space")
    plot_raw(data,"task_space")