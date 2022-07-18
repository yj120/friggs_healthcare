import pandas as pd

new_dataset=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/mapping_application_final_dataset.xlsx',index=False)
new_dataset

#=====================2번 마일스톤==========================
condition_2=new_dataset['milestone_unique']==2
test_dataset=new_dataset[condition_2]
#test_dataset


#============================2번 마일스톤===================================
df_sorted_by_date = test_dataset.sort_values(by='done_day_after_birth' ,ascending=True)

df_sorted_by_date #unique_number 즉 고유 마일스톤의 데이터 갯수(오름차순)

# =====================2번 마일스톤==========================
date_list = []
date_list_full = []
grade_count = 0
grade_count_list = []
for i in range(len(df_sorted_by_date) - 1):
    if df_sorted_by_date.iloc[i, 3] != df_sorted_by_date.iloc[i + 1, 3]:  # done_day_after_birth가 다를때
        date_list.append(df_sorted_by_date.iloc[i, 3])  # 일단 date에 추가
    if df_sorted_by_date.iloc[i, 2] == 4:
        grade_count = grade_count + 1
    if df_sorted_by_date.iloc[i, 3] == df_sorted_by_date.iloc[i + 1, 3]:  # done_day_after_birth가 같을때
        continue
    if len(date_list) > 4:  # date_list가 5개면 date_list_full에 리스트 append, date_list 리셋
        grade_count_list.append(grade_count)
        date_list_full.append(date_list)
        date_list = []
        grade_count = 0

# date_list_full
# grade_count_list


index_list = []
for j in range(len(date_list_full)):
    index_list.append(date_list_full[j][0])

# print(index_list)

data_set = pd.DataFrame()
data_set['index_list'] = index_list
data_set['date_list_full'] = date_list_full
data_set['grade_count_list'] = grade_count_list

# data_set


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#=====================2번 마일스톤====================================
xs=data_set['index_list'].to_list() #dy_day(데이터 프레임)의 index(날짜, 시간)를 리스트로 저장
ys=data_set['grade_count_list'].to_list() #dy_day(테이터 프레임)의 volume 필드를 리스트로 저장
#plt.figure(figsize=(10, 6))
plt.style.use('default')
plt.rcParams['figure.figsize'] = (10,6)
plt.rcParams['font.size'] = 15
plt.xlabel('done_day_after_birth')
plt.ylabel('4 grade_count')
plt.bar(xs, ys, width=10, color='skyblue')
plt.title('milestone_unique_number : 2')
