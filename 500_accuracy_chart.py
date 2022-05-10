import numpy as np
import matplotlib.pyplot as plt

data = [[481, 450, 418.58], [468, 422, 390.79], [433, 405, 378.15]]
percentages = [['96.2%', '90.0%', ''], ['93.6%', '84.4%', ''], ['86.6%', '81.1%', '']]

_, ax = plt.subplots(figsize=(12,8))

bar_width = 0.3
bar1 = np.arange(len(data[0]))
bar2 = [x + bar_width for x in bar1]
bar3 = [x + bar_width for x in bar2]

p1 = ax.bar(bar1, data[0], width=bar_width)
p2 = ax.bar(bar2, data[1], width=bar_width)
p3 = ax.bar(bar3, data[2], width=bar_width)

ax.bar_label(p1, ['Combined', 'Combined', 'Combined'])
ax.bar_label(p2, ['Edge focus', 'Edge focus', 'Edge focus'])
ax.bar_label(p3, ['Light mask', 'Light mask', 'Light mask'])

ax.bar_label(p1, [str(x) + '\n\n' + y if y != '' else x for x, y in zip(data[0], percentages[0])], label_type='center')
ax.bar_label(p2, [str(x) + '\n\n' + y if y != '' else x for x, y in zip(data[1], percentages[1])], label_type='center')
ax.bar_label(p3, [str(x) + '\n\n' + y if y != '' else x for x, y in zip(data[2], percentages[2])], label_type='center')

plt.title('Accuracy measures for the 500 Images of the Riew View dataset')
plt.xlabel('Metrics', fontweight='bold', fontsize=15)
plt.ylabel('Number of cars', fontweight='bold', fontsize=15)
plt.xticks([r + bar_width for r in range(len(data[0]))], ['LP detected', 'OCR passed', 'OCR Sum Score'])

plt.show()
