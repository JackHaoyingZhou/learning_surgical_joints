import numpy as np
import rospy
import pickle
from GaitAnaylsisToolkit.LearningTools.Runner import TPGMMRunner
from GaitAnaylsisToolkit.LearningTools.Trainer import TPGMMTrainer
import numpy.polynomial.polynomial as poly


if __name__ == '__main__':
    rospy.init_node("runner")
    # open the config file and create the runner
    runner_file = "joint_space.pickle"
    runner = TPGMMRunner.TPGMMRunner(runner_file)
    rate = rospy.Rate(10) # some control rate to publish the traj

    # Use this to change the start and goal
    # start = np.array([ [-0.41540834595308324],[-0.21760656787167168],[1.441400568252263],[0.13108997751442897],[0.03153427435760321],[0.03153427435760321] ])
    # start = np.array([ [-0.40671161420953195],[-0.21982665763229683],[1.4317679106598609],[0.26573914624090833],[0.0028867430229473365],[0.7115770566056169] ])
    ### task space goal
    # start = np.array([ [-0.49918503042391105],[0.28165682335390063],[-1.1587630077028808],[1.6626135065258558],[-0.3292343363331438],[-2.8513431970531973] ])
    # start = np.array([[-0.5137730146510905], [0.2784229168588189], [-1.1638972084410133], [1.68812347787683],[-0.19467792784377203], [-2.712825200853556]])

    # runner.update_start(start)
    # goal = np.array([ [-0.2824755718720363],[-0.18461612454621512],[1.6996133250437584],[0.7461838252799323],[0.38462755010471666],[0.47757898786484215] ])
    # goal = np.array([ [-0.3913698125122527],[-0.12528189730754946],[1.5407188102983544],[0.2593524293972941],[0.8513889862374516],[0.4290786938889553] ])
    ### task goals
    # goal = np.array([ [-0.5380523267528037],[0.10639465839196165],[-1.2583591650295094],[0.817472725890319],[0.09827039311339075],[3.0874891760770296] ])
    #goal = np.array([[-0.44908647775421234], [0.26089858065572874], [-1.4650689438469748], [1.0640618572595462],[-0.566076490563442], [2.966329441416792]])
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

    # with open('joint_data_1.pickle','wb') as fp:
    #     pickle.dump(q_list,fp)
    #
    # with open('joint_data_1.pickle','rb') as fp:
    #     itemlist = pickle.load(fp)
