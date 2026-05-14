# packages
import numpy as np
import matplotlib.pyplot as plt
# Mounting Google Drive
from google.colab import drive
drive.mount('/content/drive')

# import data
data = np.loadtxt("/content/drive/MyDrive/Colab Notebooks/fem/error.dat")

h = data[:,0]
errH1 = data[:,1]
errL2 = data[:,2]
errLinf = data[:,3]

plt.figure(figsize=(4,8))

plt.loglog(h, errH1, 'o-', linewidth=2.5, label="H1 error")
plt.loglog(h, errL2, 's-', linewidth=2.5, label="L2 error")
plt.loglog(h, errLinf, '^-', linewidth=2.5, label="MAX error")

plt.xlabel("h")
plt.ylabel("error")
plt.grid(True, which="both")
plt.legend()
plt.savefig('/content/drive/MyDrive/Colab Notebooks/fem/error.png',dpi=300, bbox_inches='tight')
plt.show()
