from tabula import read_pdf
import pandas as pd
df = read_pdf("765.pdf")
# print (df.head())
roll_series = list(df["Roll No."])
name_series = list(df["Name"])
roll_list = [roll for roll in roll_series]
name_list = [name for name in name_series]
# with open('roll_comma_seprtd.txt', 'w') as f:
#     for item in roll_list:
#         f.write("%s," % item)

df_roll = pd.DataFrame(roll_list)
df_name = pd.DataFrame(name_list)

# print (df_roll)
print (roll_series)
df_roll.to_csv("roll.csv", index=False, header=False)
df_name.to_csv("name.csv", index=False, header=False)
