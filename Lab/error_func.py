import numpy as np
import matplotlib.pyplot as plt
a = 1
x = np.linspace(1,10,11)
y = [1.0, 1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1, 10.0]
plt.plot(x,y)
plt.show()

w = np.linspace(-6,9,11)
l = 0
it = len(x)
for i in range(it):
    l += (w*x[i]- y[i])**2
    plt.plot(w,l)

plt.xlabel('W')
plt.ylabel('Error')
plt.title('W vs Error')
plt.scatter(w,l,c='red')
plt.show()
