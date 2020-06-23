#include<iostream>
using namespace std;

int main()
{
	double a, b, c, x1, x2, x3;

	cout << "Introduza os coeficientes (a b c): " << endl;
	cin >> a >> b >> c;

	x1 = (-b + sqrt(b*b - 4 * a*c)) / 2 * a;
	x2 = (-b - sqrt(b*b - 4 * a*c)) / 2 * a;

	if (b*b - 4 * a*c >= 0 && x1 == x2)
		cout << "A equacao tem 2 raizes reais iguais: " << x1;
	else
		if (b*b - 4 * a*c > 0 && x1 != x2)
			cout << "A equacao tem 2 raizes reais diferentes " << x1 << " e " << x2;
		else
			if (b*b - 4 * a*c < 0)
			{
				x1 = -b / 2 * a;
				x2 = sqrt(-(b*b - 4 * a*c)) / 2 * a;
				cout << "A equacao tem 2 raizes complexas conjugadas " << x1 << "+" << x2 << "i" << " e " << x1 << "-" << x2 << "i";
			}

	_getwch();
	return 0;
}