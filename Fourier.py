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

#def freReq(senal,dt): #Recibe la señal y la diferencia de tiempos.
#	n= np.size(senal)
#	mitad = int(n/2)
#	frecuencias= np.zeros(n)
#	for i in range (1,n):
#		if( i < mitad):
#			f= (1/dt)*i			 #Posibles frecuencias para el tiempo
#			frecuencias[i]= f
#		else:
#			f= (1/dt)*i
#			frecuencias[i]= f
#	return frecuencias
#lt.figure()
#imp= freReq(Fu,timestep)
#plt.plot(imp, Fu)


#Graficas Fourier
N= len(f)
Fu= fu(f,N )
timestep = t[1]-t[0]
freq = np.fft.fftfreq(len(Fu), timestep)#, d=timestep) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html

plt.figure()
plt.subplot(2,1,2)
plt.title("Transformada Señal")# implementacion propia")
plt.plot(freq,Fu)
plt.grid()

Ns= len(fS)
FuS= fu(fS, Ns)
timestepS = tS[1]-tS[0]
freqS = np.fft.fftfreq(len(FuS),timestepS ) # Recuperado de: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.fft.fftfreq.html
plt.subplot(2,1,1)
plt.title("Transformada Señal sumada")# implementacion propia")
plt.plot(freqS,FuS)
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.savefig("TransformadasSenales.png")


#Spectogram
dt= t[1]-t[0]
Fs= int (1.0/dt) #Cantidad de samples por unidad de tiempo. En nuestro caso será el array completo porque los datos son de menos de 1 segundo. Referencias: https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
FsS=int (1.0/dt)

plt.figure()
plt.subplot(2,1,1)
plt.title("Espectrograma señal sumada")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.specgram(fS,Fs=FsS)#, noverlap=900) # Recuperado de: https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
plt.subplots_adjust(hspace=0.5)
plt.savefig("EspectrogramaSenales.png")
plt.subplot(2,1,2)
plt.title("Espectrograma señal")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.specgram(f,Fs=Fs)#Referencia:https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
plt.savefig("EspectrogramaSenales.png")



#Señal sismica
datosTemblor= np.genfromtxt("temblor.txt",skip_header=4)
dt = 1/100 #En el documento aparece que la frecuencia de sampleo fue  100Hz. Como Hz son s^-1 siginifica que 1/hz nos dara el dt que existe entre los datos.
n= len(datosTemblor)
t= np.linspace(0,n*dt,len(datosTemblor))

plt.figure()
plt.title("Datos temblor")
plt.plot(t,datosTemblor)
plt.ylabel("Amplitud")
plt.xlabel("Tiempo (s)")
plt.grid()

#Transformada señal
f= np.fft.fft(datosTemblor)
n=len(f)
timestep = dt
freq = np.fft.fftfreq(n, d=timestep)

plt.figure()
plt.title("Transformada Fourier señal sismica")
plt.grid()
plt.plot(freq,f)
plt.ylabel("Amplitud")
plt.xlabel("Frecuencia (Hz)")

#Spectogram señal sismica

FsSismo= int (1.0/dt) #Cantidad de samples por unidad de tiempo. En nuestro caso será el array completo porque los datos son de menos de 1 segundo. Referencias: https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
plt.title("Espectrograma señal sismica")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.specgram(datosTemblor, Fs=FsSismo)#Referencia:https://matplotlib.org/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-gallery-images-contours-and-fields-specgram-demo-py
plt.show()
