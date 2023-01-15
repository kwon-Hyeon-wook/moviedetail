import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

a=pd.read_csv('../Data/영화상세정보.csv', encoding='cp949')
b=pd.read_csv('../Data/영화상세정보_크레딧.csv', encoding='cp949')
c=pd.read_csv('../Data/영화상세정보_참여사.csv', encoding='cp949')

a=a[['제명','유형구분','국가구분','제작년도','길이구분','장르','상영시간','KMDb 영화정보관리번호']]
b=b[['크레딧명','인명','KMDb 영화정보관리번호']]
c=c[['크레딧명','참여사명','KMDb 영화정보관리번호']]
c=c.rename(columns={'크레딧명':'참여/제작'})
movie=pd.merge(pd.merge(a,b),c)
plt.rcParams.update({'font.family':'Malgun Gothic'})


# 1. 넷플릭스에서 제작에 참여한 영화?
netflix = movie.query('참여사명 == "넷플릭스"')
# print(list(set(netflix['제명'])))

# 2. 가장 많은 영화제작에 참여한 참여사 5개
best_maker=movie['참여사명'].value_counts()\
    .to_frame('n')\
    .rename_axis('참여사명')
# print(list(best_maker.index)[:5])

# 3 100회 미만 영화 제작한 해 중에서 제작년도에 따른 영화의 수를 그래프로 표현
year_data=a['제작년도'].value_counts()
print(year_data)
year_data = year_data.rename_axis('year').to_frame('n').query('n<100')
sns.lineplot(data=year_data,x='year',y='n')
# plt.show()

# 4 가장 영화를 많이 제작한 해
# print(list(a['제작년도'].value_counts().index)[0])

# 5 영화의 길이구분(장편,단편,중편)에 따라서 상영시간의 차이를 보이기
sns.boxplot(data=a,x='길이구분',y='상영시간')
# plt.show()


# 6 영화 유형구분에 따른 상영시간 평균
# type_time=a.groupby('유형구분',as_index=False).agg(mean_time=('상영시간','mean'))
# print(type_time)
# sns.barplot(data=type_time,x='유형구분',y='mean_time')
plt.show()