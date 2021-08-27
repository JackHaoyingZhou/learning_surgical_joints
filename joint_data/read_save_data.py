from learning_surgical_joints.joint_data.joint_pos_recorder import JointPosLoader
import pickle

m,l = JointPosLoader.load_by_prefix(prefix='JP#2021-06-28 13',folder_path='./joint_data/new_goal')

jp_values = []

for i in range(len(m)):
    for j in range(len(m[0])):
        jp_values.append(m[i][j]['pos'])
print(jp_values)
with open('test_new','wb') as fp:
    pickle.dump(jp_values,fp)

with open('test_new','rb') as fp:
    itemlist = pickle.load(fp)
