#include<iostream>

using namespace std;

int isPrime(int n)
{
	int counter = 0;
	for (int i = 1; i <= n; i++)
	{
		if (n % i == 0)
			counter += 1;
	}
	if (counter == 2)
		return 1;
	else
		return 0;
}


int main()
{
	double x;
	cout << "Introduza um numero : ";
	cin >> x;
	if (isPrime(x))
		cout << "O numero " << x << " e primo" << endl;
	else
		cout << "O numero " << x << " nao e primo" << endl;

	_getwch();
	return 0;
}