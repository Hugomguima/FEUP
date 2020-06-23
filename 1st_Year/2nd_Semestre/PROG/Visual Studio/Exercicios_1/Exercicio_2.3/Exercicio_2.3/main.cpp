#include <iostream>

using namespace std;

int main()
{
	float n1, n2;
	char op;

	cout << "Introduza a operaçao aritmetica :" << endl;
	cin >> n1 >> op >> n2;

	switch (op)
	{
	case '+':
		cout << n1 + n2;
		break;
	case '-':
		cout << n1 - n2;
		break;
	case '*':
		cout << n1 * n2;
		break;
	case '/':
		cout << n1 / n2;
		break;

	}



	_getwch();
	return 0;
}