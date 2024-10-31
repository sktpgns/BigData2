import seaborn as sns
import pandas as pd

print(sns.get_dataset_names())
#tutanic = sns.load_dataset('titanic')
mpg = sns.load_dataset('mpg')
print(mpg.head())


