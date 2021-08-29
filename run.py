import numpy as np
import rospy
import pickle
from GaitAnaylsisToolkit.LearningTools.Runner import TPGMMRunner
from GaitAnaylsisToolkit.LearningTools.Trainer import TPGMMTrainer
import numpy.polynomial.polynomial as poly


if __name__ == '__main__':
    rospy.init_node("runner")
    # open the config file and create the runner
    runner_file = "joint_data_2.pickle"
    runner = TPGMMRunner.TPGMMRunner(runner_file)
    rate = rospy.Rate(10) # some control rate to publish the traj

    # Use this to change the start and goal
    # start = np.array([ [-0.41540834595308324],[-0.21760656787167168],[1.441400568252263],[0.13108997751442897],[0.03153427435760321],[0.03153427435760321] ])
    start = np.array([ [-0.40671161420953195],[-0.21982665763229683],[1.4317679106598609],[0.26573914624090833],[0.0028867430229473365],[0.7115770566056169] ])
    runner.update_start(start)
    # goal = np.array([ [-0.2824755718720363],[-0.18461612454621512],[1.6996133250437584],[0.7461838252799323],[0.38462755010471666],[0.47757898786484215] ])
    goal = np.array([ [-0.3913698125122527],[-0.12528189730754946],[1.5407188102983544],[0.2593524293972941],[0.8513889862374516],[0.4290786938889553] ])
    runner.update_goal(goal)

    # loop through the trajectory
    count = 0
    q_list = []
    while count < runner.get_length():
        runner.step()
        q = runner.x # pos
        qd = runner.dx # vel
        qdd = runner.ddx # accel
        # print(q)
        q_list.append(q)
        ##################################
        # send the desired position here #
        ##################################

        count = count + 1

        rate.sleep()

    with open('train_data_1.pickle','wb') as fp:
        pickle.dump(q_list,fp)

    with open('train_data_1.pickle','rb') as fp:
        itemlist = pickle.load(fp)
