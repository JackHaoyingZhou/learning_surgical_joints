import numpy as np
import rospy
import pickle
from GaitAnaylsisToolkit.LearningTools.Runner import TPGMMRunner
from GaitAnaylsisToolkit.LearningTools.Trainer import TPGMMTrainer
import numpy.polynomial.polynomial as poly


if __name__ == '__main__':
    rospy.init_node("runner")
    # open the config file and create the runner
    runner_file = "all_joints.pickle"
    runner = TPGMMRunner.TPGMMRunner(runner_file)
    rate = rospy.Rate(10) # some control rate to publish the traj

    # Use this to change the start and goal
    # start = np.array([ [0.0],[0.0],[0.0],[0].0,[0.0],[0.0] ])
    # runner.update_start(start)
    # goal = np.array([ [0.0],[0.0],[0.0],[0].0,[0.0],[0.0] ])
    # runner.update_goal(goal)

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

    with open('test_data_origin','wb') as fp:
        pickle.dump(q_list,fp)

    with open('test_data_origin','rb') as fp:
        itemlist = pickle.load(fp)
