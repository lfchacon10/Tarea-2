import matplotlib.pylab as plt
import numpy as np

datos = np.genfromtxt("amp.dat", delimiter=",")
t= datos[:,0]
u1= datos[:,1]
u2= datos[:,2]
u3= datos[:,3]

plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 1*w")
plt.plot(t[28*1000:29*1000],u1[28*1000:29*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[28*1000:29*1000],u2[28*1000:29*1000], label="Amplitud2")
plt.plot(t[28*1000:29*1000],u3[28*1000:29*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudes.png")


plt.figure()
plt.grid()
plt.title("Amplitud 1 para frecuencia de forzamiento = 1*w")
plt.plot(t[28*1000:29*1000],u1[28*1000:29*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.ylabel("Amplitudes frecuencia de forzamiento = 1*w")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitud1.png")

plt.figure()
plt.grid()
plt.title("Amplitud 2 para frecuencia de forzamiento = 1*w")
plt.plot(t[28*1000:29*1000],u2[28*1000:29*1000], "orange",label="Amplitud2") #Entre 28 y 29 porque esos son los datos de 1*w
plt.ylabel("Amplitudes frecuencia de forzamiento = 1*w")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitud2.png")

plt.figure()
plt.grid()
plt.title("Amplitud 3 para frecuencia de forzamiento = 1*w")
plt.plot(t[28*1000:29*1000],u3[28*1000:29*1000],"g", label="Amplitud3") #Entre 28 y 29 porque esos son los datos de 1*w
plt.ylabel("Amplitudes frecuencia de forzamiento = 1*w")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitud3.png")

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
plt.savefig("amplitudesMax.png")


plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 0.4*w")
plt.plot(t[10*1000:11*1000],u1[10*1000:11*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[10*1000:11*1000],u2[10*1000:11*1000], label="Amplitud2")
plt.plot(t[10*1000:11*1000],u3[10*1000:11*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudes04.png")


plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 1.2*w")
plt.plot(t[39*1000:40*1000],u1[39*1000:40*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[39*1000:40*1000],u2[39*1000:40*1000], label="Amplitud2")
plt.plot(t[39*1000:40*1000],u3[39*1000:40*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudes12.png")


plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 1.7*w")
plt.plot(t[53*1000:54*1000],u1[53*1000:54*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[53*1000:54*1000],u2[53*1000:54*1000], label="Amplitud2")
plt.plot(t[53*1000:54*1000],u3[53*1000:54*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudes17.png")


plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 3*w")
plt.plot(t[99*1000:100*1000],u1[99*1000:100*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[99*1000:100*1000],u2[99*1000:100*1000], label="Amplitud2")
plt.plot(t[99*1000:100*1000],u3[99*1000:100*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudes30.png")




datos = np.genfromtxt("bono.dat", delimiter=",")
t= datos[:,0]
u1= datos[:,1]
u2= datos[:,2]
u3= datos[:,3]

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

w=np.linspace(0.2,100000,len(u1ampMax))
plt.figure()
plt.grid()
plt.title("Amplitudes")
plt.plot(w,u1ampMax,"o-", label="Maxima Amplitud1")
plt.plot(w,u2ampMax,"o-", label="Maxima Amplitud2")
plt.plot(w,u3ampMax,"o-", label="Maxima Amplitud3")
plt.ylabel("Amplitud")
#plt.xscale("Log")
plt.yscale("Log")
plt.xlabel("Frecuencia de forzamiento")
plt.legend()
plt.savefig("amplitudesMaxBono.png")

plt.figure()
plt.grid()
plt.title("Amplitudes para frecuencia de forzamiento = 64000*w")
plt.plot(t[64*1000:65*1000],u1[64*1000:65*1000], label="Amplitud1") #Entre 28 y 29 porque esos son los datos de 1*w
plt.plot(t[64*1000:65*1000],u2[64*1000:65*1000], label="Amplitud2")
plt.plot(t[64*1000:65*1000],u3[64*1000:65*1000], label="Amplitud3")
plt.ylabel("Amplitudes")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.savefig("amplitudesBONO.png")
