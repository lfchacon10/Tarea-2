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
float ecuacion1( float u1, float u2, float v1, float w, float t)
{
  return -(fric/m)*v1 - 2*(k/m)*u1 + (k/m)*u2 + forzamiento(w,t)/m;
}
float ecuacion2( float u1, float u2, float u3, float v2)
{
  return -(fric/m)*v2 + (k/m)*u1 - 2*(k/m)*u2 + (k/m)*u3;
}
float ecuacion3( float u2, float u3, float v3)
{
  return -(fric/m)*v3 + (k/m)*u2 - (k/m)*u3;
}

float lf ( float u, int v)
{
  //Se iniciliazan los tres primeros puntos
  float puntos[3][3];

}

float rk ( float u1, float u2, float u3,float v1, float v2, float v3, float t, float w  )
{
  //Se iniciliazan las posiciones de acuerdo a las velocidades en t=0

  float puntos[4][6];
  puntos[0][0]= dt*v1;
  puntos[0][1]= dt*v2;
  puntos[0][2]= dt*v3;
  //Posiciones futuras
  puntos[0][3]= dt*ecuacion1( u1,  u2,  v1,  w,  t);
  puntos[0][4]= dt*ecuacion2( u1,  u2,  u3,  v2);
  puntos[0][5]= dt*ecuacion3( u2,  u3,  v3);


}
int main()
{
  //Para LeapFrog
  float u=0;
  float v=0;
  float x0=lf(u, v);


  //Para RungeKuta
  float u1 = 0.0, u2 = 0.0, u3 = 0.0;
  float v1 = 0.0, v2 = 0.0, v3 = 0.0;

  float x0=rk(u, v);

	return 0;
}
