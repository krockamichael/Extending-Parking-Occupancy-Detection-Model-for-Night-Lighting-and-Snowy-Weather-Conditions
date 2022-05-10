import numpy as np
import matplotlib.pyplot as plt


data = [[476, 486, 461, 454],
        [24, 14, 39, 46]]

_, ax = plt.subplots(figsize=(12,8))

bar_width = 0.4
bar1 = np.arange(4)
bar2 = [x + bar_width for x in bar1]

p1 = ax.bar(bar1, data[0], width=bar_width, edgecolor='grey', label='shape')
p2 = ax.bar(bar2, data[1], width=bar_width, edgecolor='grey', label='stuff')
ax.bar_label(p1, ['Rectangle', 'Black-White', 'No', 'Yes'])
ax.bar_label(p2, ['Square', 'Colored', 'Yes', 'No'])
ax.bar_label(p1, data[0], label_type='center')
ax.bar_label(p2, data[1], label_type='center')

plt.title('Characteristics of the 500 Images of the Riew View dataset')
plt.xlabel('Attributes', fontweight='bold', fontsize=15)
plt.ylabel('Number of cars', fontweight='bold', fontsize=15)
plt.xticks([r + bar_width / 2 for r in range(4)], ['Shape', 'Colored', 'Tilted', 'Clear'])

plt.show()
