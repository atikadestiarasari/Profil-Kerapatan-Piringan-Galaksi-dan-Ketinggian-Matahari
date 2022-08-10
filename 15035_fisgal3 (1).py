import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

z=np.arange(-6000,6000,100)
xi= np.loadtxt('histogram_t1.txt',usecols=[0])
y= np.loadtxt('histogram_t1.txt',usecols=[1])
xfilter=[]
yfilter=[]
xfilteri=[]
yfilteri=[]
x=[]

for i in range (len(xi)):
    x.append((xi[i]+0.05)*1000)
    if (xi[i]<-2 or  xi[i]>2):
        xfilter.append(x[i])
        yfilter.append(y[i])
    if (xi[i]<-3 or  xi[i]>3):
        xfilteri.append(x[i])
        yfilteri.append(y[i])
    

def thin(z):
    rho = rhoo*np.exp(-np.abs(z+zo)/h)
    return rho

def thick(z):
    rhot = rhoot*np.exp(-np.abs(z+zot)/ht)
    return rhot

def halo(z):
    rhoz = rhooz*np.exp(-np.abs(z+zoz)/hz)
    return rhoz

def func(x, a, b, c):
    return a*np.exp(-abs(x+b)/c)

popt, pcov = curve_fit(func, x, y,p0=(8e7,20, 20))
print (popt)
rhoo = popt[0]
zo = popt[1]
h = popt[2]

popy, pcov = curve_fit(func, xfilter, yfilter,p0=(4e7, 1, 200))
print (popy)
rhoot = popy[0]
zot = popy[1]
ht = popy[2]

popz, pcov = curve_fit(func, xfilteri, yfilteri,p0=(4e7, 1, 200))
print (popz)
rhooz = popz[0]
zoz = popz[1]
hz = popz[2]

plt.plot()
plt.plot(x,np.log(y),'r.')
plt.plot(z,np.log(thin(z)),label='Thin')
plt.plot(z,np.log(thick(z)),label='Thick')
plt.plot(z,np.log(halo(z)),label='Halo')
plt.legend()
plt.ylabel('ln (rho)')
plt.xlabel('z(pc)')
plt.savefig('fisgal3.png')
plt.ylim(0,20)
plt.show()