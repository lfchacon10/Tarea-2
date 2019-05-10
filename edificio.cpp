#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;
using std::cout;
using std::endl;
#define PI 3.14159265

float m = 1000.0; // masa del piso
float fric = 0.0;// Coeficiente de friccion
float k = 2000; // Rigidez
float ω = 1.0*(k/m); //Frecuencia de forzamiento
float dt=0.1;
float tFinal=10;


float  forzExterno (float w, float t)
{
  return sin(w*t*PI/180);
}
float ecuacion1( float u1, float u2, float v1, float w, float t)
{
  return -(fric/m)*v1 - 2*(k/m)*u1 + (k/m)*u2 + forzExterno(w,t)/m;
}
float ecuacion2( float u1, float u2, float u3, float v2)
{
  return -(fric/m)*v2 + (k/m)*u1 - 2*(k/m)*u2 + (k/m)*u3;
}
float ecuacion3( float u2, float u3, float v3)
{
  return -(fric/m)*v3 + (k/m)*u2 - (k/m)*u3;
}

void lf ( float u1, float u2, float u3,float v1, float v2, float v3, float t, float w  )
{
  int tamano = tFinal/dt;
  float u1[tamano];
  float u2[tamano];
  float u3[tamano];
  float v1[tamano];
  float v2[tamano];
  float v3[tamano];

  //Se iniciliazan los primeros puntos
  u1[0]=u1;
  u2[0]=u2;
  u3[0]=u3;

  v1[1]=v1;
  v2[1]=v2;
  v3[1]=v3;

  v1[0] = 0.5*dt*ecuacion1( u1pasado, u2pasado, v1pasado, w, t) +v1[0];
  v2[0] = 0.5*dt*ecuacion2( u1pasado, u2pasado, u3pasado, v2pasado)+v2[0];
  v3[0] = 0.5*dt*ecuacion3( u2pasado, u3pasado, v3pasado) + v3[0];

  u1[1]=dt*v1[0]+u1[0];
  u2[1]=dt*v2[0]+u2[0];
  u3[1]=dt*v3[0]+u3[0];

  //De ahi en adelante
  outfile.open("amplitudes.dat");
  for( int p= 0; p < tamano; p++ )
  {
    v1[p+2] = 2*dt*ecuacion1( u1[p+1], u2[p+1], v1[p+1], w, t) +v1[p];
    v2[p+2] = 2*dt*ecuacion2( u1[p+1], u2[p+1], u3[p+1], v2[p+1])+v2[p];
    v3[p+2] = 2*dt*ecuacion3( u2[p+1], u3[p+1], v3[p+1]) + v3[p];
    outfile << t << " " << u1 << " " << u2 << " " << u3 << " " << v1 << " " << v2 << " " << v3 << endl;
  }
  outfile.close();
}
/*
void rk ( float u1, float u2, float u3,float v1, float v2, float v3, float t, float w  )
{
  //Se iniciliazan las posiciones de acuerdo a las velocidades en t=0

  float puntos[4][6];
  puntos[0][0]= dt*v1;
  puntos[1][0]= dt*v1;
  puntos[2][0]= dt*v1;
  puntos[3][0]= dt*v1;


  puntos[0][1]= dt*v2;
  puntos[0][2]= dt*v3;
  //Posiciones futuras
  puntos[0][3]= dt*ecuacion1( u1,  u2,  v1,  w,  t);
  puntos[0][4]= dt*ecuacion2( u1,  u2,  u3,  v2);
  puntos[0][5]= dt*ecuacion3( u2,  u3,  v3);
}*/
//Derivada  posicion x
float derivada_x(float vx)
{
	return vx;
}
//Derivada posicion y
float derivada_y(float vy)
{
	return vy;
}


int main()
{
  float w = sqrt(k/m);
  float u1 = 0.0, u2 = 0.0, u3 = 0.0;
  float v1 = 0.0, v2 = 0.0, v3 = 0.0;

  //Para LeapFrog
  float u=0;
  float v=0;
  lf(u1, u2, u3, v1, v2, v3,t,w );




  //Para RungeKuta
  //rk(u1, u2, u3, v1, v2, v3,t,w );
	//return 0;
}
