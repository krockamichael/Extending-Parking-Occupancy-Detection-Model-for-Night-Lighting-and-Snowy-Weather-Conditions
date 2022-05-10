import numpy as np
import matplotlib.pyplot as plt

data = [[211.92, 160.52, 162.54], [182.39, 134.14, 137.39]]

_, ax = plt.subplots(figsize=(8,6))

bar_width = 0.4
bar1 = np.arange(len(data[0]))
#bar2 = [x + bar_width for x in bar1]
#bar3 = [x + bar_width for x in bar2]

p1 = ax.bar(bar1, data[1], width=bar_width)
p2 = ax.bar(bar1, [x - y for x, y in zip(data[0], data[1])], width=bar_width, bottom=data[1])
#p3 = ax.bar(bar3, data[2], width=bar_width)

#ax.bar_label(p1, ['Combined', 'Combined'])
ax.bar_label(p2, data[0])
#ax.bar_label(p3, ['Light mask', 'Light mask'])

ax.bar_label(p1, [str(x) + '\n\n' + y for x, y in zip(data[1], 3 * ['Tesseract\nOCR'])], label_type='center')
ax.bar_label(p2, 3 * ['Other'], label_type='center')
#ax.bar_label(p3, [str(x) + '\n\n' + y if y != '' else x for x, y in zip(data[2], percentages[2])], label_type='center')

plt.title('Temporal measures for the 500 Images of the Riew View dataset')
plt.ylabel('Time in seconds', fontweight='bold', fontsize=15)
plt.xticks(bar1, ['Combined', 'Edge focus', 'Light mask'])

plt.show()
