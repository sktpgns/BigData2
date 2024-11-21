import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor  # 적용모델 : K 최근접 이웃 회귀 모델
from sklearn.model_selection import train_test_split  # 훈련 / 검증 셋트 분할 함수


mpg = sns.load_dataset(('mpg'))
print(mpg.info())

mpg.dropna(inplace=True)
# print(mpg.info())
# print(mpg.head())
# print(mpg.tail())
print(mpg.describe())