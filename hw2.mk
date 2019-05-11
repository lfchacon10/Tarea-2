Resultados_hw2.pdf: Senal.png TransformadasSenales.png EspectrogramaSenales.png EspectrogramaTemblor.png
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

amplitud1.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

#amplitud2.png:Plotws_hw2.py amp.dat
#	python Plotws_hw2.py

#amplitud3.png:Plotws_hw2.py amp.dat
#	python Plotws_hw2.py

#amplitud4.png:Plotws_hw2.py amp.dat
#	python Plotws_hw2.py

amp.dat: Edificio.cpp
	g++ edificio.cpp
	./a.out 2.0
