import pandas as pd
df_unique_number=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/milestone_content_uniquenumber.xlsx',sheet_name='unique_number')
#print(df_unique_number)

data_set=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/milestone_duplicates_removezerotime.xlsx')
#print(data_set)

data_set['milestone_unique']=''
#print(data_set)



for i in range(241298):
    for j in range(800):
        if data_set.milestone[i]== df_unique_number.milestone_number[j]:
            data_set.milestone_unique[i]= df_unique_number.unique_number[j]

print(data_set)
'''
for i in range(10):
    for j in range(10):
        if data_set.milestone[i]== df_unique_number.milestone_number[j]:
            data_set.milestone_unique[i]= df_unique_number.unique_number[j]



print(data_set)

'''