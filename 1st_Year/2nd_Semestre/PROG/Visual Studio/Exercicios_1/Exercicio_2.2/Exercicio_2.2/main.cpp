#include<iostream>
using namespace std;

int main()
{
	double a, b, c;
	char alinea;

	cout << "A ? ";
	cin >> a;
	cout << "B ? ";
	cin >> b;
	cout << "C ? ";
	cin >> c;

	cout << "Escolha a alinea que deseja executar : ";
	cin >> alinea;

	switch(alinea)
	{
	case 'a':
		if (a >= b && a >= c)
			cout << "O maior numero e : " << a;
		else
		{
			if (b >= a && b >= c)
				cout << "O maior numero e : " << b;
			else
			{
				if (c >= a && c >= b)
					cout << "O maior numero e : " << c;
			}
		}

		if (a <= b && a <= c)
			cout << "\nO menor numero e : " << a;
		else
		{
			if (b <= a && b <= c)
				cout << "\nO menor numero e : " << b;
			else
			{
				if (c <= a && c <= b)
					cout << "\nO menor numero e : " << c;
			}
		}
		break;
	case 'b':
		if (a >= b && b >= c && b >= c)
			cout << "\nOs numeros por ordem decrescente sao : " << a << " " << b << " " << c;
		else
			if (a >= b && b >= c && c >= b)
				cout << "\nOs numeros por ordem decrescente sao : " << a << " " << c << " " << b;
			else
				if (b >= a && b >= c && a >= c)
					cout << "\nOs numeros por ordem decrescente sao : " << b << " " << a << " " << c;
				else
					if (b >= a && b >= c && c >= a)
						cout << "\nOs numeros por ordem decrescente sao : " << b << " " << c << " " << a;
					else 
						if (c >= a && c >= b && a >= b)
							cout << "\nOs numeros por ordem decrescente sao : " << c << " " << a << " " << c;
						else
							if (c > a && c > b && b > a)
								cout << "\nOs numeros por ordem decrescente sao : " << c << " " << b << " " << a;
		break;

	case 'c':
		if (a >= b + c | b >= a + c | c >= a + b)
			cout << "Estes valores permitem a construcao de um triangulo";
		else
			if (a < b + c | b < a + c | c < a + b)
				cout << "Estes valores nao permitem a construcao de um triangulo";
		break;
	default:
		break;
	}

	_getwch();
	return 0;
}