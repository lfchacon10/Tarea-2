import matplotlib.pylab as plt
import numpy as np

#Para t=0
datos = np.genfromtxt("amp.dat", delimiter=",")
t= datos[:,0]
u1= datos[:,1]
u2= datos[:,2]
u3= datos[:,3]
#v1= datos[:,4]
#v2= datos[:,5]
#v3= datos[:,6]

plt.figure()
plt.grid()
plt.title("Amplitudes")
plt.plot(t[:1000],u1[:1000], label="Amplitud1")
plt.plot(t[:1000],u2[:1000], label="Amplitud2")
plt.plot(t[:1000],u3[:1000], label="Amplitud3")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitud1.png")
plt.show()

u1ampMax=[]
u2ampMax=[]
u3ampMax=[]

max=int(len(t)/1000)
for i in range(max):
    limInf= i*1000
    limSup= (i+1)*1000
    u1Act=u1[limInf:limSup]
    u2Act=u2[limInf:limSup]
    u3Act=u3[limInf:limSup]

    u1ampMax.append(np.amax(u1Act))
    u2ampMax.append(np.amax(u2Act))
    u3ampMax.append(np.amax(u3Act))

w=np.linspace(0.2,3.0,len(u1ampMax))

plt.figure()
plt.grid()
plt.title("Amplitudes")
plt.plot(w,u1ampMax,"o-", label="Maxima Amplitud1")
plt.plot(w,u2ampMax,"o-", label="Maxima Amplitud2")
plt.plot(w,u3ampMax,"o-", label="Maxima Amplitud3")
plt.ylabel("Amplitud")
plt.yscale("Log")
plt.xlabel("Frecuencia de forzamiento")
plt.legend()
plt.show()
