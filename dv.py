import matplotlib.pyplot as plt
import numpy as np

x = [1, 3, 5]
y = [2, 4, 6]

x2 = [4, 5, 6]
y2 = [6, 7, 9]

plt.plot(x, y, label='First Data')
plt.plot(x2, y2, label='Second Data')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out dudtties')
plt.legend()
plt.show()
