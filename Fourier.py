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

#Implementación propia de Fourier
def fu (fun,N):
	n= np.size(fun)
	k= np.arange(0,n)
	F = np.zeros(N, dtype=np.complex)
	constante= -2*1j*np.pi
	for n in range (0,N):
		F[n]= np.sum( fun*np.exp( constante*k*(n/N) ) )
	return F


Fu= fu(f, len(f))
timestep = 0.1
freq = np.fft.fftfreq(len(f), d=timestep) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html

plt.figure()
plt.title("Transformada implementacion propia")
plt.plot(freq,Fu)
plt.grid()

FuS= fu(fS, len(fS))
timestep = 0.1
freqS = np.fft.fftfreq(len(fS), d=timestep) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html
plt.figure()
plt.title("Transformada Suma implementacion propia")
plt.plot(freqS,FuS)
plt.grid()
plt.show()
