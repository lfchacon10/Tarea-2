#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;

float m = 1000.0; // masa del piso
float fric = 0.0;// Coeficiente de friccion
float k = 2000; // Rigidez
float ω = 1.0*(k/m); //Frecuencia de forzamiento
float dt=0.1;

float  forzExterno (float w, float t)
{
  return sin(w*t*PI/180);
}
float ecuacion1( float u1, float u1, float v1, float v2, float w,)
{
  return -(fric/m)*v1 - 2*(k/m)*u1 + (k/m)*u2 + forzamiento(w,t)/m;
}
float ecuacion2( float u1, float u1, float v1, float v2, float w,)
{
  return -(fric/m)*v2 + (k/m)*u1 - 2*(k/m)*u2 + (k/m)*u3;
}
float ecuacion3( float u2, float u3, float v3)
{
  return -(fric/m)*v3 + (k/m)*u2 - (k/m)*u3;
}

float lf ( float ang, int pun)
{
  //Se iniciliazan los tres primeros puntos
  float puntos[3][3];

}


float rk ( float ang, int pun)
{
  //Se iniciliazan los tres primeros puntos
  float puntos[3][3];

}
int main()
{
  float u=0;
  float v=0;
  float x0=lf(u, v);

	return 0;
}
