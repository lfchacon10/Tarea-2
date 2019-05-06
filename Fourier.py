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
plt.title("Señal suma")
plt.plot(tS,fS)
plt.grid()

plt.subplot(2,1,2)
plt.title("Señal")
plt.plot(t,f)
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.savefig("Senal.png")


#Implementación propia de Fourier
def fu (fun,N):
	n= np.size(fun)
	k= np.arange(0,n)
	F = np.zeros(N, dtype=np.complex)
	constante= -2*1j*np.pi
	for n in range (0,N):
		F[n]= np.sum( fun*np.exp( constante*k*(n/N) ) )
	return F


#Graficas Fourier
N= len(f)

Fu= fu(f,N )
#timestep = t[1]-t[0]
freq = np.fft.fftfreq(len(Fu))#, d=timestep) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html

plt.figure()
plt.subplot(2,1,2)
plt.title("Transformada Señal implementacion propia")
plt.plot(freq,Fu)
plt.grid()
#plt.savefig("TransformadaSenal.png")

FuS= fu(fS, len(fS))
#timestep = 0.1
freqS = np.fft.fftfreq(len(FuS) )#, d=timestep) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html
plt.subplot(2,1,1)
plt.title("Transformada Señal sumanda implementacion propia")
plt.plot(freqS,FuS)
plt.grid()
plt.subplots_adjust(hspace=0.5)
#plt.savefig("TransformadaSenalSumada.png")
plt.savefig("TransformadasSenales.png")


#Espectogram
NFFT= len(f)
dt= t[1]-t[0]
Fs= int (1.0/dt) #Frecuencua de sampleo como en sismica

plt.figure()
plt.subplot(2,1,1)
plt.title("Senal sumada")
plt.plot(t, f)
plt.subplot(2,1,2)
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.specgram(fS, NFFT=NFFT, Fs=Fs, noverlap=900) # Recuperado de: https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py

NFFTS= len(fS)
dtS= tS[1]-tS[0]
FsS= int (1.0/dtS) #Frecuencua de sampleo como en sismica

plt.figure()
plt.subplot(2,1,1)
plt.title("Senal sumada")
plt.grid()
plt.plot(tS, fS)
plt.subplot(2,1,2)
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
Pxx, freqs, bins, im= plt.specgram(fS, NFFT=512, Fs=2) # Recuperado de: https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
