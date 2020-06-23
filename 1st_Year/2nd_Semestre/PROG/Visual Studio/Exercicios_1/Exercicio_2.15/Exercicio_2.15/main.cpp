#include<iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
	double t1, t2, t;
	int resultado;
	int n1 = rand() % 8 + 2;
	int n2 = rand() % 8 + 2;

	cout << n1 << " * " << n2 << " = ";
	t1 = time(NULL);
	cin >> resultado;
	t2 = time(NULL);

	t = t2 - t1;

	if (resultado != n1 * n2)
		cout << "Muito Mau";
	else if (t < 5)
		cout << "Bom";
	else if (t <= 5 && t <= 10)
		cout << "Satisfaz";
	else
		cout << "Insuficiente";




	_getwch();
	return 0;
}