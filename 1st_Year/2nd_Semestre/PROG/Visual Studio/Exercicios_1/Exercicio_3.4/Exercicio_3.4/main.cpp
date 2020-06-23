#include<iostream>

using namespace std;

double round(double x, unsigned n){

	return  floor(x * pow(10,n) + 0.5) / pow(10,n);
}

int main()
{
	double numero;
	int casas;

	cout << "Introduza um numero : ";
	cin >> numero;
	cout << "A quantas casas decimais deseja arredondar? ";
	cin >> casas;

	cout << endl << round(numero, casas);

	_getwch();
	return 0;
}
