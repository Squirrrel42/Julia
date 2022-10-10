import numpy as np
import matplotlib.pyplot as plt


length = 500

re = np.linspace(-2, 2, length)
im = np.linspace(-2, 2, length)

img = np.zeros((length, length))

c = 1j

for i in range(length):
    for j in range(length):
        z = re[i] + im[j] * 1j

        for k in range(300):
            z = z ** 2 + c

            if(np.abs(z) > 2):
                img[j, i] = k
                break

plt.imshow(img)
plt.show()