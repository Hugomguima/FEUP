#include<iostream>

using namespace std;

int main()
{
	double n, q, j, montante;

	cout << "Introduza o numero de anos : \n";
	cin >> n;
	cout << "Introduza o deposito da quantia inicial : \n";
	cin >> q;
	cout << "Introduza a taxa anual de juro : \n";
	cin >> j;
	j = j / 100;

	montante = q*(pow(1+j,n)-1);

	cout << "Podera levantar  o montante de : " << montante << " euros";


	_getwch();
	return 0;
}