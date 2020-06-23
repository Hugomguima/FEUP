#include <iostream>
using namespace std;

int main()
{
	float a1, a2, b1, b2, c1, c2, ab, ac, cb, s, area;

	cout << "Introduza as coordenadas de a : ";
	cin >> a1 >> a2;

	cout << "Introduza as coordenadas de b : ";
	cin >> b1 >> b2;

	cout << "Introduza as coordenadas de c : ";
	cin >> c1 >> c2;

	ab = sqrt((a2 - b2)*(a2 - b2) + (a1 - b1)*(a1 - b1));
	ac = sqrt((a2 - c2)*(a2 - c2) + (a1 - c1)*(a1 - c1));
	cb = sqrt((c2 - b2)*(c2 - b2) + (c1 - b1)*(c1 - b1));

	s = (ab + ac + cb) / 2;
	
	area = sqrt(s*(s - ab)*(s - ac)*(s - cb));

	cout << "A area do triangulo e : " << area;

	_getwch();
	return 0;
}