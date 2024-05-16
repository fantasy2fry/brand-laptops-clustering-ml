# this script will split the data into data for us and validators

import pandas as pd
from sklearn.model_selection import train_test_split

# load the data
data=pd.read_csv("../data/laptops.csv")

# split the data
for_us, for_validators = train_test_split(data, test_size=0.3, random_state=42)

# save the data
for_us.to_csv("../data/modelers_data.csv", index=False)
for_validators.to_csv("../data/validators_data.csv", index=False)
#%%
