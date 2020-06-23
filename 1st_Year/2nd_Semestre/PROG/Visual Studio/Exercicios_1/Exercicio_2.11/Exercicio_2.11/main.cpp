#include<iostream>
#include<cmath>

using namespace std;

int factorial(int n)
{
	return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

int main()
{
	char alinea;
	double sum = 0;
	double total = 1;
	double resultado = 1;
	double j = -1;
	double x;
	int expoente = 1;
	double k = -1;
	double sinal;




	cout << "Introduza a alinea que deseja : ";
	cin >> alinea;

	switch (alinea)
	{
	case 'a':
		for (double i = 1; i <= 9999999999999999999; i = (2 * i + 1) * -1)	
			sum += 4 / i;
		cout << sum;
		break;
	case 'b':
		while (j <= 99999999999)
		{
			j *= (j + 1);
			resultado += 1 / j;
			
		}
		cout << resultado;
		break;
	case 'c':

		cout << "Introduza a variavel da serie : ";
		cin >> x;

		while (expoente <= 10)
		{
			if (expoente % 2 == 0)
				sinal = 1;
			else
				sinal = -1;

			total += pow(x, expoente) / factorial(expoente) * sinal;
			expoente += 1;
		}
		cout << total;
		break;
	}


	_getwch();
	return 0;
}