import numpy as np
import matplotlib.pylab as plt

#Descarga los datos
dataSum= np.genfromtxt("signalSuma.dat")
tS=dataSum[0:,0]
fS=dataSum[0:,1]

data= np.genfromtxt("signal.dat")
t=data[0:,0]
f=data[0:,1]

#Plotea los datos
plt.figure()
plt.subplot(2,1,1)
plt.title("Senal suma")
plt.plot(tS,fS)
plt.grid()

plt.subplot(2,1,2)
plt.title("\n Senal")
plt.plot(t,f)
plt.grid()
plt.show()

#Implementación propia de Fourier
def fu (fun,N):
	n= np.size(fun)
	k= np.arange(0,n)
	F = np.zeros(N, dtype=np.complex)
	constante= -2*1j*np.pi
	for n in range (0,N):
		F[n]= np.sum( fun*np.exp( constante*k*(n/N) ) )
	return F
