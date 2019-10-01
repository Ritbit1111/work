import pandas as pd
import numpy as np
df = pd.read_csv('new_list.csv')
roll = np.array(df['Roll No'])
saved_roll_list = roll
dict = {}
duplicate = 0
for i,r in enumerate(roll):
    if dict.get(r):
        duplicate += 1
        print (f'Duplicate at {i}')
    else :
        dict.update({r:i})
# print (roll)
set_list=[]
while len(roll)>7:
    new_set = np.random.choice(roll, 5, replace=False)
    roll = np.setdiff1d(roll, new_set)
    set_list.append(list(new_set))
set_list.append(list(roll))
print (set_list)
# print (saved_roll_list)

student_dict = {}
for index,set_ in enumerate(set_list):
    [student_dict.update({r:index}) for r in set_]
print (student_dict)

