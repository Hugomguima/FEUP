#include<iostream>

using namespace std;

int main()
{
	double contador, n, soma, media, menor, maior, i;
	char alinea;

	cout << "Introduza a alinea que deseja : ";
	cin >> alinea;

	contador = 0;
	soma = 0;
	maior = 0;	
	menor = 9999999999999;
	media = 0;
	n = 1;

	switch (alinea)
	{
	case 'a':

		while (n != 0)
		{
			cout << "Introduza um numero para continuar\n" << "Introduza 0 para terminar o programa \n";
			cin >> n;

			if (n == 0)
				break;

			contador += 1;
			soma += n;
			media = soma / contador;
			if (n > maior)
				maior = n;
			if (n < menor)
				menor = n;
		}
		cout << "\nA sequencia tem " << contador << " elementos" << endl;
		cout << "A soma da sequencia e : " << soma << endl;
		cout << "A media da sequencia e : " << media << endl;
		cout << "O menor numero da sequencia e : " << menor << endl;
		cout << "O maior numero da sequencia e : " << maior << endl;
		break;

	case 'b':
		
		cout << "Introduza o numero de elementos da sequencia : ";
		cin >> contador;
		i = contador;

		for (contador; contador > 0; contador -= 1)
		{
			cout << "Introduza um novo elemento da sequencia : ";
			cin >> n;

			soma += n;
			media = soma / i;
			if (n > maior)
				maior = n;
			if (n < menor)
				menor = n;


		}
		cout << "\nA soma da sequencia e : " << soma << endl;
		cout << "A media da sequencia e : " << media << endl;
		cout << "O menor numero da sequencia e : " << menor << endl;
		cout << "O maior numero da sequencia e : " << maior << endl;

		break;

	case 'c':
		while (n != 0)
		{
			cout << "Introduza um novo elemento da sequencia : (CTRL-Z to end) ? ";
			cin >> n;

			contador += 1;
			soma += n;
			media = soma / contador;
			if (n > maior)
				maior = n;
			if (n < menor)
				menor = n;
		}
		cout << "\nA sequencia tem " << contador << " elementos" << endl;
		cout << "A soma da sequencia e : " << soma << endl;
		cout << "A media da sequencia e : " << media << endl;
		cout << "O menor numero da sequencia e : " << menor << endl;
		cout << "O maior numero da sequencia e : " << maior << endl;
		break;
	}

	_getwch();
	return 0;
}