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
float dt=0.1;
float tFinal=100;

float  forzExterno (float w, float t)
{
  return sin(w*t);
}
float ecuacion1( float u1, float u2, float v1, float w, float t)
{
  return -fric/m*v1 - 2*k/m*u1 + k/m*u2 + forzExterno(w,t)/m;
}
float ecuacion2( float u1, float u2, float u3, float v2)
{
  return -fric/m*v2 + k/m*u1 - 2*k/m*u2 + k/m*u3;
}
float ecuacion3( float u2, float u3, float v3)
{
  return -fric/m*v3 + k/m*u2 - k/m*u3;
}

void lf ( float u1value, float u2value, float u3value,float v1value, float v2value, float v3value, float tFinal, float w  )
{
  float di=2.8/100;
  ofstream outfile;
  outfile.open("amp.dat");
  for (float i=0.2; i <3; i+=di) //crea los valores para distintos W
  {
    int tamano = tFinal/dt;
    float u1[tamano];
    float u2[tamano];
    float u3[tamano];
    float v1[tamano];
    float v2[tamano];
    float v3[tamano];

    //Se iniciliazan los primeros puntos
    u1[0]=u1value;
    u2[0]=u2value;
    u3[0]=u3value;

    v1[1]=v1value;
    v2[1]=v2value;
    v3[1]=v3value;

    v1[0] = dt*ecuacion1( u1[0], u2[0], v1[1], w*i, 0)+v1[1];
    v2[0] = dt*ecuacion2( u1[0], u2[0], u3[0], v2[1])+v2[1];
    v3[0] = dt*ecuacion3( u2[0], u3[0], v3[1]) + v3[1];

    u1[1]=dt*v1[0]+u1[0];
    u2[1]=dt*v2[0]+u2[0];
    u3[1]=dt*v3[0]+u3[0];

    //De ahi en adelante
    for( int p= 0; p < tamano; p++ )
    {
      u1[p+2]=2*dt*v1[p+1]+u1[p];
      u2[p+2]=2*dt*v2[p+1]+u2[p];
      u3[p+2]=2*dt*v3[p+1]+u3[p];
      v1[p+2] = 2*dt*ecuacion1( u1[p+1], u2[p+1], v1[p+1], w*i, p*dt) +v1[p]; //Aca se usa el i
      v2[p+2] = 2*dt*ecuacion2( u1[p+1], u2[p+1], u3[p+1], v2[p+1])+v2[p];
      v3[p+2] = 2*dt*ecuacion3( u2[p+1], u3[p+1], v3[p+1]) + v3[p];
    }

    //Crea el archivo
    for ( int i=0; i<tamano;i++)
    {
      outfile << i*dt << "," << u1[i] << "," << u2[i] << "," << u3[i]<<endl;// << "," << v1[i] << "," << v2[i] << "," << v3[i] << endl;
    }
  }
  outfile.close();

}

void lfBono ( float u1value, float u2value, float u3value,float v1value, float v2value, float v3value, float tFinal, float w  )
{
  float di=100000/100;
  ofstream outfile;
  outfile.open("bono.dat");
  for (float i=0.2; i <100000; i+=di) //crea los valores para distintos W
  {
    int tamano = tFinal/dt;
    float u1[tamano];
    float u2[tamano];
    float u3[tamano];
    float v1[tamano];
    float v2[tamano];
    float v3[tamano];

    //Se iniciliazan los primeros puntos
    u1[0]=u1value;
    u2[0]=u2value;
    u3[0]=u3value;

    v1[1]=v1value;
    v2[1]=v2value;
    v3[1]=v3value;

    v1[0] = dt*ecuacion1( u1[0], u2[0], v1[1], w*i, 0)+v1[1];
    v2[0] = dt*ecuacion2( u1[0], u2[0], u3[0], v2[1])+v2[1];
    v3[0] = dt*ecuacion3( u2[0], u3[0], v3[1]) + v3[1];

    u1[1]=dt*v1[0]+u1[0];
    u2[1]=dt*v2[0]+u2[0];
    u3[1]=dt*v3[0]+u3[0];

    //De ahi en adelante
    for( int p= 0; p < tamano; p++ )
    {
      u1[p+2]=2*dt*v1[p+1]+u1[p];
      u2[p+2]=2*dt*v2[p+1]+u2[p];
      u3[p+2]=2*dt*v3[p+1]+u3[p];
      v1[p+2] = 2*dt*ecuacion1( u1[p+1], u2[p+1], v1[p+1], w*i, p*dt) +v1[p]; //Aca se usa el i
      v2[p+2] = 2*dt*ecuacion2( u1[p+1], u2[p+1], u3[p+1], v2[p+1])+v2[p];
      v3[p+2] = 2*dt*ecuacion3( u2[p+1], u3[p+1], v3[p+1]) + v3[p];
    }

    //Crea el archivo
    for ( int i=0; i<tamano;i++)
    {
      outfile << i*dt << "," << u1[i] << "," << u2[i] << "," << u3[i]<<endl;// << "," << v1[i] << "," << v2[i] << "," << v3[i] << endl;
    }
  }
  outfile.close();

}

int main()
{
  float w = sqrt(k/m);
  float u1value = 0.0, u2value = 0.0, u3value = 0.0;
  float v1value = 0.0, v2value = 0.0, v3value = 0.0;
  //Para LeapFrog
  lf(u1value, u2value, u3value, v1value, v2value, v3value,tFinal,w );
  //Caso Bono

  m = 600000; // masa del piso
  fric = 0.005;// Coeficiente de friccion
  k = 20000; // Rigidez
  dt=0.1;
  tFinal=100;
  lfBono(u1value, u2value, u3value, v1value, v2value, v3value,tFinal,w );

}
