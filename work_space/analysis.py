import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.font_manager as fm
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

data_set=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/survival_average_female_ver2.xlsx')
data_set_m=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/survival_average_male_ver2.xlsx')
#print(data_set)
data=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/data_preprocessing_final_f_ver.xlsx')
data_m=pd.read_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/data_preprocessing_final_m_ver.xlsx')
'''
milestone_num=data_set['milestone_number'].tolist()
average=data_set['day_average'].tolist()
count=data_set['milestone_number'].max()
#print(count)

plt.title("<여자아이 마일스톤별 평균일자>",size=35)
plt.ylabel("day_average",size=20)
plt.xlabel("milestone_number",size=20)
plt.ylim(0,2800)
#plt.bar(milestone_num,average)
hist=plt.hist(milestone_num,bins=count,weights=average,density=False,cumulative=False,label='A'
          ,range=(data_set['milestone_number'].min(),data_set['milestone_number'].max()),color='c',linewidth=1.2)

plt.show()

plt.hist(data_set['milestone_number'],bins=10,color='orange')
plt.style.use('ggplot')
plt.rcParams['figure.figsize']=(15,5)
plt.rcParams['font.size']=15
plt.title('<남자아이 마일스톤별 평균>')
plt.xlabel('milestone')
plt.ylim(1,2800)
plt.show()
'''

group=data.groupby(["unique_number"])
#group.to_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/groupby_female.xlsx',index=False)
#group_size=group.size().reset_index(name='counts')
#print(group_size)
#group_size.to_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/groupby_female.xlsx',index=False)
#print(group.size().reset_index(name='counts'))

group_m=data_m.groupby(["unique_number"])
group_m_size=group_m.size().reset_index(name='counts')
group_m_size.to_excel('C:/Users/홍예지/Desktop/프릭스헬스케어/final_test/result_test/groupby_male.xlsx',index=False)
#print(group_m.size().reset_index(name='counts'))