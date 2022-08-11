import numpy as np
import matplotlib.pyplot as plt

filedata= np.loadtxt("/home/dhanush/Softwares/files_vs/DSP3.2.txt")

l= len(filedata)
print(l)

fig,axs=plt.subplots(1,figsize=(10,10))
plt.stem(range(0,l),filedata)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
