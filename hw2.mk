Resultados_hw2.pdf: Senal.png TransformadasSenales.png amplitud1.png amplitud2.png amplitud3.png amplitud4.png


Senal.png: Fourier.py
	python Fourier.py

TransformadasSenales.png:Fourier.py
	python Fourier.py

amplitud1.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitud2.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitud3.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py

amplitud4.png:Plotws_hw2.py amp.dat
	python Plotws_hw2.py


amp.dat: Edificio.cpp
	g++ edificio.cpp
	./a.out
