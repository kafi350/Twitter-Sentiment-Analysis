

import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(
    [63.879, 63.661, 61.498, 63.330, 61.840, 61.612, 63.661],
    index = ['Naive Bayes', 'MNB', 'BernoulliNB', 'Logistic Regression', 'LinearSVC', 'SGD', 'Mixed Classifier']
)

#Set descriptions:
plt.title("Machine Learning Algorithms Performace and Accuracy")
plt.ylabel('Accuracy in Percent')
plt.xlabel('Algorithms')

#Set tick colors:
ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

#Plot the data:
my_colors = ['b','r','g','g','g']  #red, green, blue, black, etc.

s.plot(
    kind='bar',
    color=my_colors,
)

plt.show()