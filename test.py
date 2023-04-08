import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {}
# количество шариков
N = 10000
# количество уровней
level = 20
for _ in range(N):
    index = 0
    for _ in range(level):
        index += np.random.choice([-1, 1])
    data.setdefault(index, 0)
    data[index] += 1

# Set the font scale
sns.set(font_scale=1.5)

# Create the bar plot using seaborn
sns.barplot(x=list(data.keys()), y=list(data.values()))
#
# # Set the x-axis label and rotate the labels
# plt.xlabel('Index')
# plt.xticks(rotation=45)
#
# # Set the y-axis label
# plt.ylabel('Count')
#
# # Set the title
# plt.title('Distribution of Index')
#
# # Adjust the figure size
# plt.figure(figsize=(12, 6))
#
# # Show the plot
# plt.show()