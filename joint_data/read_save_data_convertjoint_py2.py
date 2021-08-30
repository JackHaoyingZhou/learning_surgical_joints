from __future__ import print_function
# from joint_pos_recorder import JointPosLoader
import pickle
from psmIK import *
import tf


# m,l = JointPosLoader.load_by_prefix(prefix='JP#2021-08-17',folder_path='./1')
#
# jp_values = []
#
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         jp_values.append(m[i][j]['pos'])
# print(jp_values)

# with open('test_new.pickle','wb') as fp:
#     pickle.dump(jp_values,fp)
# with open('./1/test1.pickle','rb') as fp:
#     joint_values = pickle.load(fp)

# with open('./task_3.pickle','rb') as fp:
#     pose_values = pickle.load(fp)

with open('../goal_1/goal1_pose.pickle','rb') as fp:
    pose_values = pickle.load(fp)

# print(type(pose_values[0]))
#
# a_list = pose_values[0]
#
# p_x = float(a_list[0])
# p_y = float(a_list[1])
# p_z = float(a_list[2])
# alpha = float(a_list[3])
# beta = float(a_list[4])
# gamma = float(a_list[5])
#
# T_f = tf.transformations.euler_matrix(alpha,beta,gamma,axes='rxyz')
# T_f = np.mat(T_f)
# T_f[0,3] = p_x
# T_f[1,3] = p_y
# T_f[2,3] = p_z
# T_f = convert_mat_to_frame(T_f)
# jp_values = compute_IK(T_f)




Joint = []
for i in range(len(pose_values)):
    T_f = tf.transformations.euler_matrix(float(pose_values[i][3]), float(pose_values[i][4]), float(pose_values[i][5]), axes='rxyz')
    T_f = np.mat(T_f)
    T_f[0, 3] = float(pose_values[i][0])
    T_f[1, 3] = float(pose_values[i][1])
    T_f[2, 3] = float(pose_values[i][2])
    T_f = convert_mat_to_frame(T_f)
    jp_values = compute_IK(T_f)
    Joint.append(jp_values)

# print(Joint[-1])
# print(joint_values[-1])

with open('../test_pose3.pickle', 'wb') as fp:
    pickle.dump(Joint,fp)

with open('../test_pose3.pickle', 'rb') as fp:
    item_values = pickle.load(fp)


