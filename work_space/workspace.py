import pandas as pd
df_raw=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/milestone.xlsx')
#print(df_2)


# <중복제거>
df_refine=df_raw.drop_duplicates()

#print(df_refine)

df_refine_astype = df_refine.astype({'created_at': 'str','updated_at':'str'})

df_temporary_1=pd.DataFrame()
df_temporary_2=pd.DataFrame()
df_temporary_1 = df_temporary_1.copy()
df_temporary_2 = df_temporary_2.copy()
df_temporary_1=df_refine_astype['created_at'].str.split(" ")
df_temporary_2=df_refine_astype['updated_at'].str.split(" ")
df_temporary_1=df_temporary_1.str[-1]
df_temporary_2=df_temporary_2.str[-1]

result = pd.concat([df_refine,df_temporary_1,df_temporary_2],axis=1)
result.columns=['person','milestone','grade','done_day_after_birth','created_at','updated_at','created_hour','updated_hour']




# <00시 제거>
final_result=pd.DataFrame()
final_result=result[result.created_hour!='00:00:00.000']
#print(final_result)




# <milestone_number / unique_milestone_number mapping>
milestone_content_uniquenumber=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/milestone_content_uniquenumber_test_ver.xlsx',index=False)
#milestone_duplicates_removezerotime=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/work/milestone_duplicates_removezerotime.xlsx',index=False)
milestone_nuique_number_join = final_result.join(milestone_content_uniquenumber.set_index('milestone_number')['unique_number'], on='milestone')

#print(milestone_nuique_number_join)




# <done_day_after_birth (생후일수) 지정해서 분석할 수 있도록 하는 기능>
a=int(input("==========done_day_after_start_date=========="))
b=int(input("==========done_day_after_due_date=========="))

condition_1=milestone_nuique_number_join['done_day_after_birth']>=a
condition_2=milestone_nuique_number_join['done_day_after_birth']<=b
milestone_date_range=milestone_nuique_number_join[condition_1 & condition_2]
#print(milestone_date_range)




# <person,gender_info mapping>
gender_set=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/raw/milestone_gender.xlsx',index=False)
sub_df_gender_join = milestone_date_range.join(gender_set.set_index('person_id')['gender'], on='person')
#print(sub_df_gender_join)

#sub_df_gender_join.to_excel(excel_writer='C:/Users/홍예지/Desktop/프릭스헬스케어/work/mapping_application_final_dataset_gender_join.xlsx',index=False)

# <done_day_after_birth, milestone_unique sorted>
df_result= sub_df_gender_join.sort_values(by=["unique_number","done_day_after_birth"], ascending=[True,True])

gender_input=str(input("==========gender_choice==========\n<answer: m / f / both>"))

if gender_input == 'm':
    condition_3 = df_result['gender'] =='M'
    final_dataset = df_result[condition_3]
    condition_3 = sub_df_gender_join['gender'] =='M'
    final_dataset = sub_df_gender_join[condition_3]

if gender_input == 'f':
    condition_4 = df_result['gender'] == 'F'
    final_dataset = df_result[condition_4]
    condition_4 = sub_df_gender_join['gender'] == 'F'
    final_dataset = sub_df_gender_join[condition_4]

if gender_input == 'both':
    final_dataset = df_result
    final_dataset = sub_df_gender_join


print(final_dataset)

