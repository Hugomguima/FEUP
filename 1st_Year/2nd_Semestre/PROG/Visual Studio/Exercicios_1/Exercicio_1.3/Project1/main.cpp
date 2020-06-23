#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

int main()
{	
	float p;
	float r;
	float M;


	cout << "Introduza a massa especifica do material em Kilogramas(Kg) : ";
	cin >> p;
	cout << "Introduza o raio da esfera em metros(m) : ";
	cin >>  r;

	M = 4 / 3 * p * M_PI *(r*r*r);
	
	cout << "A massa da esfera e de " << M << "Kg";

	_getwch();
	return 0;
}