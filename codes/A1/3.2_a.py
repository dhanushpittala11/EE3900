import numpy as np
import matplotlib.pyplot as plt
xfile= "/home/dhanush/Softwares/files_vs/DSP3.2_X.txt"
xfiledata= np.loadtxt("/home/dhanush/Softwares/files_vs/DSP3.2_X.txt")

k = len(xfiledata)

fig,axs=plt.subplots(1,figsize=(10,10))
plt.stem(range(0,k),xfiledata)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
