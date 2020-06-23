#include<iostream>

using namespace std;

double g(double x)
{
	return x * x;
}

double h(double x)
{
	return sqrt(4 - x * x);
}

double integrateTR(double f(double), double a, double b, int n)
{
	double h = (b - a) / n;
	double result = 0;

	for (int i = 1; i <= n;i++)
		result += h / 2 * (f(a + (i - 1)*h) + f(a + i * h));
	
	return result;

}

int main()
{
	
	cout << integrateTR(h, -2, 2, 10000);


	_getwch();
	return 0;
}