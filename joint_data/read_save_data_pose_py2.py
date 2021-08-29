from __future__ import print_function
# from joint_pos_recorder import JointPosLoader
import pickle
from psmFK import *
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

with open('./5/test5.pickle','rb') as fp:
    jp_values = pickle.load(fp)

Pose = []
for i in range(len(jp_values)):
    T_f = compute_FK(jp_values[i])
    Pos = T_f[0:3,3]
    Rot = T_f[0:3,0:3]
    euler = tf.transformations.euler_from_matrix(Rot,axes='rxyz')
    Pos_x = float(Pos[0])
    Pos_y = float(Pos[1])
    Pos_z = float(Pos[2])
    Rot_x = float(euler[0]) # alpha
    Rot_y = float(euler[1]) # beta
    Rot_z = float(euler[2]) # gamma
    Pose_f = [Pos_x, Pos_y, Pos_z, Rot_x, Rot_y, Rot_z]
    Pose.append(Pose_f)

with open('./5/test5_pose.pickle','wb') as fp:
    pickle.dump(Pose,fp)

with open('./5/test5_pose.pickle','rb') as fp:
    pose_values = pickle.load(fp)


