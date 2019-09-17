import numpy as np
import matplotlib.pyplot as plt

def f(x,a):
    y = (x-a)*(x-a**2)*(x-a**3)
    return(y)
x = np.linspace(-20,60,100)

plt.figure(figsize=(10,3))
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title(i+1)
    #plt.ylim(-100000,100000)
    plt.plot(x,f(x,i),'k')
    plt.grid(True)
plt.show()