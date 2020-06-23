#include<iostream>

using namespace std;

long int factorial_ite(int n)
{
	int result = 1;
	for (int i = 1; i <= n; i++)
	{
		result *= i;
		cout << result << endl;
	}
	return result;
}

long int factorial_rec(int n)
{
	if (n <= 1)
		return 1;
	
	return n * factorial_rec(n - 1);



}

int main()
{
	int num;
	cout << "Introduza o numero : ";
	cin >> num;
	cout << factorial_rec(num);

	_getwch();
	return 0;
}