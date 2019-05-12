Resultados_hw2.pdf: Senal.png TransformadasSenales.png EspectrogramaSenales.png EspectrogramaTemblor.png amplitudes.png amplitud1.png amplitud2.png amplitud3.png amplitudesMax.png amplitudes04.png amplitudes12.png amplitudes17.png amplitudes30.png amplitudesBONO.png amplitudesMaxBono.png
	pdflatex Resultados_hw2.tex

Senal.png: Fourier.py
	python Fourier.py

TransformadasSenales.png:Fourier.py
	python Fourier.py

EspectrogramaSenales.png:Fourier.py
	python Fourier.py

SenalSismica.png:Fourier.py
	python Fourier.py

TransformadaFourierSenalSismica.png:Fourier.py
	python Fourier.py

EspectrogramaTemblor.png:Fourier.py
	python Fourier.py

amplitudes.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitud1.png:Plotws_hw2.py amp.dat
			python Plotws_hw2.py

amplitud2.png:Plotws_hw2.py amp.dat
			python Plotws_hw2.py

amplitud3.png:Plotws_hw2.py amp.dat
			python Plotws_hw2.py

amp.dat: edificio.cpp
	g++ edificio.cpp
	./a.out

amplitud1.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudesMax.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudes04.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudes12.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudes17.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudes30.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitudesMaxBono.png:Plotws_hw2.py bono.dat
	python Plotws_hw2.py

amplitudesBONO.png:Plotws_hw2.py bono.dat
	python Plotws_hw2.py
