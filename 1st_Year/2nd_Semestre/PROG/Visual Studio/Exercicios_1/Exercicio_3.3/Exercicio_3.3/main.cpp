#include<iostream>
#include<iomanip>
#include<cmath>

using namespace std;

double raiz(double num, int ite)
{
	double n, rq, rqn, dif, x;

	rq = 1;
	rqn = (rq + num / rq) / 2;
	dif = num - rqn * rqn;

	for(;ite>0;ite--)
	{
		rq = rqn;
		rqn = (rqn + num / rqn) / 2;
		dif = num - rqn * rqn;

	}
	return rqn;



}

int main()
{
	double number;
	int iterations;

	cout << "Introduza un numero : ";
	cin >> number;
	cout << "Introduza o numero de iteracoes que deseja : ";
	cin >> iterations;

	cout << "\nA raiz quadrada segundo o metodo do exercicio 2.14 e : " << raiz(number, iterations) << endl;
	cout << "A raiz quadrada segundo a funcao de C++ e : " << sqrt(number) << endl << endl;

	cout << "Logo, a diferenca entreos valores e : " << abs(sqrt(number) - raiz(number, iterations));

	_getwch();
	return 0;
}