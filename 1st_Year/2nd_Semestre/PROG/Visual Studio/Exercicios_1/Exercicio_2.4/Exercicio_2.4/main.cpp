#include<iostream>
using namespace std;

int main()
{
	float peso;

	cout << "Introduza o peso do veiculo : ";
	cin >> peso;

	if (peso < 500)
		cout << "O custo do transporte da mercadoria e : 5 euros";
	else
		if (peso >= 500 && peso <= 1000)
			cout << "O custo do transporte da mercadoria e : " << 5 + 1.5*int(peso - 500) / 100 << " euros";
		else
			if (peso > 1000)
				cout << "O custo do transporte da mercadoria e : " << 12.5 + 5 * int(peso - 1000) / 250 << " euros";



	_getwch();
	return 0;
}

