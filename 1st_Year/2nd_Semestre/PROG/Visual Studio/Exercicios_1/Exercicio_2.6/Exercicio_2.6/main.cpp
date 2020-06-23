#include<iostream>
using namespace std;

int main()
{
	char alinea;

	cout << "Escolha a alinea : ";
	cin >> alinea;

	switch (alinea)
	{
	case 'a':
		int n, counter;
		cout << "Introduza um numero inteiro : ";
		cin >> n;
		counter = 0;
		

		for (int i = 1; i <= n; i = i + 1)
		{
			if (n % i == 0)
				counter += 1;
		}
		if (counter == 2)
			cout << n << " e um numero primo";
		else
			cout << n << " nao e um numero primo";
		break;


	case 'b':
		
		int counter_1, counter_2;

		counter_2 = 0;

		for (int i = 1; counter_2 <= 100; i = i + 1)
		{
			counter_1 = 0;
			for (int j = 1; j <= i; j = j + 1)
			{
				if (i % j == 0)
					counter_1 += 1;
			}
			if (counter_1 == 2)
			{
				cout << i << endl;
				counter_2 += 1;
			}		
		}
		break;

	case 'c':
		int contador_1, contador_2;

		contador_2 = 0;

		for (int i = 1; contador_2 <= 1000; i += 1)
		{
			contador_1 = 0;
			contador_2 += 1;

			for (int j = 1; j <= i; j += 1)
			{
				if (i % j == 0)
					contador_1 += 1;
			}
			if (contador_1 == 2)
				cout << i << endl;
		}
		break;
	}

	






	_getwch();
	return 0;
}
