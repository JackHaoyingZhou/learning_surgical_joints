# from learning_surgical_joints.joint_data.joint_pos_recorder import JointPosLoader
import pickle

# m,l = JointPosLoader.load_by_prefix(prefix='JP#2021-06-28 13',folder_path='./joint_data/new_goal')
#
# jp_values = []
#
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         jp_values.append(m[i][j]['pos'])
# print(jp_values)

# with open(name,'wb') as fp:
#     pickle.dump(jp_values,fp)

# name_1 = './1/goal1.pickle'
# name_1 = './joint_data/1/test1.pickle'
# name_2 = 'train_data_new.pickle'
# name_2 = './joint_data/1/test1.pickle'
# name_2 = '/home/jack/catkin_ws_surgical/src/learning_surgical_joints/train_data_1.pickle'
with open(name_1,'rb') as fp:
    itemlist_1 = pickle.load(fp)
#
# with open(name_2,'rb') as fp:
#     itemlist_2 = pickle.load(fp)

# itemlist_3 = []
# for i_item in range(len(itemlist_2)):
#     np_ap = itemlist_2[i_item]
#     list_ap = list(np_ap.reshape(6))
#     itemlist_3.append(list_ap)
#
# with open('test_1.pickle','wb') as fp:
#     pickle.dump(itemlist_3,fp,protocol=2)
# #
# print(itemlist_2[0])
# # print(itemlist_2[0])
# print(itemlist_2[-1])
# # print(itemlist_2[-1])
