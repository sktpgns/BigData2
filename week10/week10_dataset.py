import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import title

titanic = sns.load_dataset('titanic')



#print(titanic['embarked'], titanic['deck'], titanic['class'])
#print(titanic['deck'])
#titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#print(titanic['deck'])

#print(titanic['survived'])

# sns.countplot(data=titanic, x="survived")
# plt,title(('survived (0 = No,1 = Yes)'))
# plt.xlabel('survived')
# plt.ylabel('count')
# plt.show()

# gender_survval = titanic.groupby(by='sex')['survived'].mean()
# print(type(gender_survval))
gender_survval = titanic.groupby(by='sex')['survived'].mean().reset_index()
print(type(gender_survval))

sns.barplot(data=gender_survval, x = 'sex', y='survived')
plt.title('survival rate by gender')
plt.ylabel('survival rate')
plt.show()

