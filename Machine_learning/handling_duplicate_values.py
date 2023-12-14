# -*- coding: utf-8 -*-
"""handling_duplicate_values.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v8UIjOWoRG6lFvahGc-eM4gbssAtUbP6
"""

import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Anju', 'Arathi', 'Swathy','Arathi', 'Keerthana','Swathy', 'Alwin', 'Mridhul','Mridhul'],
    'Id': [1, 2,3,2,4,3,5,6,6],'Dept':['English','Maths','Chemistry','Maths','Physics','Chemistry','English','Malayalam','Malayalam']
}
df = pd.DataFrame(data)
duplicates = df.duplicated(['Name'])
print(duplicates)
df.drop_duplicates()
plt.figure(figsize=(8, 5))
plt.bar(df[duplicates]['Name'], 1, color='red', label='Duplicates')
plt.xlabel('Names')
plt.ylabel('Occurrences')
plt.title('Duplicate Values in Name Column')
plt.show()