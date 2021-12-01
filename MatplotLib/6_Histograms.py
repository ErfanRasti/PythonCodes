"""."""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data/data_3.csv')
ids = data['Responder_id']
ages = data['Age']

bins = np.arange(10, 110, step=10)

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = int(data['Age'].median())
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xticks(bins)
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
